# Análise Probatória com Matriz Pedido x Prova

Realize análise probatória exaustiva, examinando as provas relacionadas a CADA pedido e CADA fato controvertido.

$ARGUMENTS

---

## FASE 1 — Fatos controvertidos

```
FATOS CONTROVERTIDOS
=====================
FC1: [descricao]
     Versao do autor: [alegacao — ref.]
     Versao do reu:   [alegacao — ref.]

FC2: [...]
```

## FASE 2 — Onus da prova

```
| Fato | Onus (art. 373, CPC) | Inversao? | Fundamento |
|------|----------------------|-----------|------------|
| FC1  | Autor (I) / Reu (II) | Sim/Nao  | [motivo]   |
```

Considere: regra geral (art. 373, I e II), inversao legal (CDC, art. 6, VIII), inversao judicial (art. 373, par. 1), distribuicao dinamica.

## FASE 3 — Analise individual de cada prova

Para CADA prova nos autos:

```
PROVA [N]: [identificacao]
============================
Tipo:           [Documental/Testemunhal/Pericial/etc.]
Produzida por:  [parte]
Localizacao:    (ev. X, TIPO, p. Y)

CONTEUDO:
[Resumo fiel do conteudo]

O QUE DEMONSTRA: [analise]
O QUE NAO DEMONSTRA: [limitacoes]
CREDIBILIDADE: [Alta/Media/Baixa — justificativa]
CORROBORADA POR: [outras provas]
CONTRADITA POR: [provas em sentido contrario]
RELEVANTE PARA: [FC1, FC3, etc.]
SENTIDO: [favoravel ao autor/reu]
```

## FASE 4 — Matriz probatoria por pedido

Para CADA pedido:

```
PEDIDO [N]: [descricao]
========================

FATOS CONSTITUTIVOS (onus do autor):
  Fato: [descricao]
  Provas favoraveis:
    - [prova] — [o que demonstra] — (ev. X, p. Y)
  Provas contrarias:
    - [prova] — [o que contradiz] — (ev. X, p. Y)
  RESULTADO: [Provado / Nao provado / Parcial]

FATOS IMPEDITIVOS/MODIFICATIVOS/EXTINTIVOS (onus do reu):
  Fato: [descricao]
  Provas favoraveis:
    - [prova] — [o que demonstra] — (ev. X, p. Y)
  Provas contrarias:
    - [prova] — [o que contradiz] — (ev. X, p. Y)
  RESULTADO: [Provado / Nao provado / Parcial]

CONCLUSAO PROBATORIA: [Procedente / Improcedente / Parcial]
FUNDAMENTO: [explicacao]
```

## FASE 5 — Credibilidade (se houver prova oral)

```
ANALISE DE CREDIBILIDADE
==========================
Testemunha/Depoente: [nome]
Arrolada por: [parte]
Relacao com as partes: [se informada]
Coerencia interna: [consistente?]
Coerencia externa: [condiz com demais provas?]
Detalhamento: [vago ou preciso?]
Contradicoes: [com quem/o que?]
Interesse no resultado: [parcialidade?]
Avaliacao: [confiavel / parcialmente confiavel / pouco confiavel]
```

## FASE 6 — Sintese probatoria

```
SINTESE PROBATORIA
===================
Pedido 1: [resultado]
Pedido 2: [resultado]

PROVAS DECISIVAS:
- [prova que mais influencia o resultado]

LACUNAS PROBATORIAS:
- [fatos sem prova adequada]

CONTRADICOES NAO RESOLVIDAS:
- [provas conflitantes que demandam atencao]
```

## POSSIVEIS IMPRECISOES

```
| Afirmacao | Motivo da incerteza | Acao sugerida |
|-----------|--------------------|--------------| 
| [afirmacao] | [motivo] | [VERIFICAR: ...] |
```

---

## Regras

1. NUNCA invente conteudo de provas — resuma fielmente.
2. SEMPRE indique a localizacao exata de cada prova: (ev. X, TIPO, p. Y) ou (fls. X).
3. Quando uma prova for ambigua, apresente TODAS as interpretacoes possiveis.
4. Se prova documental estiver ilegivel ou incompleta, informe.
5. Distinga entre o que a prova DIZ e o que voce CONCLUI a partir dela.
6. Para provas tecnicas (pericia), reproduza as conclusoes do perito antes de analisar.
