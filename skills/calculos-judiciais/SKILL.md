# Skill: Cálculos Judiciais

## Descrição
Auxílio na elaboração e conferência de cálculos judiciais: atualização monetária, juros de mora, honorários, custas e liquidação de sentença.

## Regras de Estilo

Quando a saída for uma decisão (homologação de cálculos, decisão sobre impugnação):
- NUNCA abrir com "Trata-se".
- Nomes em minúsculas.
- Parágrafos numerados, prosa corrida.
- Dispositivo abre com "Logo," ou "Assim,".

## Tipos de Cálculo

### 1. Atualização Monetária

**Índices mais comuns:**
- INPC: correção de benefícios previdenciários, verbas trabalhistas
- IPCA-E: correção de débitos judiciais da Fazenda Pública (após EC 113/2021: SELIC)
- IGP-M: contratos privados (quando pactuado)
- SELIC: débitos tributários, débitos da Fazenda Pública (EC 113/2021)

**Termos iniciais mais comuns:**
- Dano material: data do efetivo prejuízo (Súmula 43/STJ)
- Dano moral: data do arbitramento (Súmula 362/STJ)
- Verbas contratuais: data do vencimento
- Verbas previdenciárias: data de cada parcela vencida

### 2. Juros de Mora

**Percentuais:**
- Regra geral CC: 1% ao mês (art. 406, CC c/c art. 161, §1º, CTN) — ou SELIC, conforme entendimento adotado
- Fazenda Pública (EC 113/2021): SELIC (engloba correção + juros)
- Contratual: taxa pactuada, se lícita

**Termos iniciais:**
- Responsabilidade contratual: citação (art. 405, CC) ou vencimento da obrigação
- Responsabilidade extracontratual: evento danoso (Súmula 54/STJ)
- Relação de consumo extracontratual: evento danoso
- Fazenda Pública: citação

**ATENÇÃO:** Se usar SELIC como juros, NÃO cumular com índice de correção monetária separado (SELIC já embute correção + juros).

### 3. Honorários Advocatícios

**Regra geral (art. 85, §2º, CPC):** 10% a 20% sobre:
- Valor da condenação; ou
- Proveito econômico; ou
- Valor atualizado da causa

**Critérios para fixação do percentual (art. 85, §2º, I a IV):**
- Grau de zelo do profissional
- Lugar da prestação do serviço
- Natureza e importância da causa
- Trabalho realizado e tempo exigido

**Causas em que a Fazenda Pública for parte (art. 85, §3º):**
- Percentuais escalonados conforme valor da condenação/proveito
- Mínimo de 10% até 200 salários mínimos

**Valor inestimável ou irrisório (art. 85, §8º):**
- Fixação por apreciação equitativa (aplicação excepcional)
- [VERIFICAR: Tema 1076/STJ — limitou o uso do §8º]

**Sucumbência recíproca (art. 86, CPC):**
- Distribuição proporcional
- Vedada compensação (art. 85, §14)

### 4. Liquidação de Sentença

**Modalidades:**
- Por arbitramento (art. 509, I, CPC): quando a sentença determinar ou quando exigir conhecimento técnico
- Pelo procedimento comum (art. 509, II, CPC): quando houver necessidade de provar fato novo

**Memória de cálculo:**
- Principal (valor base)
- Correção monetária (índice + período)
- Juros de mora (taxa + período)
- Multa (se houver)
- Honorários
- Custas
- Deduções (valores já pagos, compensações)
- TOTAL

## Estrutura de Memória de Cálculo

```
MEMÓRIA DE CÁLCULO
===================

1. VALOR PRINCIPAL:                    R$ [X]
   Origem: [sentença/contrato/evento]
   Data-base: [data]

2. CORREÇÃO MONETÁRIA:
   Índice: [INPC/IPCA-E/SELIC]
   Período: [data inicial] a [data final]
   Fator acumulado: [X]
   Valor corrigido:                    R$ [X]

3. JUROS DE MORA:
   Taxa: [1% a.m. / SELIC]
   Período: [data inicial] a [data final]
   Valor dos juros:                    R$ [X]

4. SUBTOTAL (principal + correção + juros): R$ [X]

5. DEDUÇÕES:
   [valores já pagos, se houver]:      R$ [X]

6. HONORÁRIOS ADVOCATÍCIOS:
   Base: [condenação/causa]
   Percentual: [X]%
   Valor:                              R$ [X]

7. CUSTAS PROCESSUAIS:                 R$ [X]

TOTAL GERAL:                           R$ [X]
Data do cálculo: [data]
```

## Decisão sobre Impugnação aos Cálculos

```
[nome do impugnante em minúsculas] impugnou os cálculos apresentados por [nome], alegando [resumo da impugnação — ref.].

1. [Análise de cada ponto impugnado: índice de correção, termo inicial dos juros, base de cálculo, etc.]

2. [Se houver divergência: indicar qual cálculo está correto e por quê.]

3. [Se necessário: determinar nova conta.]

Logo, [acolho/rejeito/acolho parcialmente] a impugnação aos cálculos para [resultado]:

a) [providência específica];
b) [novo valor apurado, se for o caso]: R$ [X].

[Se acolhida parcialmente: determino a retificação da conta para adequar [ponto específico].]

Intimem-se.
```

## Marcações

- `[COMPLETAR: ...]` — informação a ser inserida pelo magistrado
- `[VERIFICAR: ...]` — citação que precisa conferência

## Saída

Entregar dentro de code block (``` ```) para copiar e colar no eproc.
