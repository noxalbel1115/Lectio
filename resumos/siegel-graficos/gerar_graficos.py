"""Gera os gráficos SVG do resumo de Siegel. Uso: python3 gerar_graficos.py resumos/siegel-graficos"""
import math
import os
import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

W = 600
FONT = "system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif"

CSS = """
.bg{fill:#fcfcfb;stroke:rgba(11,11,11,.10)}
.ink{fill:#0b0b0b}.ink2{fill:#52514e}.mut{fill:#898781}
.grid{stroke:#e1e0d9;stroke-width:1}.axis{stroke:#c3c2b7;stroke-width:1}
.ref{stroke:#52514e;stroke-width:1}
.s1{fill:#2a78d6}.s1s{stroke:#2a78d6}.s1w{fill:#2a78d6;fill-opacity:.10}
.s2{fill:#eb6834}.s2s{stroke:#eb6834}.s2w{fill:#eb6834;fill-opacity:.10}
.s3{fill:#1baf7a}
.gray{fill:#c3c2b7}.grays{stroke:#c3c2b7}
.neg{fill:#2a78d6}.pos{fill:#e34948}.posl{fill:#e34948;fill-opacity:.40}
.ring{stroke:#fcfcfb}.surf{fill:#fcfcfb}
.onfill{fill:#ffffff}
@media (prefers-color-scheme: dark){
.bg{fill:#1a1a19;stroke:rgba(255,255,255,.10)}
.ink{fill:#ffffff}.ink2{fill:#c3c2b7}.mut{fill:#898781}
.grid{stroke:#2c2c2a}.axis{stroke:#383835}
.ref{stroke:#c3c2b7}
.s1{fill:#3987e5}.s1s{stroke:#3987e5}.s1w{fill:#3987e5;fill-opacity:.14}
.s2{fill:#d95926}.s2s{stroke:#d95926}.s2w{fill:#d95926;fill-opacity:.14}
.s3{fill:#199e70}
.gray{fill:#52514e}.grays{stroke:#52514e}
.neg{fill:#3987e5}.pos{fill:#e66767}.posl{fill:#e66767;fill-opacity:.45}
.ring{stroke:#1a1a19}.surf{fill:#1a1a19}
}
"""


def br(v, nd=1):
    """Número no formato brasileiro."""
    s = f"{v:,.{nd}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def t(x, y, s, cls="ink", size=14, anchor="start", weight=400, extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" font-size="{size}" '
            f'text-anchor="{anchor}" font-weight="{weight}" {extra}>{escape(s)}</text>')


def line(x1, y1, x2, y2, cls="grid", extra=""):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="{cls}" {extra}/>'


def col(x, w, y0, y1, cls, r=4):
    """Coluna vertical com ponta arredondada (lado dos dados) e base reta."""
    h = abs(y1 - y0)
    r = min(r, h / 2, w / 2)
    if y1 < y0:
        d = (f"M{x:.1f},{y0:.1f} L{x:.1f},{y1 + r:.1f} Q{x:.1f},{y1:.1f} {x + r:.1f},{y1:.1f} "
             f"L{x + w - r:.1f},{y1:.1f} Q{x + w:.1f},{y1:.1f} {x + w:.1f},{y1 + r:.1f} L{x + w:.1f},{y0:.1f} Z")
    else:
        d = (f"M{x:.1f},{y0:.1f} L{x:.1f},{y1 - r:.1f} Q{x:.1f},{y1:.1f} {x + r:.1f},{y1:.1f} "
             f"L{x + w - r:.1f},{y1:.1f} Q{x + w:.1f},{y1:.1f} {x + w:.1f},{y1 - r:.1f} L{x + w:.1f},{y0:.1f} Z")
    return f'<path d="{d}" class="{cls}"/>'


def hbar(x0, x1, y, h, cls, r=4, round_end=True):
    """Barra horizontal; arredonda só a ponta direita."""
    w = x1 - x0
    if w <= 0:
        return ""
    if not round_end:
        return f'<rect x="{x0:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" class="{cls}"/>'
    r = min(r, w / 2, h / 2)
    d = (f"M{x0:.1f},{y:.1f} L{x1 - r:.1f},{y:.1f} Q{x1:.1f},{y:.1f} {x1:.1f},{y + r:.1f} "
         f"L{x1:.1f},{y + h - r:.1f} Q{x1:.1f},{y + h:.1f} {x1 - r:.1f},{y + h:.1f} L{x0:.1f},{y + h:.1f} Z")
    return f'<path d="{d}" class="{cls}"/>'


def swatch(x, y, cls):
    return f'<rect x="{x:.1f}" y="{y - 10:.1f}" width="12" height="12" rx="3" class="{cls}"/>'


def frame(name, h, title, subtitle, note, body, desc):
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" '
        f'role="img" aria-labelledby="tt dd" style="font-family:{FONT}">',
        f'<title id="tt">{escape(title)}</title><desc id="dd">{escape(desc)}</desc>',
        f"<style>{CSS}</style>",
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="12" class="bg"/>',
        t(24, 36, title, "ink", 18, weight=600),
    ]
    if subtitle:
        for i, s in enumerate(subtitle.split("\n")):
            parts.append(t(24, 60 + i * 19, s, "ink2", 14))
    parts.extend(body)
    if note:
        for i, s in enumerate(note.split("\n")):
            parts.append(t(24, h - 18 - (len(note.split("\n")) - 1 - i) * 17, s, "mut", 12))
    parts.append("</svg>")
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write("\n".join(parts))


# ---------------------------------------------------------------- Fig. 1
def fig_dolar_1802():
    data = [("Ações", 704997, "US$ 704.997", "s1"),
            ("Títulos", 1778, "US$ 1.778", "gray"),
            ("Letras", 281, "US$ 281", "gray"),
            ("Ouro", 3.12, "US$ 3,12", "gray"),
            ("Dólar", 0.05, "US$ 0,05", "gray")]
    x0, x1 = 120, 470
    lo, hi = -2, 6  # log10 de 0,01 a 1.000.000

    def X(v):
        return x0 + (math.log10(v) - lo) / (hi - lo) * (x1 - x0)

    top, rowh = 136, 46
    body = []
    ticks = [(0.01, "0,01"), (1, "1"), (100, "100"), (1e4, "10 mil"), (1e6, "1 milhão")]
    ybot = top + rowh * len(data) - 14
    for v, lab in ticks:
        body.append(line(X(v), top - 18, X(v), ybot, "grid"))
        body.append(t(X(v), ybot + 20, lab, "mut", 13, "middle"))
    body.append(line(X(1), top - 22, X(1), ybot, "ref"))
    body.append(t(X(1) + 6, top - 26, "US$ 1 aplicado em 1802", "ink2", 13))
    for i, (lab, v, vlab, cls) in enumerate(data):
        y = top + i * rowh + 8
        body.append(t(x0 - 14, y + 5, lab, "ink", 15, "end", 600 if i == 0 else 400))
        stroke = "s1s" if cls == "s1" else "grays"
        body.append(line(X(1), y, X(v), y, stroke, 'stroke-width="2" stroke-linecap="round"'))
        body.append(f'<circle cx="{X(v):.1f}" cy="{y}" r="6" class="{cls} ring" stroke-width="2"/>')
        if v >= 1:
            body.append(t(X(v) + 12, y + 5, vlab, "ink", 14, weight=600 if i == 0 else 400))
        else:
            body.append(t(X(v), y - 13, vlab, "ink", 14, "middle"))
    frame("fig01-dolar-de-1802.svg", 420,
          "Quanto valeria em 2012 US$ 1 aplicado em 1802",
          "Valor em poder de compra (descontada a inflação), com reinvestimento\ndos rendimentos. Escala logarítmica: cada marca vale 100 vezes a anterior.",
          "Fonte: Siegel, 5ª ed., figura de abertura do livro (dados de 1802 a 2012).", body,
          "Ações: 704.997 dólares; títulos: 1.778; letras: 281; ouro: 3,12; dólar: 0,05.")


# ---------------------------------------------------------------- Fig. 2
def fig_alavancagem():
    data = [("Sem dívida", "1 : 1", 3), ("10 : 1", "", 30), ("20 : 1", "", 60), ("30 : 1", "", 90)]
    left, right, y0, ymax = 92, 560, 120, 330
    body = []

    def Y(p):
        return y0 + p / 100 * (ymax - y0)

    for p in (0, 25, 50, 75, 100):
        body.append(line(left, Y(p), right, Y(p), "grid" if p else "axis"))
        body.append(t(left - 10, Y(p) + 4, f"−{p}%" if p else "0%", "mut", 13, "end"))
    n = len(data)
    band = (right - left) / n
    bw = 24
    for i, (lab, sub, p) in enumerate(data):
        cx = left + band * (i + 0.5)
        body.append(t(cx, y0 - 26, lab, "ink", 14, "middle", 600))
        if sub:
            body.append(t(cx, y0 - 9, sub, "mut", 12, "middle"))
        body.append(col(cx - bw / 2, bw, Y(0), Y(p), "s1"))
        body.append(t(cx, Y(p) + 20, f"−{p}%", "ink", 15, "middle", 600))
    body.append(t(24, ymax + 52, "A 30 : 1, basta uma queda de 3,3% nos ativos para zerar o patrimônio.", "ink2", 14))
    frame("fig02-alavancagem.svg", 420,
          "Uma queda de 3% nos ativos, conforme a alavancagem",
          "Perda de patrimônio próprio para cada relação entre ativos e capital próprio",
          "Cálculo ilustrativo: perda do patrimônio = queda dos ativos × alavancagem.", body,
          "Com queda de 3% nos ativos, o patrimônio cai 3% sem dívida, 30% a 10:1, 60% a 20:1 e 90% a 30:1.")


# ---------------------------------------------------------------- Fig. 3
def fig_risk_on_off():
    rows = ["Ações", "Commodities", "Dólar", "Títulos do Tesouro"]
    on = [True, True, False, False]
    cols = [("Risk-on", "boas notícias"), ("Risk-off", "más notícias")]
    x_lab, xs, top, rowh = 24, [290, 450], 120, 52
    body = []
    for j, (c, sub) in enumerate(cols):
        body.append(t(xs[j], top - 26, c, "ink", 15, "middle", 600))
        body.append(t(xs[j], top - 8, sub, "mut", 13, "middle"))
    for i, r in enumerate(rows):
        y = top + i * rowh + 26
        body.append(line(x_lab, y - 26, W - 24, y - 26, "grid"))
        body.append(t(x_lab, y + 5, r, "ink", 15))
        for j in range(2):
            up = on[i] if j == 0 else not on[i]
            cx = xs[j]
            if up:
                tri = f"M{cx - 52},{y + 6} L{cx - 44},{y - 8} L{cx - 36},{y + 6} Z"
                body.append(f'<path d="{tri}" class="s1"/>')
                body.append(t(cx - 28, y + 5, "compra-se", "ink", 14))
            else:
                tri = f"M{cx - 52},{y - 6} L{cx - 44},{y + 8} L{cx - 36},{y - 6} Z"
                body.append(f'<path d="{tri}" class="s2"/>')
                body.append(t(cx - 28, y + 5, "vende-se", "ink", 14))
    body.append(line(x_lab, top + 4 * rowh, W - 24, top + 4 * rowh, "grid"))
    frame("fig03-risk-on-risk-off.svg", 360,
          "Os dois modos do mercado depois da crise",
          "O que os investidores compram e vendem conforme o tom das notícias",
          "▲ compra (o preço tende a subir)   ▼ venda (o preço tende a cair)", body,
          "Risk-on: compram-se ações e commodities, vendem-se dólar e títulos. Risk-off: o inverso.")


# ---------------------------------------------------------------- Fig. 4
def fig_populacao_producao():
    data = [("População", "hoje", 20), ("Produção", "hoje", 50), ("Produção", "fim do século (projeção)", 25)]
    x0, x1, top, rowh, bh = 24, 576, 150, 74, 24
    body = [swatch(24, 106, "s1"), t(42, 106, "Países desenvolvidos", "ink", 14),
            swatch(220, 106, "s2"), t(238, 106, "Países em desenvolvimento", "ink", 14)]
    for i, (lab, sub, dev) in enumerate(data):
        y = top + i * rowh
        body.append(t(x0, y - 8, lab, "ink", 15, weight=600))
        body.append(t(x0 + len(lab) * 9 + 8, y - 8, sub, "mut", 13))
        xm = x0 + (x1 - x0) * dev / 100
        body.append(hbar(x0, xm - 1, y, bh, "s1", round_end=False))
        body.append(hbar(xm + 1, x1, y, bh, "s2"))
        body.append(t(x0 + 8, y + 17, f"{dev}%", "onfill", 14, weight=600))
        body.append(t(x1 - 8, y + 17, f"{100 - dev}%", "onfill", 14, "end", 600))
    frame("fig04-populacao-e-producao.svg", 370,
          "Quem vive e quem produz no mundo",
          "Participação na população e na produção mundial",
          "Fonte: números citados por Siegel no capítulo 4.", body,
          "População hoje: 20% em países desenvolvidos. Produção hoje: 50%. Produção projetada para o fim do século: 25%.")


# ---------------------------------------------------------------- Fig. 5
def fig_subperiodos():
    data = [("1802–1870", 6.7), ("1871–1925", 6.6), ("1926–2012", 6.4)]
    left, right, base, ytop = 64, 560, 330, 110

    def Y(v):
        return base - v / 8 * (base - ytop)

    body = []
    for v in (0, 2, 4, 6, 8):
        body.append(line(left, Y(v), right, Y(v), "grid" if v else "axis"))
        body.append(t(left - 10, Y(v) + 4, f"{v}%", "mut", 13, "end"))
    band = (right - left) / len(data)
    for i, (lab, v) in enumerate(data):
        cx = left + band * (i + 0.5)
        body.append(col(cx - 12, 24, Y(0), Y(v), "s1"))
        body.append(t(cx, Y(v) - 10, br(v) + "%", "ink", 15, "middle", 600))
        body.append(t(cx, base + 22, lab, "ink2", 14, "middle"))
    frame("fig05-retorno-por-periodo.svg", 430,
          "Retorno real das ações americanas, por período",
          "Média anual acima da inflação. Média de todo o período: cerca de 6,6%",
          "Fonte: Siegel, cap. 5. Os três períodos atravessam guerras, crises e a troca do\nouro pelo papel-moeda, e mesmo assim o retorno real quase não muda.", body,
          "1802–1870: 6,7%; 1871–1925: 6,6%; 1926–2012: 6,4%.")


# ---------------------------------------------------------------- Fig. 6
GS10 = {1981: 13.91, 1982: 13.00, 1983: 11.10, 1984: 12.44, 1985: 10.62, 1986: 7.68, 1987: 8.39,
        1988: 8.85, 1989: 8.49, 1990: 8.55, 1991: 7.86, 1992: 7.01, 1993: 5.87, 1994: 7.09,
        1995: 6.57, 1996: 6.44, 1997: 6.35, 1998: 5.26, 1999: 5.65, 2000: 6.03, 2001: 5.02,
        2002: 4.61, 2003: 4.01, 2004: 4.27, 2005: 4.29, 2006: 4.80, 2007: 4.63, 2008: 3.66,
        2009: 3.26, 2010: 3.22, 2011: 2.78, 2012: 1.80}


def fig_juros_10_anos():
    left, right, base, ytop = 56, 548, 330, 100

    def X(yr):
        return left + (yr - 1981) / (2012 - 1981) * (right - left)

    def Y(v):
        return base - v / 16 * (base - ytop)

    body = []
    for v in (0, 4, 8, 12, 16):
        body.append(line(left, Y(v), right, Y(v), "grid" if v else "axis"))
        body.append(t(left - 10, Y(v) + 4, f"{v}%", "mut", 13, "end"))
    for yr in (1981, 1990, 2000, 2012):
        body.append(t(X(yr), base + 22, str(yr), "mut", 13, "middle"))
    pts = [(X(y), Y(v)) for y, v in sorted(GS10.items())]
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    area = f"M{pts[0][0]:.1f},{Y(0):.1f} L" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f" L{pts[-1][0]:.1f},{Y(0):.1f} Z"
    body.append(f'<path d="{area}" class="s1w"/>')
    body.append(f'<polyline points="{poly}" fill="none" class="s1s" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
    for (x, y), v, anchor, dx in ((pts[0], GS10[1981], "start", 12), (pts[-1], GS10[2012], "end", -12)):
        body.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" class="s1 ring" stroke-width="2"/>')
        body.append(t(x + dx, y - 10, br(v) + "%", "ink", 15, anchor, 600))
    frame("fig07-juros-10-anos.svg", 420,
          "Juros do título de 10 anos do Tesouro americano",
          "Média anual, 1981–2012",
          "Médias anuais aproximadas (Federal Reserve, série GS10). No pior dia de 1981, os juros\nchegaram a cerca de 15,8%; no melhor de 2012, a cerca de 1,4%.", body,
          "Os juros caem de 13,9% em 1981 para 1,8% em 2012, com oscilações.")


# ---------------------------------------------------------------- Fig. 7
def preco_titulo(cupom, juros, anos=30):
    j = juros / 100
    return sum(cupom / (1 + j) ** k for k in range(1, anos + 1)) + 100 / (1 + j) ** anos


def fig_gangorra():
    left, right, base, ytop = 64, 556, 330, 104
    jmax, jmin = 14, 2

    def X(j):
        return left + (jmax - j) / (jmax - jmin) * (right - left)

    def Y(p):
        return base - p / 400 * (base - ytop)

    body = []
    for p in (0, 100, 200, 300, 400):
        body.append(line(left, Y(p), right, Y(p), "grid" if p else "axis"))
        body.append(t(left - 10, Y(p) + 4, str(p), "mut", 13, "end"))
    for j in (14, 11, 8, 5, 2):
        body.append(t(X(j), base + 22, f"{j}%", "mut", 13, "middle"))
    body.append(t((left + right) / 2, base + 44, "Juros de mercado, caindo da esquerda para a direita", "ink2", 13, "middle"))
    js = [jmax - k * 0.25 for k in range(int((jmax - jmin) / 0.25) + 1)]
    pts = [(X(j), Y(preco_titulo(14, j))) for j in js]
    body.append('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
                + '" fill="none" class="s1s" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
    for j, anchor, dx, dy in ((14, "start", 10, 24), (8, "end", -10, -12), (2, "end", -10, -12)):
        p = preco_titulo(14, j)
        body.append(f'<circle cx="{X(j):.1f}" cy="{Y(p):.1f}" r="5" class="s1 ring" stroke-width="2"/>')
        body.append(t(X(j) + dx, Y(p) + dy, f"{br(p, 0)} com juros de {j}%", "ink", 14, anchor, 600))
    frame("fig06-gangorra-juros-preco.svg", 420,
          "A gangorra: juros caem, preço do título sobe",
          "Preço de um título de 30 anos que paga 14% ao ano, comprado por 100",
          "Cálculo ilustrativo (valor presente dos pagamentos), supondo 30 anos de prazo restante.", body,
          "O preço vai de 100, com juros de 14%, para cerca de 168 com juros de 8% e 369 com juros de 2%.")


# ---------------------------------------------------------------- Fig. 8
PIOR = [  # horizonte, ações, títulos, letras (retorno real anualizado, %)
    (1, -38.6, -21.9, -15.6), (2, -31.6, -15.9, -15.1), (5, -11.0, -10.1, -8.0),
    (10, -4.1, -5.4, -5.1), (20, 1.0, -3.1, -3.0), (30, 2.6, -2.0, -1.8)]


def fig_pior_retorno():
    left, right, ytop, ybot = 64, 572, 128, 362
    vmax, vmin = 5, -45

    def Y(v):
        return ytop + (vmax - v) / (vmax - vmin) * (ybot - ytop)

    body = [swatch(24, 104, "s1"), t(42, 104, "Ações", "ink", 14),
            swatch(110, 104, "s2"), t(128, 104, "Títulos", "ink", 14),
            swatch(204, 104, "s3"), t(222, 104, "Letras", "ink", 14)]
    for v in (0, -10, -20, -30, -40):
        body.append(line(left, Y(v), right, Y(v), "axis" if v == 0 else "grid"))
        body.append(t(left - 10, Y(v) + 4, f"{v}%".replace("-", "−"), "mut", 13, "end"))
    band = (right - left) / len(PIOR)
    bw, gap = 20, 2
    for i, (h, a, b, c) in enumerate(PIOR):
        cx = left + band * (i + 0.5)
        xs = [cx - bw * 1.5 - gap, cx - bw / 2, cx + bw / 2 + gap]
        for x, v, cls in zip(xs, (a, b, c), ("s1", "s2", "s3")):
            body.append(col(x, bw, Y(0), Y(v), cls))
        lab = ("+" if a > 0 else "") + br(a) + "%"
        ya = Y(a) - 8 if a > 0 else Y(a) + 18
        body.append(t(xs[0] + bw / 2, ya, lab.replace("-", "−"), "ink", 13, "middle", 600))
        body.append(t(cx, ybot + 24, f"{h} ano" + ("s" if h > 1 else ""), "ink2", 14, "middle"))
    frame("fig08-pior-retorno-por-horizonte.svg", 456,
          "O pior resultado já registrado, conforme o prazo",
          "Pior retorno real anualizado de cada classe de ativos, 1802–2012",
          "Valores aproximados da tabela de Siegel (cap. 6); rótulos indicam as ações.\nA tabela completa está no texto.", body,
          "Em 1 ano o pior das ações é −38,6%, contra −21,9% dos títulos e −15,6% das letras. "
          "Em 10 anos as ações já perdem menos. Em 20 e 30 anos o pior das ações é positivo (+1,0% e +2,6%).")


# ---------------------------------------------------------------- Fig. 9
def fig_raiz_quadrada():
    left, right, base, ytop = 64, 560, 340, 104

    def X(T):
        return left + (T - 1) / 29 * (right - left)

    def Y(p):
        return base - p / 100 * (base - ytop)

    body = []
    Ts = [1 + k * 0.25 for k in range(117)]
    curve = [(X(T), Y(100 / math.sqrt(T))) for T in Ts]
    above = f"M{X(1):.1f},{Y(100):.1f} L" + " L".join(f"{x:.1f},{y:.1f}" for x, y in curve) + f" L{X(30):.1f},{Y(100):.1f} Z"
    below = f"M{X(1):.1f},{Y(0):.1f} L" + " L".join(f"{x:.1f},{y:.1f}" for x, y in curve) + f" L{X(30):.1f},{Y(0):.1f} Z"
    body.append(f'<path d="{above}" class="s2w"/>')
    body.append(f'<path d="{below}" class="s1w"/>')
    for p in (0, 25, 50, 75, 100):
        body.append(line(left, Y(p), right, Y(p), "grid" if p else "axis"))
        body.append(t(left - 10, Y(p) + 4, f"{p}%", "mut", 13, "end"))
    for T in (1, 5, 10, 15, 20, 25, 30):
        body.append(t(X(T), base + 22, str(T), "mut", 13, "middle"))
    body.append(t((left + right) / 2, base + 44, "Horizonte do investimento, em anos", "ink2", 13, "middle"))
    body.append('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in curve)
                + '" fill="none" class="ref" stroke-width="2" stroke-linejoin="round"/>')
    for T, lab, anchor, dx in ((4, "4 anos: metade", "start", 10), (25, "25 anos: um quinto", "end", -10)):
        x, y = X(T), Y(100 / math.sqrt(T))
        body.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" class="ink ring" stroke-width="2"/>')
        body.append(t(x + dx, y - 10, lab, "ink", 14, anchor, 600))
    body.append(t(X(14), Y(78), "Títulos: o risco cai mais devagar", "ink", 14, weight=600))
    body.append(t(X(14), Y(78) + 18, "(aversão à média)", "ink2", 13))
    body.append(t(X(8), Y(8), "Ações: o risco cai mais depressa (reversão à média)", "ink", 14, weight=600))
    frame("fig09-raiz-quadrada-do-tempo.svg", 430,
          "A régua do passeio aleatório",
          "Risco do retorno médio anual, em proporção ao risco de 1 ano, se os retornos\nfossem um passeio aleatório (a curva cai na proporção de 1 ÷ √T)",
          "As áreas indicam só a direção do desvio observado por Siegel, não valores medidos.", body,
          "A curva parte de 100% em 1 ano e cai para 50% em 4 anos e 20% em 25 anos. Ações ficam abaixo dela, títulos acima.")


# ---------------------------------------------------------------- Fig. 10
def fig_correlacao_eras():
    rows = [("1926–1965", "levemente positiva", 1926, 1965, "posl"),
            ("Grande Depressão", "negativa", 1929, 1939, "neg"),
            ("1960–1990", "positiva", 1960, 1990, "pos"),
            ("Depois de 1998", "negativa", 1998, 2012, "neg")]
    left, right, top, rowh, bh = 24, 576, 158, 52, 20
    y0, y1 = 1920, 2015

    def X(yr):
        return left + (yr - y0) / (y1 - y0) * (right - left)

    body = [swatch(24, 100, "neg"), t(42, 100, "Negativa: os títulos protegem quando as ações caem", "ink", 14),
            swatch(24, 122, "pos"), t(42, 122, "Positiva: ações e títulos caem juntos", "ink", 14)]
    ybot = top + rowh * len(rows) - 18
    for yr in (1920, 1940, 1960, 1980, 2000):
        body.append(line(X(yr), top - 8, X(yr), ybot, "grid"))
        body.append(t(X(yr), ybot + 20, str(yr), "mut", 13, "middle"))
    for i, (lab, sinal, a, b, cls) in enumerate(rows):
        y = top + i * rowh
        body.append(hbar(X(a), X(b), y + 6, bh, cls))
        tx = X(b) + 10
        anchor = "start"
        if tx > right - 150:
            tx, anchor = X(a) - 10, "end"
        body.append(t(tx, y + 15, lab, "ink", 14, anchor, 600))
        body.append(t(tx, y + 31, sinal, "ink2", 13, anchor))
    frame("fig10-correlacao-acoes-titulos.svg", 440,
          "Os títulos nem sempre protegem as ações",
          "Sinal da correlação entre os retornos de ações e de títulos do governo",
          "Classificação qualitativa, conforme o capítulo 6. A Grande Depressão aparece em linha própria\n(o livro não delimita as datas; usamos a década de 1930 como referência).", body,
          "1926–1965: levemente positiva; Grande Depressão: negativa; 1960–1990: positiva; depois de 1998: negativa.")


# ---------------------------------------------------------------- Fig. 11
def fig_carteira_risco_minimo():
    data = [("1 ano", 0, "quase nada"), ("2 anos", 0, "quase nada"), ("5 anos", 25, "cerca de 25%"),
            ("10 anos", 33.3, "mais de 1/3"), ("20 anos", 50, "mais de 50%"), ("30 anos", 60, "mais de 60%")]
    x0, x1, top, rowh, bh = 96, 576, 124, 40, 22
    body = [swatch(24, 100, "s1"), t(42, 100, "Ações", "ink", 14),
            swatch(110, 100, "gray"), t(128, 100, "Renda fixa", "ink", 14)]
    for i, (lab, pct, txt) in enumerate(data):
        y = top + i * rowh
        body.append(t(x0 - 12, y + 16, lab, "ink", 14, "end"))
        xm = x0 + (x1 - x0) * pct / 100
        if pct > 0:
            body.append(hbar(x0, xm - 1, y, bh, "s1", round_end=False))
            body.append(hbar(xm + 1, x1, y, bh, "gray"))
            body.append(t(x0 + 8, y + 16, txt, "onfill", 13, weight=600))
        else:
            body.append(hbar(x0, x1, y, bh, "gray"))
            body.append(t(x0 + 8, y + 16, "ações: " + txt, "ink", 13, weight=600))
    frame("fig11-carteira-de-risco-minimo.svg", 420,
          "A carteira de menor risco muda com o prazo",
          "Parcela em ações na carteira que minimiza o risco, por horizonte",
          "Fonte: Siegel, cap. 6. As parcelas de 10, 20 e 30 anos são os mínimos citados no livro\n(\"mais de\"); as barras foram desenhadas nesses mínimos.", body,
          "1 e 2 anos: quase nada em ações; 5 anos: 25%; 10 anos: mais de um terço; 20 anos: mais de metade; 30 anos: mais de 60%.")


# ---------------------------------------------------------------- Fig. 12
def fig_ponderacao():
    pa_preco = 200 / 220 * 100
    pa_valor = 2 / 202 * 100
    data = [("Ponderado pelo preço (como o Dow Jones)", pa_preco),
            ("Ponderado pelo valor de mercado (como o S&P 500)", pa_valor)]
    x0, x1, top, rowh, bh = 24, 576, 178, 76, 24
    body = [swatch(24, 106, "s1"), t(42, 106, "Empresa A: ação de US$ 200, empresa pequena (vale US$ 2 bilhões)", "ink", 14),
            swatch(24, 130, "s2"), t(42, 130, "Empresa B: ação de US$ 20, empresa gigante (vale US$ 200 bilhões)", "ink", 14)]
    for i, (lab, pa) in enumerate(data):
        y = top + i * rowh
        body.append(t(x0, y - 10, lab, "ink", 15, weight=600))
        xm = x0 + (x1 - x0) * pa / 100
        body.append(hbar(x0, xm - 1, y, bh, "s1", round_end=False))
        body.append(hbar(xm + 1, x1, y, bh, "s2"))
        la, lb = f"A: {br(pa, 0)}%", f"B: {br(100 - pa, 0)}%"
        if xm - x0 > 70:
            body.append(t(x0 + 8, y + 17, la, "onfill", 14, weight=600))
        else:
            body.append(t(x0, y + bh + 18, la, "ink", 13, weight=600))
        if x1 - xm > 70:
            body.append(t(x1 - 8, y + 17, lb, "onfill", 14, "end", 600))
        else:
            body.append(t(x1, y + bh + 18, lb, "ink", 13, "end", 600))
    frame("fig12-ponderacao-preco-valor.svg", 360,
          "O peso de cada empresa no índice",
          "Exemplo com duas empresas",
          "Exemplo ilustrativo. A tem 10 milhões de ações; B tem 10 bilhões.", body,
          "Ponderado pelo preço, A pesa 91% e B 9%. Ponderado pelo valor de mercado, A pesa 1% e B 99%.")


for fn in (fig_dolar_1802, fig_alavancagem, fig_risk_on_off, fig_populacao_producao, fig_subperiodos,
           fig_juros_10_anos, fig_gangorra, fig_pior_retorno, fig_raiz_quadrada, fig_correlacao_eras,
           fig_carteira_risco_minimo, fig_ponderacao):
    fn()
print("ok", sorted(os.listdir(OUT)))
print("preço 8%:", round(preco_titulo(14, 8), 1), " 2%:", round(preco_titulo(14, 2), 1))
