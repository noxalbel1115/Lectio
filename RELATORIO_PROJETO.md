# RELATÓRIO DO PROJETO LECTIO
## Sistema de Assessoria Jurídica com IA para Análise Processual

**Data:** 07/04/2026  
**Repositório:** noxalbel1115/Lectio  
**Branch:** claude/legal-case-analyzer-g6ZOv  

---

## 1. VISÃO GERAL

O projeto **Lectio** é um sistema de assessoria jurídica baseado em IA, projetado para auxiliar magistrados brasileiros na análise completa de processos judiciais. O objetivo central é permitir que o juiz trabalhe **sem precisar abrir os autos**, confiando na análise da IA com segurança superior à leitura humana.

O sistema opera dentro do **Claude Code** (CLI da Anthropic) utilizando **slash commands** personalizados que automatizam diferentes etapas da análise processual.

---

## 2. O QUE FOI CRIADO

### 2.1 Arquivo de Instruções do Projeto (`CLAUDE.md`)

Arquivo de configuração central que define:

- **Identidade do sistema**: assessor jurídico de alta confiabilidade
- **Princípios de confiabilidade**:
  - Regra de ouro: nunca alucinar (inventar informações)
  - Distinção rigorosa entre fontes (fato processual, conhecimento jurídico, análise/inferência)
  - Graus de certeza obrigatórios (Certo, Altamente Provável, Provável, Incerto, Impossível Determinar)
  - Auto-verificação obrigatória antes de entregar qualquer análise
- **Framework de Direito Processual Civil Brasileiro**: estrutura típica de processo, requisitos da sentença (art. 489, CPC), fundamentação adequada (art. 489, §1º)
- **Protocolo para documentos grandes**: estratégia de análise em camadas para processos volumosos
- **Regras de pesquisa jurídica**: diretrizes para citação de legislação, doutrina e jurisprudência
- **Formato de saída padrão**: template estruturado para análises completas

### 2.2 Comandos Slash (10 comandos)

Todos localizados em `.claude/commands/`:

#### `/analisar-processo` — Análise Completa
- Pipeline integral que executa todas as etapas de análise
- Gera relatório completo com: identificação, objeto, cronologia, teses, questões jurídicas, análise probatória, enquadramento jurídico, síntese e alertas
- Ponto de entrada recomendado para análise de um novo processo

#### `/extrair-dados` — Extração Estruturada
- Extrai e organiza todos os dados do processo em formato estruturado
- Identifica: partes, advogados, tipo de ação, valor da causa, pedidos, defesas
- Mapeia a estrutura documental completa do processo

#### `/analise-probatoria` — Análise de Provas
- Analisa detalhadamente as provas vinculadas a cada pedido
- Classifica provas por tipo (documental, testemunhal, pericial, etc.)
- Avalia força probatória e distribui ônus da prova
- Gera matriz pedido × prova com conclusão fundamentada

#### `/pesquisa-juridica` — Pesquisa Jurídica
- Pesquisa legislação, doutrina e jurisprudência aplicáveis ao caso
- Cita dispositivos legais exatos com verificação de vigência
- Apresenta correntes doutrinárias divergentes
- Alerta que jurisprudência citada de memória precisa ser verificada em repositórios oficiais

#### `/sintese` — Síntese Executiva
- Resumo executivo conciso para tomada de decisão
- Destaca questões-chave, posição recomendada e riscos
- Formato objetivo para magistrados com alto volume de trabalho

#### `/minuta-decisao` — Minuta de Decisão/Sentença
- Redige minuta completa seguindo os requisitos do art. 489, CPC
- Inclui relatório, fundamentação e dispositivo
- Trata de sucumbência, honorários, correção monetária e juros
- Verifica conformidade com art. 489, §1º (fundamentação adequada)

#### `/verificar` — Verificação Cruzada
- 6 checks de verificação:
  1. Consistência interna (contradições na análise)
  2. Completude (todos os pedidos/argumentos analisados)
  3. Referências aos autos (afirmações com fonte)
  4. Correção jurídica (legislação vigente, jurisprudência pertinente)
  5. Riscos processuais (nulidade, reforma, cerceamento)
  6. Anti-alucinação (verificação de informações potencialmente inventadas)
- Gera resultado consolidado: Aprovado / Aprovado com Ressalvas / Revisão Necessária

#### `/linha-do-tempo` — Cronologia
- Separa fatos materiais (causa de pedir) de atos processuais
- Registra divergências cronológicas entre as partes
- Calcula prazos de prescrição/decadência
- Gera linha do tempo visual

#### `/contraditorio` — Análise Comparativa
- Confronta argumento por argumento entre autor e réu
- Identifica fatos incontroversos (dispensam prova — art. 374, III, CPC)
- Mapeia fatos controvertidos com ônus da prova
- Lista argumentos não enfrentados (risco de nulidade — art. 489, §1º, IV)
- Avalia forças e fraquezas de cada posição

#### `/checklist-decisao` — Checklist Pré-Decisão
- 11 seções de verificação:
  - A: Pressupostos processuais (existência e validade)
  - B: Condições da ação
  - C: Questões prejudiciais e preliminares de mérito
  - D: Regularidade do contraditório
  - E: Intervenção do Ministério Público
  - F: Instrução probatória
  - G: Requisitos da sentença (art. 489)
  - H: Limites da decisão (ultra/extra/citra petita)
  - I: Sucumbência e honorários
  - J: Correção monetária e juros
  - K: Tutela de urgência
- Conclui se a decisão pode ser prolatada ou se há providências pendentes

---

## 3. DECISÕES DE DESIGN

### 3.1 Por que Claude Code com slash commands?
- Permite uso direto no terminal sem necessidade de aplicação web separada
- Cada comando é um template Markdown que guia a IA na tarefa específica
- O magistrado pode usar comandos individuais ou o pipeline completo
- Fácil de manter e expandir (basta adicionar novos arquivos `.md`)

### 3.2 Por que a ênfase em anti-alucinação?
- Em contexto jurídico, informação falsa pode gerar decisões injustas
- O sistema exige referência à página dos autos para toda afirmação factual
- Classifica cada informação por fonte (autos, conhecimento jurídico, inferência)
- Graus de certeza obrigam a IA a ser transparente sobre suas limitações

### 3.3 Por que separar em 10 comandos?
- Modularidade: o magistrado escolhe o nível de profundidade
- Processos simples podem precisar apenas de `/sintese`
- Processos complexos se beneficiam do pipeline completo
- Cada comando pode ser re-executado isoladamente se a análise inicial for insuficiente

### 3.4 Framework jurídico incorporado
- O sistema já conhece a estrutura do CPC/2015 (Código de Processo Civil)
- Requisitos da sentença (art. 489) são verificados automaticamente
- Checklist cobre desde pressupostos processuais até correção monetária
- Reduz risco de nulidade por fundamentação inadequada

---

## 4. FLUXO RECOMENDADO DE USO

```
PROCESSO NOVO
     │
     ▼
/extrair-dados ──────── Mapear o processo
     │
     ▼
/linha-do-tempo ─────── Entender a cronologia
     │
     ▼
/contraditorio ──────── Confrontar as teses
     │
     ▼
/analise-probatoria ─── Avaliar as provas
     │
     ▼
/pesquisa-juridica ──── Fundamentar juridicamente
     │
     ▼
/sintese ────────────── Resumo para decisão
     │
     ▼
/checklist-decisao ──── Verificar antes de decidir
     │
     ▼
/minuta-decisao ─────── Redigir a decisão
     │
     ▼
/verificar ──────────── Checar consistência final
```

Alternativa rápida: `/analisar-processo` executa o pipeline completo de uma vez.

---

## 5. ESTRUTURA DE ARQUIVOS

```
Lectio/
├── CLAUDE.md                              # Instruções do projeto (identidade, regras, framework)
├── RELATORIO_PROJETO.md                   # Este relatório
└── .claude/
    └── commands/
        ├── analisar-processo.md           # Análise completa
        ├── extrair-dados.md               # Extração de dados
        ├── analise-probatoria.md          # Análise de provas
        ├── pesquisa-juridica.md           # Pesquisa jurídica
        ├── sintese.md                     # Síntese executiva
        ├── minuta-decisao.md              # Minuta de decisão
        ├── verificar.md                   # Verificação cruzada
        ├── linha-do-tempo.md              # Cronologia
        ├── contraditorio.md               # Análise comparativa
        └── checklist-decisao.md           # Checklist pré-decisão
```

---

## 6. POSSÍVEIS EXPANSÕES FUTURAS

- **Integração com bases de jurisprudência** (via MCP servers) para busca automática em tribunais
- **Templates por tipo de ação** (consumidor, trabalhista, família, etc.) com checklist especializado
- **Comparação automática com precedentes** vinculantes (STF/STJ)
- **Cálculos automáticos** de prescrição, correção monetária e juros
- **Geração de relatório em PDF** formatado para juntada aos autos
- **Modo de revisão por pares** — um segundo agente verifica a análise do primeiro

---

## 7. CONSIDERAÇÕES TÉCNICAS

- **Plataforma**: Claude Code (CLI) — funciona no terminal, desktop, web e IDEs
- **Modelo**: Claude Opus 4.6 (1M de contexto) — suporta processos extensos
- **Formato dos comandos**: Markdown com variável `$ARGUMENTS` para receber input do usuário
- **Versionamento**: Git, hospedado no GitHub (noxalbel1115/Lectio)
- **Branch de desenvolvimento**: `claude/legal-case-analyzer-g6ZOv`

---

*Relatório gerado automaticamente como parte do projeto Lectio.*
