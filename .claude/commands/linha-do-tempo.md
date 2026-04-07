# Linha do Tempo — Cronologia dos Fatos e Atos Processuais

Construa uma cronologia detalhada e precisa de todos os fatos relevantes e atos processuais do caso.

$ARGUMENTS

---

## Formato da Linha do Tempo

### SEÇÃO A — Cronologia dos Fatos (Direito Material)

Eventos que compõem a causa de pedir — fatos da vida real que originaram o litígio:

```
CRONOLOGIA DOS FATOS
=====================

DATA        | FATO                              | FONTE         | VERSÃO
------------|-----------------------------------|---------------|--------
[dd/mm/aaaa]| [descrição objetiva do fato]      | [p. XX]       | [Autor/Réu/Ambos]
[dd/mm/aaaa]| [descrição objetiva do fato]      | [p. XX]       | [Autor/Réu/Ambos]
[sem data]  | [fato sem data precisa nos autos] | [p. XX]       | [parte]
```

**Regras:**
- Ordene cronologicamente
- Se a data é aproximada, indique: "~[mês/ano]" ou "[período]"
- Se apenas uma parte alega o fato, indique qual
- Se as partes divergem sobre a data, registre ambas versões
- Se não há data nos autos, coloque na posição mais provável com nota

### SEÇÃO B — Cronologia Processual (Atos do Processo)

Atos processuais em ordem cronológica:

```
CRONOLOGIA PROCESSUAL
======================

DATA        | ATO PROCESSUAL                           | LOCALIZAÇÃO
------------|------------------------------------------|------------
[dd/mm/aaaa]| Distribuição da ação                     | [p. XX]
[dd/mm/aaaa]| Petição inicial protocolada               | [p. XX]
[dd/mm/aaaa]| Decisão inicial (recebimento/emenda)      | [p. XX]
[dd/mm/aaaa]| [Tutela de urgência deferida/indeferida]  | [p. XX]
[dd/mm/aaaa]| Citação do réu [forma]                    | [p. XX]
[dd/mm/aaaa]| Contestação apresentada                   | [p. XX]
[dd/mm/aaaa]| [Reconvenção, se houver]                  | [p. XX]
[dd/mm/aaaa]| Réplica                                   | [p. XX]
[dd/mm/aaaa]| [Audiência de conciliação]                | [p. XX]
[dd/mm/aaaa]| Saneamento / Organização do processo      | [p. XX]
[dd/mm/aaaa]| [Provas produzidas — especificar]         | [p. XX]
[dd/mm/aaaa]| [Perícia — laudo / impugnação]            | [p. XX]
[dd/mm/aaaa]| [Audiência de instrução]                  | [p. XX]
[dd/mm/aaaa]| Alegações finais — Autor                  | [p. XX]
[dd/mm/aaaa]| Alegações finais — Réu                    | [p. XX]
[dd/mm/aaaa]| [Parecer do MP, se houver]                | [p. XX]
[dd/mm/aaaa]| Conclusos para sentença                   | [p. XX]
```

### SEÇÃO C — Prazos e Marcos Relevantes

```
PRAZOS E MARCOS
================

PRESCRIÇÃO / DECADÊNCIA:
- Fato gerador: [data] — [descrição]
- Prazo aplicável: [X anos — fundamento legal]
- Termo final: [data]
- Ação ajuizada em: [data]
- Situação: [✅ Dentro do prazo / ❌ Prescrito/Decaído / ⚠️ Limítrofe]
- Causas de interrupção/suspensão: [se houver — ref. p. XX]

OUTROS MARCOS TEMPORAIS:
- [Vencimento de obrigação]: [data]
- [Notificação extrajudicial]: [data]
- [Prazo contratual]: [data]
- [Prazo legal relevante]: [data]
```

### SEÇÃO D — Linha Visual

```
LINHA DO TEMPO VISUAL
======================

[data1] ──── Fato originário
    │
[data2] ──── Fato relevante
    │
[data3] ──── Último fato antes da ação
    │
    ▼
[data4] ════ AJUIZAMENTO DA AÇÃO
    │
[data5] ──── Citação
    │
[data6] ──── Contestação
    │
[data7] ──── [outros atos]
    │
    ▼
[HOJE] ════ FASE ATUAL: [identificar]
```

### SEÇÃO E — Divergências Cronológicas

Se as partes apresentam versões diferentes dos fatos:

```
DIVERGÊNCIAS NA CRONOLOGIA
============================

FATO: [descrição]
┌─────────────────────────────────────────┐
│ VERSÃO DO AUTOR (p. XX):               │
│ [o que o autor diz que aconteceu]       │
│ Data alegada: [data]                    │
├─────────────────────────────────────────┤
│ VERSÃO DO RÉU (p. XX):                 │
│ [o que o réu diz que aconteceu]         │
│ Data alegada: [data]                    │
├─────────────────────────────────────────┤
│ PROVAS:                                 │
│ [o que as provas indicam]               │
│ CONCLUSÃO: [versão mais provável]       │
│ Certeza: [✅/🟢/🟡/🟠/🔴]               │
└─────────────────────────────────────────┘
```

---

## Regras de Confiabilidade

1. **NUNCA** invente datas — se não consta nos autos, diga expressamente
2. Use `[DATA NÃO INFORMADA NOS AUTOS]` quando necessário
3. Diferencie claramente **fatos** (direito material) de **atos processuais** (direito processual)
4. Toda entrada deve ter referência à página dos autos
5. Se a cronologia revela inconsistência (ex: fato posterior citado como anterior), ALERTE
