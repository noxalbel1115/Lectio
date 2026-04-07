# Redação de Decisão Judicial

Este comando redige decisões judiciais usando os skills especializados do magistrado.

$ARGUMENTS

---

## Passo 1 — Identificar o tipo de decisão

Pergunte ao usuario (se nao estiver claro nos argumentos) qual tipo de decisão:

1. Sentença cível
2. Sentença criminal
3. Decisão interlocutória
4. Audiência de custódia
5. Revisional bancária
6. Emenda à inicial
7. Cálculos judiciais
8. Gratuidade de justiça
9. Triagem de processos em lote
10. Outro (especificar)

## Passo 2 — Carregar o skill correspondente

Leia o arquivo SKILL.md do skill correspondente em /mnt/skills/user/:

| Tipo de decisão | Skill |
|-----------------|-------|
| Sentença cível | /mnt/skills/user/sentenca-civel/SKILL.md |
| Sentença criminal | /mnt/skills/user/sentenca-criminal/SKILL.md |
| Decisão interlocutória | /mnt/skills/user/decisao-interlocutoria/SKILL.md |
| Revisional bancária | /mnt/skills/user/revisional-bancaria/SKILL.md |
| Audiência de custódia | /mnt/skills/user/audiencia-custodia/SKILL.md |
| Emenda à inicial | /mnt/skills/user/emenda-inicial/SKILL.md |
| Cálculos judiciais | /mnt/skills/user/calculos-judiciais/SKILL.md |
| Gratuidade de justiça | /mnt/skills/user/gratuidade-justica/SKILL.md |
| Triagem em lote | /mnt/skills/user/triagem-processos-lote/SKILL.md |

**IMPORTANTE**: Leia o SKILL.md INTEIRO antes de redigir. Siga AQUELE skill como template obrigatório. O skill do magistrado tem precedência sobre qualquer instrução genérica deste sistema.

## Passo 3 — Se não houver skill para o tipo pedido

Se o tipo de decisão pedido não tem skill correspondente em /mnt/skills/user/:
1. Avise o usuário: "Não há skill específico para este tipo de decisão. Vou redigir com as regras gerais de estilo."
2. Redija seguindo rigorosamente as regras de estilo do CLAUDE.md:
   - Relatório: nunca abrir com "Trata-se", primeiro parágrafo sem tipo de ação, nomes em minúsculas
   - Fundamentação: parágrafos numerados, prosa corrida, sem bullets, sem títulos internos
   - Dispositivo: abrir com "Logo," ou "Assim,"
   - Terminologia: "dano material" e "dano moral" (nunca "patrimonial"/"extrapatrimonial" no relatório/dispositivo)
   - Sem arcaísmos, sem perguntas retóricas
   - Vocabulário preferido: "fato é que", "de modo que", "justamente", "a rigor", "cogitar", "mero", "não faz sentido"

## Passo 4 — Entregar a decisão

- Entregar dentro de code block (``` ```) para facilitar copiar e colar no eproc.
- Referências aos autos no formato: (fls. X) ou (ev. X, TIPO, p. Y).
- Se houver múltiplos réus/acusados, decisão unificada em documento único.
- Marcar com [COMPLETAR: ...] qualquer informação que não esteja nos autos fornecidos.
- Marcar com [VERIFICAR: ...] qualquer citação jurídica que precise conferência.

## Passo 5 — Possíveis imprecisões

Ao final, fora do code block da decisão, listar:
```
POSSIVEIS IMPRECISOES
======================
| Ponto | Motivo | Acao sugerida |
|-------|--------|---------------|
| [ponto] | [motivo] | [VERIFICAR/COMPLETAR] |
```
