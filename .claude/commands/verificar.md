# Verificação Cruzada e Checagem de Consistência

Execute uma verificação rigorosa da análise já realizada, buscando inconsistências, erros, lacunas e pontos que demandam revisão.

$ARGUMENTS

---

## Protocolo de Verificação

### CHECK 1 — Consistência Interna

Verifique se a análise apresenta contradições internas:

```
VERIFICAÇÃO DE CONSISTÊNCIA INTERNA
=====================================

| # | Item Verificado | Resultado | Observação |
|---|----------------|-----------|------------|
| 1 | Fatos narrados são coerentes entre si? | ✅/❌ | [detalhe] |
| 2 | Datas e cronologia são consistentes? | ✅/❌ | [detalhe] |
| 3 | Valores mencionados batem entre si? | ✅/❌ | [detalhe] |
| 4 | Nomes das partes estão corretos em toda análise? | ✅/❌ | [detalhe] |
| 5 | Conclusões são coerentes com a fundamentação? | ✅/❌ | [detalhe] |
| 6 | Análise probatória condiz com a recomendação? | ✅/❌ | [detalhe] |
```

### CHECK 2 — Completude

Verifique se todos os elementos necessários foram abordados:

```
VERIFICAÇÃO DE COMPLETUDE
===========================

PEDIDOS:
| Pedido | Analisado? | Prova examinada? | Conclusão? |
|--------|-----------|-----------------|------------|
| [pedido 1] | ✅/❌ | ✅/❌ | ✅/❌ |
| [pedido 2] | ✅/❌ | ✅/❌ | ✅/❌ |

PRELIMINARES:
| Preliminar | Analisada? | Conclusão? |
|-----------|-----------|------------|
| [prelim. 1] | ✅/❌ | ✅/❌ |

ARGUMENTOS DAS PARTES:
| Argumento | Enfrentado? | Ref. art. 489, §1º, IV? |
|-----------|-----------|-------------------------|
| [arg. autor 1] | ✅/❌ | [se não, por quê] |
| [arg. réu 1] | ✅/❌ | [se não, por quê] |

PROVAS:
| Prova | Analisada? | Valorada? |
|-------|-----------|-----------|
| [prova 1] | ✅/❌ | ✅/❌ |
```

### CHECK 3 — Referências aos Autos

Verifique se todas as afirmações factuais têm referência:

```
VERIFICAÇÃO DE REFERÊNCIAS
============================

Afirmações SEM referência aos autos:
1. "[afirmação]" — ⚠️ PRECISA DE REFERÊNCIA
2. "[afirmação]" — ⚠️ PRECISA DE REFERÊNCIA

Referências que não puderam ser verificadas:
1. "p. XX" — [motivo]
```

### CHECK 4 — Correção Jurídica

Verifique a correção do enquadramento jurídico:

```
VERIFICAÇÃO JURÍDICA
=====================

| Item | Status | Observação |
|------|--------|------------|
| Legislação citada está vigente? | ✅/❌/⚠️ | [detalhe] |
| Dispositivos citados estão corretos? | ✅/❌/⚠️ | [detalhe] |
| Jurisprudência é pertinente ao caso? | ✅/❌/⚠️ | [detalhe] |
| Há jurisprudência contrária não citada? | ✅/❌/⚠️ | [detalhe] |
| Ônus da prova foi corretamente distribuído? | ✅/❌/⚠️ | [detalhe] |
| Prescrição/decadência foi verificada? | ✅/❌/⚠️ | [detalhe] |
```

### CHECK 5 — Riscos Processuais

Identifique riscos de nulidade ou reforma:

```
ANÁLISE DE RISCOS
==================

RISCO DE NULIDADE:
| Possível Nulidade | Probabilidade | Impacto |
|-------------------|--------------|---------|
| [descrição] | [Alta/Média/Baixa] | [Grave/Moderado/Leve] |

RISCO DE REFORMA EM GRAU RECURSAL:
| Ponto Vulnerável | Probabilidade de Reforma | Fundamento |
|-----------------|-------------------------|------------|
| [descrição] | [Alta/Média/Baixa] | [por quê] |

CERCEAMENTO DE DEFESA:
- [ ] Todas as provas requeridas foram produzidas ou indeferidas fundamentadamente?
- [ ] As partes tiveram oportunidade de se manifestar sobre todos os documentos?
- [ ] Houve audiência quando necessária?
```

### CHECK 6 — Alucinações

Verifique especificamente se há informações que podem ter sido inventadas:

```
VERIFICAÇÃO ANTI-ALUCINAÇÃO
=============================

Para cada afirmação factual relevante:
| Afirmação | Está nos autos? | Confiança |
|-----------|----------------|-----------|
| [afirmação 1] | ✅ Confirmado p.XX / ❌ Não encontrado / ⚠️ Incerto | [Alta/Média/Baixa] |
| [afirmação 2] | ... | ... |

JURISPRUDÊNCIA CITADA — NECESSITA VERIFICAÇÃO:
| Julgado | Verificável? | Ação Necessária |
|---------|-------------|-----------------|
| [citação 1] | [Sim/Não/Parcial] | [CONFIRMAR em repositório oficial] |
```

### SÍNTESE DA VERIFICAÇÃO

```
╔═══════════════════════════════════════════════════╗
║         RESULTADO DA VERIFICAÇÃO                 ║
╠═══════════════════════════════════════════════════╣
║                                                   ║
║ Consistência Interna:  [✅ OK / ⚠️ Atenção / ❌]  ║
║ Completude:            [✅ OK / ⚠️ Atenção / ❌]  ║
║ Referências:           [✅ OK / ⚠️ Atenção / ❌]  ║
║ Correção Jurídica:     [✅ OK / ⚠️ Atenção / ❌]  ║
║ Riscos Processuais:    [✅ OK / ⚠️ Atenção / ❌]  ║
║ Anti-Alucinação:       [✅ OK / ⚠️ Atenção / ❌]  ║
║                                                   ║
║ RESULTADO GERAL: [APROVADO / APROVADO COM         ║
║                   RESSALVAS / REVISÃO NECESSÁRIA] ║
║                                                   ║
║ ITENS QUE DEMANDAM CORREÇÃO:                      ║
║ 1. [item]                                         ║
║ 2. [item]                                         ║
║                                                   ║
║ ITENS QUE DEMANDAM ATENÇÃO DO MAGISTRADO:         ║
║ 1. [item]                                         ║
║ 2. [item]                                         ║
╚═══════════════════════════════════════════════════╝
```
