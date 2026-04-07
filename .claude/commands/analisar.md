# Análise Completa de Processo Judicial

Analise o(s) documento(s) fornecido(s) seguindo TODAS as etapas abaixo, em ordem. Entregue tudo em uma única resposta.

$ARGUMENTS

---

## ETAPA 1 — MAPA DOS AUTOS

Obrigatório. Primeira coisa a fazer. Liste todos os documentos/eventos do processo:

```
MAPA DOS AUTOS
===============
| Ev. | Tipo       | Data       | Parte/Origem | Páginas | Conteúdo resumido |
|-----|------------|------------|--------------|---------|-------------------|
| 1   | [tipo]     | [data]     | [quem]       | [X-Y]   | [resumo]          |
```

Identifique:
- Todos os documentos presentes nos autos
- Eventuais lacunas (documentos referenciados mas não encontrados)
- Fase atual do processo

## ETAPA 2 — EXTRAÇÃO DE DADOS

### 2.1 Identificação
- Processo n.: [numero]
- Vara/Juizo: [identificacao]
- Classe: [classe]
- Valor da causa: [valor]
- Distribuicao: [data]
- Justica gratuita: [sim/nao/requerida — para cada parte]
- Prioridade: [tipo ou N/A]

### 2.2 Partes e procuradores
Para CADA parte:
```
POLO ATIVO:
- [nome em minusculas] — CPF/CNPJ: [numero]
  Advogado(s): [nome] — OAB [UF] n. [numero]

POLO PASSIVO:
- [nome em minusculas] — CPF/CNPJ: [numero]
  Advogado(s): [nome] — OAB [UF] n. [numero]
```

### 2.3 Pedidos (exaustivamente)
```
PEDIDOS DO AUTOR
=================
P1: [descricao precisa] — (ev. X, TIPO, p. Y)
    Valor especifico: [se quantificado]

P2: [proximo pedido]
```

## ETAPA 3 — CRONOLOGIA

### 3.1 Cronologia dos fatos (direito material)
```
DATA        | FATO                         | FONTE          | VERSAO
------------|------------------------------|----------------|--------
[dd/mm/aaaa]| [descricao]                  | (ev. X, p. Y)  | [Autor/Reu/Ambos]
```

Regras:
- Se a data e aproximada, indique: "~[mes/ano]"
- Se apenas uma parte alega o fato, indique qual
- Se as partes divergem sobre a data, registre ambas
- Se nao ha data nos autos, diga expressamente

### 3.2 Cronologia processual (atos do processo)
```
DATA        | ATO PROCESSUAL                    | LOCALIZACAO
------------|-----------------------------------|------------
[dd/mm/aaaa]| [ato]                             | (ev. X)
```

### 3.3 Prescricao / decadencia
- Fato gerador: [data] — [descricao]
- Prazo aplicavel: [X anos — fundamento]
- Termo final: [data]
- Acao ajuizada em: [data]
- Situacao: [dentro do prazo / prescrito / limítrofe]
- Causas de interrupcao/suspensao: [se houver]

## ETAPA 4 — TESES DAS PARTES

### 4.1 Tese do autor
Para CADA pedido:
- Causa de pedir remota (fatos)
- Causa de pedir proxima (fundamento juridico)
- Provas indicadas

### 4.2 Tese do reu
Para CADA pedido contestado:
- Preliminares arguidas
- Defesa de merito (direta e indireta)
- Provas indicadas

### 4.3 Fatos incontroversos
```
| Fato | Autor (ref.) | Reu (ref.) |
|------|-------------|------------|
| [fato] | (ev. X, p. Y) | (ev. X, p. Y) |
```

### 4.4 Fatos controvertidos
```
| Fato | Versao do Autor | Versao do Reu | Onus da prova |
|------|----------------|---------------|---------------|
| [fato] | [versao — ref.] | [versao — ref.] | [quem] |
```

### 4.5 Argumentos nao enfrentados
Identifique argumentos que uma parte levantou e a outra nao respondeu:
- Do autor (nao respondidos pelo reu): [lista com ref.]
- Do reu (nao respondidos pelo autor): [lista com ref.]
- Estes argumentos, se relevantes, DEVEM ser enfrentados na sentenca (art. 489, par. 1, IV, CPC)

## ETAPA 5 — QUESTOES PRELIMINARES E PREJUDICIAIS

### 5.1 Pressupostos processuais
- Capacidade, competencia, citacao valida, regularidade formal

### 5.2 Condicoes da acao
- Legitimidade ativa e passiva, interesse processual

### 5.3 Preliminares da contestacao
Para cada preliminar arguida:
- Descricao, fundamento, analise, conclusao

### 5.4 Prejudiciais de merito
- Prescricao, decadencia, coisa julgada, litispendencia, perempcao

## ETAPA 6 — SINTESE PARA DECISAO

```
SINTESE
========
Pedido P1: [descricao]
  Tendencia: [procedente/improcedente/parcial]
  Fundamento central: [resumo em 2-3 linhas]
  Pontos de atencao: [riscos, divergencias]

Pedido P2: [...]

QUESTOES PENDENTES:
- [listar qualquer questao nao resolvida com os autos fornecidos]

ALERTAS:
- [nulidades, prescricao, questoes de ordem publica]
```

## ETAPA 7 — POSSIVEIS IMPRECISOES

Liste aqui todos os pontos onde a confianca e inferior a 90%:
```
| Afirmacao | Motivo da incerteza | Acao sugerida |
|-----------|--------------------|--------------| 
| [afirmacao] | [motivo] | [VERIFICAR: ...] |
```
