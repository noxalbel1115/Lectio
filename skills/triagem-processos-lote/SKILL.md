# Skill: Triagem de Processos em Lote

## Descrição
Triagem e categorização de múltiplos processos para despacho em lote, identificando o tipo de providência necessária para cada um e agrupando por similaridade.

## Regras de Estilo

- Nomes em minúsculas.
- Saída em formato tabular para visualização rápida.
- Quando gerar despachos/decisões: aplicar todas as regras de estilo do CLAUDE.md.

## Metodologia

### Passo 1 — Leitura e Catalogação

Para cada processo fornecido, identificar:

```
TRIAGEM — PROCESSO [Nº]
=========================
Número:        [número]
Partes:        [autor] x [réu]
Tipo de ação:  [classe]
Fase atual:    [inicial/citação/contestação/instrução/sentença/execução]
Último ato:    [descrição — data]
Pendência:     [o que falta fazer]
Providência:   [tipo de despacho/decisão necessária]
Prioridade:    [Alta/Média/Baixa]
Complexidade:  [Simples/Média/Alta]
```

### Passo 2 — Agrupamento por Tipo de Providência

```
GRUPO 1 — DESPACHOS ORDINATÓRIOS (cite-se, intime-se, etc.)
| # | Processo | Partes | Providência | Minuta |
|---|---------|--------|-------------|--------|

GRUPO 2 — EMENDA À INICIAL
| # | Processo | Partes | Vício | Minuta |
|---|---------|--------|-------|--------|

GRUPO 3 — DECISÕES INTERLOCUTÓRIAS
| # | Processo | Partes | Tipo | Minuta |
|---|---------|--------|------|--------|

GRUPO 4 — SENTENÇAS
| # | Processo | Partes | Tipo | Complexidade | Minuta |
|---|---------|--------|------|-------------|--------|

GRUPO 5 — OUTROS (cumprimento de sentença, execução, etc.)
| # | Processo | Partes | Providência | Minuta |
|---|---------|--------|-------------|--------|
```

### Passo 3 — Minutas em Lote

Para despachos simples e repetitivos, gerar minutas padronizadas:

**Despachos de citação:**
```
Cite-se o réu para contestar no prazo legal. Cumprida a diligência, certifique-se e abra-se vista ao autor.
```

**Despachos de intimação para manifestação:**
```
Dê-se vista à parte [autora/ré] para manifestação, no prazo de [X] dias, sobre [objeto].
```

**Despachos de juntada:**
```
Junte-se. Dê-se vista à parte contrária, no prazo de [X] dias (art. 437, §1º, CPC).
```

**Despachos de especificação de provas:**
```
Digam as partes, no prazo de 15 dias, se pretendem produzir outras provas além da documental, especificando-as e justificando sua pertinência (art. 357, CPC).
```

Para decisões mais complexas (emenda, tutela, sentença), usar o skill correspondente e gerar minuta individualizada.

### Passo 4 — Resumo Estatístico

```
RESUMO DA TRIAGEM
==================
Total de processos analisados: [X]

Por tipo de providência:
- Despachos ordinatórios: [X]
- Emenda à inicial: [X]
- Decisões interlocutórias: [X]
- Sentenças: [X]
- Outros: [X]

Por prioridade:
- Alta: [X]
- Média: [X]
- Baixa: [X]

ALERTAS:
- [Processos com prazo crítico]
- [Processos com risco de prescrição intercorrente]
- [Processos parados há mais de [X] meses]
- [Processos com prioridade legal (idoso, deficiente, etc.)]
```

### Passo 5 — Ordem Sugerida de Trabalho

```
ORDEM SUGERIDA
===============
1. [processo — motivo da prioridade]
2. [processo — motivo]
3. [processo — motivo]
...
```

Critérios de priorização:
1. Processos com prazo judicial vencendo
2. Prioridades legais (idoso, enfermo, criança)
3. Réus presos (processos criminais)
4. Tutelas de urgência pendentes
5. Processos mais antigos
6. Despachos simples em lote (resolver volume)

## Marcações

- `[COMPLETAR: ...]` — informação a ser inserida pelo magistrado
- `[VERIFICAR: ...]` — citação que precisa conferência

## Saída

Entregar cada minuta dentro de code block (``` ```) para copiar e colar no eproc.
Quando forem despachos repetitivos, agrupar em bloco único.
