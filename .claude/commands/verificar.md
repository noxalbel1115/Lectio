# Verificação Cruzada e Checagem de Consistência

Execute verificação rigorosa da análise já realizada, buscando inconsistências, erros, lacunas e pontos que demandam revisão.

$ARGUMENTS

---

## CHECK 1 — Consistência Interna

```
CONSISTENCIA INTERNA
=====================
| # | Item | Resultado | Observacao |
|---|------|-----------|------------|
| 1 | Fatos narrados sao coerentes entre si? | OK/FALHA | [detalhe] |
| 2 | Datas e cronologia sao consistentes? | OK/FALHA | [detalhe] |
| 3 | Valores mencionados batem entre si? | OK/FALHA | [detalhe] |
| 4 | Nomes das partes estao corretos em toda analise? | OK/FALHA | [detalhe] |
| 5 | Conclusoes sao coerentes com a fundamentacao? | OK/FALHA | [detalhe] |
| 6 | Analise probatoria condiz com a recomendacao? | OK/FALHA | [detalhe] |
```

## CHECK 2 — Completude

```
PEDIDOS:
| Pedido | Analisado? | Prova examinada? | Conclusao? |
|--------|-----------|-----------------|------------|

PRELIMINARES:
| Preliminar | Analisada? | Conclusao? |
|-----------|-----------|------------|

ARGUMENTOS DAS PARTES (art. 489, par. 1, IV, CPC):
| Argumento | Enfrentado? | Se nao, por que? |
|-----------|-----------|------------------|

PROVAS:
| Prova | Analisada? | Valorada? |
|-------|-----------|-----------|
```

## CHECK 3 — Referencias aos Autos

```
Afirmacoes SEM referencia:
1. "[afirmacao]" — PRECISA DE REFERENCIA
2. "[afirmacao]" — PRECISA DE REFERENCIA

Referencias que nao puderam ser verificadas:
1. "[referencia]" — [motivo]
```

## CHECK 4 — Correcao Juridica

```
| Item | Status | Observacao |
|------|--------|------------|
| Legislacao citada esta vigente? | OK/FALHA/VERIFICAR | [detalhe] |
| Dispositivos citados estao corretos? | OK/FALHA/VERIFICAR | [detalhe] |
| Jurisprudencia e pertinente? | OK/FALHA/VERIFICAR | [detalhe] |
| Ha jurisprudencia contraria nao citada? | OK/FALHA/VERIFICAR | [detalhe] |
| Onus da prova corretamente distribuido? | OK/FALHA/VERIFICAR | [detalhe] |
| Prescricao/decadencia verificada? | OK/FALHA/VERIFICAR | [detalhe] |
```

## CHECK 5 — Riscos Processuais

```
RISCO DE NULIDADE:
| Possivel Nulidade | Probabilidade | Impacto |
|-------------------|--------------|---------|

RISCO DE REFORMA:
| Ponto Vulneravel | Probabilidade | Fundamento |
|-----------------|--------------|------------|

CERCEAMENTO DE DEFESA:
- Todas as provas requeridas foram produzidas ou indeferidas fundamentadamente?
- As partes se manifestaram sobre todos os documentos?
- Houve audiencia quando necessaria?
```

## CHECK 6 — Anti-Alucinacao

```
Para cada afirmacao factual relevante:
| Afirmacao | Esta nos autos? | Confianca |
|-----------|----------------|-----------|

JURISPRUDENCIA CITADA:
| Citacao | Verificavel? | Acao |
|---------|-------------|------|
```

## RESULTADO

```
Consistencia Interna:  [OK / ATENCAO / FALHA]
Completude:            [OK / ATENCAO / FALHA]
Referencias:           [OK / ATENCAO / FALHA]
Correcao Juridica:     [OK / ATENCAO / FALHA]
Riscos Processuais:    [OK / ATENCAO / FALHA]
Anti-Alucinacao:       [OK / ATENCAO / FALHA]

RESULTADO GERAL: [APROVADO / APROVADO COM RESSALVAS / REVISAO NECESSARIA]

ITENS QUE DEMANDAM CORRECAO:
1. [item]

ITENS QUE DEMANDAM ATENCAO DO MAGISTRADO:
1. [item]
```
