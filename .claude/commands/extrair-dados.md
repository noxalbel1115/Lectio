# Extração Estruturada de Dados do Processo

Extraia TODOS os dados do processo de forma estruturada e referenciada. Cada informação deve ter indicação de página/documento de origem.

$ARGUMENTS

---

## Protocolo de Extração

### PASSO 1 — Leitura Integral
Leia TODO o documento fornecido, página por página, sem pular nenhuma seção.

### PASSO 2 — Extração por Categorias

Execute cada categoria abaixo. Se uma informação não for encontrada, indique explicitamente "NÃO LOCALIZADO NOS AUTOS FORNECIDOS".

---

### A. DADOS DE IDENTIFICAÇÃO

```
IDENTIFICAÇÃO DO PROCESSO
=========================
Número:           [                    ] — [ref: p. __]
Classe:           [                    ] — [ref: p. __]
Assunto(s):       [                    ] — [ref: p. __]
Vara/Juízo:       [                    ] — [ref: p. __]
Comarca/Seção:    [                    ] — [ref: p. __]
Distribuição:     [data]                 — [ref: p. __]
Valor da causa:   [R$                  ] — [ref: p. __]
Justiça gratuita: [Sim/Não/Requerida]   — [ref: p. __]
Prioridade:       [tipo ou N/A]          — [ref: p. __]
Segredo/sigilo:   [Sim/Não]              — [ref: p. __]
```

### B. PARTES E PROCURADORES

Para CADA parte, extraia:
```
PARTE [Nº] — [POLO ATIVO/PASSIVO/TERCEIRO]
Nome completo:      [                    ] — [ref: p. __]
CPF/CNPJ:           [                    ] — [ref: p. __]
Endereço:           [                    ] — [ref: p. __]
Qualificação:       [profissão, estado civil, etc.]
Advogado(s):        [nome] — OAB [UF] nº [número]
Procuração:         [página]
```

### C. CRONOLOGIA PROCESSUAL

Extraia TODOS os atos processuais em ordem cronológica:
```
| Data       | Ato Processual              | Parte/Juízo | Página |
|------------|-----------------------------|-------------|--------|
| DD/MM/AAAA | [descrição do ato]          | [quem]      | p. XX  |
```

### D. PEDIDOS — EXTRAÇÃO INTEGRAL

Para cada pedido formulado por qualquer das partes:
```
PEDIDO Nº [X] — [Autor/Réu]
================================================
Tipo:              [Condenatório/Constitutivo/Declaratório/Mandamental/Executivo]
Descrição:         [transcrição ou resumo fiel do pedido]
Valor:             [se quantificado]
Base legal:        [dispositivos legais invocados]
Base fática:       [fatos alegados como fundamento]
Página(s):         [referência precisa]
Antecipação tutela: [sim/não — se sim, fundamento]
```

### E. DOCUMENTOS JUNTADOS

Liste TODOS os documentos anexados ao processo:
```
| # | Documento | Juntado por | Data | Páginas | Conteúdo Resumido |
|---|-----------|-------------|------|---------|-------------------|
```

### F. PROVAS PRODUZIDAS OU REQUERIDAS

```
PROVAS DOCUMENTAIS:
- [lista com referência de páginas]

PROVAS TESTEMUNHAIS:
- [testemunhas arroladas por cada parte]
- [depoimentos já realizados — resumo]

PROVA PERICIAL:
- [tipo de perícia / perito nomeado / quesitos / laudo]

DEPOIMENTO PESSOAL:
- [se houve — resumo]

INSPEÇÃO JUDICIAL:
- [se houve — conclusões]
```

### G. DECISÕES INTERLOCUTÓRIAS

Para cada decisão proferida no curso do processo:
```
DECISÃO DE [data] — p. [XX]
Conteúdo: [resumo]
Recursos: [se houve agravo/recurso — resultado]
```

### H. VALORES E CÁLCULOS

```
Valor da causa:              R$ [          ]
Custas pagas:                R$ [          ]
Honorários periciais:        R$ [          ]
Valores discutidos:          R$ [          ]
Cálculos apresentados:       [por quem, página, metodologia]
Impugnações aos cálculos:    [se houve]
```

---

## PASSO 3 — Controle de Qualidade

Após a extração, realize:

1. **Verificação de completude**: Todos os campos foram preenchidos ou marcados como "NÃO LOCALIZADO"?
2. **Verificação de consistência**: Há dados contraditórios entre documentos diferentes?
3. **Lacunas identificadas**: Que informações importantes estão ausentes dos autos?

```
RELATÓRIO DE QUALIDADE DA EXTRAÇÃO
====================================
Campos preenchidos:    [X de Y]  ([%])
Campos não localizados: [lista]
Contradições encontradas: [lista]
Documentos referenciados mas ausentes: [lista]
```
