# Análise Completa de Processo Judicial

Você receberá um processo judicial (ou partes dele) para análise completa. Execute o pipeline integral abaixo com máxima precisão e confiabilidade.

## Instruções

Analise o(s) documento(s) fornecido(s) seguindo TODAS as etapas abaixo, em ordem. Para cada etapa, seja exaustivo e preciso.

$ARGUMENTS

---

## ETAPA 1 — MAPEAMENTO DO PROCESSO

Antes de qualquer análise, mapeie a estrutura completa do processo:

```
ÍNDICE DO PROCESSO
==================
| # | Documento | Páginas | Data | Parte |
|---|-----------|---------|------|-------|
| 1 | [tipo]    | [X-Y]  | [data] | [quem juntou] |
```

Identifique:
- Todos os documentos presentes nos autos
- Eventuais lacunas (documentos referenciados mas não encontrados)
- Ordem cronológica dos atos processuais

## ETAPA 2 — EXTRAÇÃO DE DADOS ESSENCIAIS

### 2.1 Identificação do Processo
- Número do processo
- Vara/Juízo
- Classe processual
- Assuntos (conforme tabelas do CNJ se possível)
- Valor da causa
- Data de distribuição
- Prioridades (idoso, deficiente, etc.)

### 2.2 Partes e Representação
```
PARTES
======
POLO ATIVO:
- Nome: [nome completo]
- Qualificação: [dados disponíveis]
- Advogado(s): [nome — OAB nº]

POLO PASSIVO:
- Nome: [nome completo]
- Qualificação: [dados disponíveis]
- Advogado(s): [nome — OAB nº]

TERCEIROS INTERVENIENTES:
- [se houver]

MINISTÉRIO PÚBLICO:
- [se intervém e por quê]
```

### 2.3 Pedidos (EXAUSTIVAMENTE)
Liste TODOS os pedidos formulados, numerando-os:
```
PEDIDOS DO AUTOR
================
P1: [descrição precisa do pedido] — [ref. página]
    Fundamento alegado: [base legal/fática]
    Valor específico: [se quantificado]
    
P2: [próximo pedido]
    ...

PEDIDOS DO RÉU (reconvenção/pedido contraposto)
================================================
[se houver]
```

## ETAPA 3 — ANÁLISE DAS TESES

### 3.1 Tese do Autor
Para CADA pedido, identifique:
- Causa de pedir remota (fatos)
- Causa de pedir próxima (fundamento jurídico)
- Argumentos de sustentação
- Provas indicadas pelo autor

### 3.2 Tese do Réu
Para CADA pedido contestado:
- Preliminares arguidas
- Prejudiciais de mérito
- Defesa de mérito (direta e indireta)
- Argumentos de sustentação
- Provas indicadas pelo réu

### 3.3 Pontos de Convergência e Divergência
```
QUADRO COMPARATIVO
==================
| Fato/Questão | Versão do Autor | Versão do Réu | Status |
|--------------|-----------------|---------------|--------|
| [fato 1]     | [versão]        | [versão]      | Controverso/Incontroverso |
```

## ETAPA 4 — QUESTÕES PRELIMINARES E PREJUDICIAIS

Analise e se manifeste sobre:

### 4.1 Pressupostos Processuais
- Capacidade de ser parte
- Capacidade processual
- Capacidade postulatória
- Competência (absoluta e relativa)
- Regularidade formal da petição inicial

### 4.2 Condições da Ação
- Legitimidade ad causam (ativa e passiva)
- Interesse de agir (necessidade, utilidade, adequação)

### 4.3 Preliminares da Contestação
Para cada preliminar arguida:
- Descrição da preliminar
- Fundamento legal
- Análise de procedência
- Consequência se acolhida

### 4.4 Prejudiciais de Mérito
- Prescrição
- Decadência
- Coisa julgada
- Litispendência
- Perempção

## ETAPA 5 — ANÁLISE PROBATÓRIA

Para CADA pedido, construa a MATRIZ PROBATÓRIA:

```
MATRIZ PROBATÓRIA — PEDIDO [Nº]
================================

FATO A PROVAR: [descrição]
ÔNUS DA PROVA: [quem tem — art. 373, CPC]

| Prova | Tipo | Favorece | Conteúdo Relevante | Confiabilidade | Ref. |
|-------|------|----------|--------------------|----------------|------|
| [doc] | Documental | Autor/Réu | [o que demonstra] | Alta/Média/Baixa | p.XX |

CONCLUSÃO PROBATÓRIA:
- Fato provado? [Sim/Não/Parcialmente]
- Grau de certeza: [✅/🟢/🟡/🟠/🔴]
- Fundamentação: [por que cheguei a essa conclusão]
```

## ETAPA 6 — ENQUADRAMENTO JURÍDICO

Para cada questão jurídica identificada:

### 6.1 Legislação Aplicável
- Dispositivos legais pertinentes (com texto quando relevante)
- Verificar vigência e eventuais alterações

### 6.2 Doutrina
- Correntes doutrinárias sobre o tema
- Posição majoritária
- `[CONHECIMENTO JURÍDICO EXTERNO — verificar atualidade]`

### 6.3 Jurisprudência
- Súmulas aplicáveis (STF, STJ, TST)
- Temas de repercussão geral / recursos repetitivos
- Jurisprudência do tribunal local
- `[VERIFICAR: citar números e datas exatas nos repositórios oficiais]`

## ETAPA 7 — SÍNTESE PARA DECISÃO

```
SÍNTESE EXECUTIVA
=================

PEDIDO P1: [descrição resumida]
├── Mérito: [Procedente/Improcedente/Parcialmente procedente]
├── Certeza: [grau]
├── Fundamento central: [resumo em 2-3 linhas]
└── Pontos de atenção: [riscos, divergências]

PEDIDO P2: [...]
...

QUESTÕES PENDENTES:
- [listar qualquer questão que não pôde ser resolvida com os autos fornecidos]

ALERTAS:
- [nulidades, prescrição, questões de ordem pública, etc.]
```

## ETAPA 8 — AUTODIAGNÓSTICO

Ao final, apresente:
```
AUTODIAGNÓSTICO DE CONFIABILIDADE
==================================
- Documentos analisados: [lista]
- Documentos referenciados mas não encontrados: [lista]
- Informações que não pude verificar: [lista]
- Pontos onde minha análise pode estar incompleta: [lista]
- Legislação que precisa verificação de vigência: [lista]
- Jurisprudência que precisa confirmação: [lista]
- Confiança geral na análise: [Alta/Média/Baixa com justificativa]
```
