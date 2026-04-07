# Análise Probatória Detalhada

Realize uma análise probatória exaustiva do processo, examinando as provas relacionadas a CADA pedido e CADA fato controvertido.

$ARGUMENTS

---

## Metodologia

### FASE 1 — Identificação dos Fatos Controvertidos

Liste todos os fatos que são objeto de controvérsia entre as partes:

```
FATOS CONTROVERTIDOS
====================
FC1: [descrição do fato]
     Versão do Autor: [o que alega — ref. p. XX]
     Versão do Réu:   [o que alega — ref. p. XX]
     
FC2: [...]
```

### FASE 2 — Mapeamento do Ônus da Prova

Para cada fato controvertido, determine:

```
DISTRIBUIÇÃO DO ÔNUS DA PROVA
==============================
| Fato | Ônus (art. 373, CPC) | Inversão? | Fundamento |
|------|----------------------|-----------|------------|
| FC1  | Autor (I) / Réu (II) | Sim/Não  | [motivo]   |
```

Considere:
- Regra geral (art. 373, I e II, CPC)
- Inversão legal (ex: CDC, art. 6º, VIII)
- Inversão judicial (art. 373, §1º, CPC)
- Distribuição dinâmica do ônus da prova
- Teoria da carga dinâmica da prova

### FASE 3 — Análise Individual de Cada Prova

Para CADA prova existente nos autos:

```
PROVA [Nº]: [identificação]
===============================
Tipo:           [Documental/Testemunhal/Pericial/etc.]
Produzida por:  [parte]
Localização:    [páginas nos autos]
Admissibilidade: [lícita? pertinente? relevante?]

CONTEÚDO:
[Resumo fiel do conteúdo da prova]

FORÇA PROBANTE:
- O que esta prova demonstra: [análise]
- Limitações: [o que NÃO demonstra]
- Credibilidade: [Alta/Média/Baixa — justificativa]
- Corroborada por: [outras provas que confirmam]
- Contradita por: [provas em sentido contrário]

RELAÇÃO COM FATOS CONTROVERTIDOS:
- Relevante para: [FC1, FC3, etc.]
- Sentido: [favorável ao Autor/Réu]
```

### FASE 4 — Matriz Probatória por Pedido

Para CADA pedido formulado, construa:

```
═══════════════════════════════════════════════
PEDIDO [Nº]: [descrição]
═══════════════════════════════════════════════

FATOS CONSTITUTIVOS (ônus do Autor):
┌─────────────────────────────────────────────┐
│ Fato necessário: [descrição]                │
│ Provas favoráveis:                          │
│   ✓ [prova] — [o que demonstra] — p. XX     │
│   ✓ [prova] — [o que demonstra] — p. XX     │
│ Provas contrárias:                          │
│   ✗ [prova] — [o que contradiz] — p. XX     │
│ RESULTADO: Provado / Não provado / Parcial  │
│ CERTEZA: [✅/🟢/🟡/🟠/🔴]                    │
└─────────────────────────────────────────────┘

FATOS IMPEDITIVOS/MODIFICATIVOS/EXTINTIVOS (ônus do Réu):
┌─────────────────────────────────────────────┐
│ Fato alegado: [descrição]                   │
│ Provas favoráveis:                          │
│   ✓ [prova] — [o que demonstra] — p. XX     │
│ Provas contrárias:                          │
│   ✗ [prova] — [o que contradiz] — p. XX     │
│ RESULTADO: Provado / Não provado / Parcial  │
│ CERTEZA: [✅/🟢/🟡/🟠/🔴]                    │
└─────────────────────────────────────────────┘

CONCLUSÃO PROBATÓRIA PARA ESTE PEDIDO:
→ [Procedente / Improcedente / Parcialmente procedente]
→ Fundamento: [explicação]
→ Ressalvas: [se houver]
```

### FASE 5 — Análise de Credibilidade

Se houver prova testemunhal ou depoimento pessoal:

```
ANÁLISE DE CREDIBILIDADE
=========================
Testemunha/Depoente: [nome]
Arrolada por: [parte]
Relação com as partes: [se informada]

Coerência interna: [o depoimento é internamente consistente?]
Coerência externa: [condiz com as demais provas?]
Detalhamento: [o relato é vago ou preciso?]
Contradições: [com quem/o quê contradiz?]
Interesse no resultado: [há parcialidade aparente?]

Avaliação geral: [Altamente confiável / Confiável / Parcialmente confiável / Pouco confiável]
```

### FASE 6 — Síntese Probatória

```
╔═══════════════════════════════════════════════╗
║          SÍNTESE PROBATÓRIA GERAL            ║
╠═══════════════════════════════════════════════╣
║                                               ║
║ Pedido 1: [resultado] — Certeza: [grau]      ║
║ Pedido 2: [resultado] — Certeza: [grau]      ║
║ Pedido 3: [resultado] — Certeza: [grau]      ║
║                                               ║
║ PROVAS DECISIVAS:                             ║
║ → [prova que mais influencia o resultado]     ║
║                                               ║
║ LACUNAS PROBATÓRIAS:                          ║
║ → [fatos que ficaram sem prova adequada]      ║
║                                               ║
║ CONTRADIÇÕES NÃO RESOLVIDAS:                  ║
║ → [provas conflitantes que demandam atenção]  ║
╚═══════════════════════════════════════════════╝
```

## Regras de Confiabilidade para Análise Probatória

1. **NUNCA** invente conteúdo de provas — transcreva ou resuma fielmente
2. **SEMPRE** indique a página exata de cada prova referenciada
3. Quando uma prova for ambígua, apresente TODAS as interpretações possíveis
4. Se uma prova documental estiver ilegível ou incompleta, informe expressamente
5. Distingua entre **o que a prova DIZ** e **o que você CONCLUI** a partir dela
6. Para provas técnicas (perícia), reproduza as conclusões do perito antes de analisar
