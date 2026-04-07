# Relatório de Pesquisa: Melhores Práticas para IA em Assessoria Judicial

**Data:** 07/04/2026
**Projeto:** Lectio — Assessoria Jurídica com IA

---

## 1. FERRAMENTAS DE IA EM USO NO JUDICIÁRIO BRASILEIRO

### 1.1 VICTOR (STF)

Parceria STF + UnB. Executa: (i) OCR, (ii) separação de documentos, (iii) classificação de peças, (iv) identificação de temas de repercussão geral. Classifica 27 temas com ~95% de acerto. É indicativo — nunca decide, sempre validado pelos ministros.

**O que funciona:** Tarefas de classificação com escopo limitado e supervisão humana obrigatória.

Fontes:
- https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=471331&ori=1
- https://noticias.stf.jus.br/postsnoticias/stf-amplia-uso-de-inteligencia-artificial-em-apoio-a-atividade-jurisdicional/

### 1.2 Plataforma SINAPSES (CNJ/TRF4)

Instituída pela Resolução CNJ 332/2020. Plataforma nacional de armazenamento, treinamento supervisionado, controle de versionamento, distribuição e auditoria de modelos de IA. Atualmente reúne 150 modelos ativos, produzidos por 29 tribunais. Integrada ao PJe para classificação de classe, assunto e indicação de precedentes.

**O que funciona:** Centralização de modelos, governança unificada, repositório compartilhado.

Fontes:
- https://www.undp.org/pt/brazil/news/plataforma-sinapses-reune-150-modelos-de-inteligencia-artificial
- https://www.cnj.jus.br/sistemas/plataforma-sinapses/

### 1.3 PJe (Processo Judicial Eletrônico)

Opera em 70% do Judiciário. IA integrada para classificação automática de petições, sugestão de assuntos e indicação de precedentes via Sinapses.

### 1.4 Prometea (Argentina — referência comparativa)

Sistema da Promotoria de Buenos Aires. Prediz resultados com 96% de acurácia em <20 segundos. Produtividade: de 130 para 490 casos/mês (+300%). Em 2024, começaram a migrar para IA generativa.

**Lição:** Mesmo sistemas bem-sucedidos de classificação estão sendo substituídos por LLMs, validando a abordagem do Lectio.

Fontes:
- https://inter-american-law-review.law.miami.edu/prometea-revolutionizing-judicial-efficiency-in-argentina-through-artificial-intelligence-powered-legal-solutions/
- https://www.techandjustice.bsg.ox.ac.uk/research/argentina

### 1.5 Panorama geral

O Brasil tem mais de 140 ferramentas de IA no Judiciário. A Resolução CNJ 615/2025 exige que todos os tribunais reportem projetos e submetam modelos ao Sinapses. O acervo do STF caiu ao menor nível desde 1992 com auxílio de IA.

Fontes:
- https://www.techandjustice.bsg.ox.ac.uk/research/brazil
- https://www.sipa.columbia.edu/aidriven-innovations-brazilian-judiciary
- https://restofworld.org/2025/brazil-ai-courts-lawsuits/

---

## 2. REGULAMENTAÇÃO: CNJ E MARCO NORMATIVO

### 2.1 Resolução CNJ 332/2020

Primeiros parâmetros para IA no Judiciário. Criou a Plataforma Sinapses. Requisitos básicos de transparência e supervisão humana.

Fonte: https://atos.cnj.jus.br/atos/detalhar/3429

### 2.2 Resolução CNJ 615/2025 (vigência a partir de 14/07/2025)

**Princípios:** justiça, equidade, inclusão, não discriminação, explicabilidade, confiabilidade e segurança jurídica.

**Classificação de risco:** Sistemas categorizados em baixo ou alto risco, com auditorias regulares para alto risco.

**Supervisão humana obrigatória:** Juízes mantêm responsabilidade integral sobre decisões geradas com auxílio de IA.

**Proibições:** Decisões automatizadas sobre mérito sem revisão judicial. Uso irrestrito de dados pessoais.

**Governança:** Comitê Nacional de Inteligência Artificial do Judiciário (CNIAJ), com CNJ, tribunais, OAB, MP e sociedade civil.

**Transparência:** Sistemas auditados e documentados, com logs rastreáveis. Algoritmos devem explicar critérios.

**LGPD:** Proteção de dados integrada.

**Relevância para o Lectio:** O sistema já atende vários requisitos (supervisão humana, marcações [VERIFICAR], seção de imprecisões). Falta: (i) log de auditoria, (ii) classificação de risco por uso, (iii) declaração de transparência sobre uso de IA.

Fontes:
- https://atos.cnj.jus.br/atos/detalhar/6001
- https://www.cnj.jus.br/cnj-aprova-resolucao-regulamentando-o-uso-da-ia-no-poder-judiciario/

---

## 3. DIRETRIZES INTERNACIONAIS

### 3.1 UNESCO — Guidelines for AI in Courts (2025)

Primeiro framework ético global para IA em tribunais. 15 princípios: proteção de direitos humanos, não discriminação, transparência, accountability, supervisão humana, auditabilidade, segurança. Mensagem central: IA como ferramenta assistiva, não substitutiva.

Fonte: https://www.unesco.org/en/articles/guidelines-use-ai-systems-courts-and-tribunals

### 3.2 EU AI Act

IA na administração da justiça classificada como alto risco (Anexo III). Exige: avaliação de conformidade, registro em base da UE, gestão de risco e supervisão humana. Vigência: agosto de 2026.

Fonte: https://artificialintelligenceact.eu/annex/3/

### 3.3 EUA — Judiciário Federal

**Caso do Judge Rodriguez (Duke Judicature):**
- **Usos permitidos:** localização de documentos, resumo de testemunhos via RAG, preparação de audiências, cite-checking.
- **Usos proibidos:** redação de decisões finais, análise legal completa sem supervisão.
- **Workflow:** cada output de IA verificado clicando nos links para documentos originais. Prompts focados e específicos.

Fontes:
- https://judicature.duke.edu/articles/judging-ai-generative-ai-courts/
- https://www.americanbar.org/groups/judicial/resources/judges-journal/2025-spring/guidelines-judicial-officers-responsible-use-artificial-intelligence/

---

## 4. TÉCNICAS ANTI-ALUCINAÇÃO PARA IA JURÍDICA

### 4.1 O problema

Estudos de Stanford (2025): LLMs fabricam citações jurídicas em 30-45% das respostas. Ferramentas com RAG (LexisNexis, Westlaw) alucinam 17-33%. Mais de 700 casos judiciais já envolvem conteúdo fabricado por IA.

Fontes:
- https://onlinelibrary.wiley.com/doi/full/10.1111/jels.12413
- https://dho.stanford.edu/wp-content/uploads/Legal_RAG_Hallucinations.pdf

### 4.2 Técnicas de mitigação

**A. Ancoragem nos autos** (Lectio: implementada)
Exigir referências (ev. X, TIPO, p. Y) é a forma mais eficaz. Recomendação: cada parágrafo da fundamentação deve conter pelo menos uma referência.

**B. RAG (Retrieval-Augmented Generation)**
Integra bases externas para verificação de dispositivos, vigência e precedentes. Limitação: não elimina alucinações — LLM pode alucinar "em torno" do material recuperado.

**C. Marcação de incerteza** (Lectio: implementada)
[VERIFICAR] + "Possíveis imprecisões". Alinhado com melhores práticas.

**D. Verificação cruzada** (Lectio: implementada)
O `/verificar` é um dos pontos mais fortes do sistema.

**E. Separação fato vs. inferência** (Lectio: parcial)
Recomenda-se marcar explicitamente [FATO] e [INFERÊNCIA] nos outputs.

**F. Proibição de citações inventadas** (Lectio: implementada)
Regras de pesquisa jurídica proíbem citar sem tribunal, órgão, número e data. Alinhado com práticas internacionais.

---

## 5. PESQUISA ACADÊMICA

### 5.1 Prompt engineering jurídico

**Framework hierárquico de três estágios** (Nature, 2025): definição de tarefa + background de conhecimento + orientação de raciocínio. Resultados: +11% sensibilidade, +6% especificidade, +30-40% acurácia de citações.

**Chain of Logic (CoL):** Decomposição de regras em elementos, avaliação independente, recomposição lógica. Ideal para subsunção jurídica.

O `/analisar` do Lectio já implementa chain-of-thought com 7 etapas progressivas. Recomendação: explicitar raciocínio em cada parágrafo (premissa normativa → fato → conclusão).

Fontes:
- https://www.nature.com/articles/s41598-025-30306-9
- https://www.nature.com/articles/s41599-025-05924-3

### 5.2 Sistemas multi-agente

**SAMVAD:** Agentes simulando juiz, promotor, defensor + RAG jurídico.
**Chatlaw:** Multi-agente com SOPs que reduzem erros significativamente.

O Lectio já implementa workflow multi-etapa. Evolução futura: pipeline automático `/analisar` → `/provas` → `/decidir` → `/verificar`.

### 5.3 LLMs como decisores — limitações

Estudo 2026: LLMs são fortemente influenciados por precedentes mas não por contexto humano (oposto de juízes). Prompt engineering teve pouco sucesso em corrigir isso.

**Conclusão:** Confirma abordagem do Lectio — IA como assessor, não como decisor.

Fonte: https://www.tandfonline.com/doi/full/10.1080/07418825.2026.2618254

---

## 6. AVALIAÇÃO DO LECTIO vs. MELHORES PRÁTICAS

| Prática | Status no Lectio | Observação |
|---------|-----------------|------------|
| Supervisão humana | Implementada | Magistrado valida tudo |
| Anti-alucinação (ancoragem) | Implementada | Regra principal do CLAUDE.md |
| Marcação de incerteza | Implementada | [VERIFICAR] + Possíveis imprecisões |
| Verificação cruzada | Implementada | Comando /verificar |
| Checklist pré-decisão | Implementada | Comando /checklist |
| Proibição de citações inventadas | Implementada | Regras de pesquisa jurídica |
| Fundamentação art. 489 | Implementada | Skills de sentença |
| Matriz probatória | Implementada | Comando /provas |
| Formato para eproc | Implementado | Code blocks |
| Classificação de risco | NÃO implementada | Recomendação CNJ 615/2025 |
| Declaração de uso de IA | NÃO implementada | Recomendação CNJ 615/2025 |
| Log de auditoria | NÃO implementado | Recomendação CNJ 615/2025 |
| Integração RAG | NÃO implementada | Evolução futura |

---

## 7. RECOMENDAÇÕES PARA EVOLUÇÃO

### Prioridade ALTA (implementar agora)

1. **Declaração de transparência:** Nota ao final de cada output indicando uso de IA (conformidade CNJ 615/2025).
2. **Checklist automático art. 489, §1º:** Verificar os 6 incisos antes de entregar minuta.
3. **Separação explícita fato/inferência:** Marcar [FATO] vs. [INFERÊNCIA].

### Prioridade MÉDIA (próxima iteração)

4. **Gate de questões preliminares:** Alertar magistrado antes de analisar mérito se houver preliminar determinante.
5. **Suficiência probatória:** Avaliação de standard de prova por pedido.
6. **Pipeline integrado:** /analisar → /provas → /decidir → /verificar com passagem de contexto.
7. **Verificação de prova ilícita:** Campo no /provas.

### Prioridade BAIXA (evolução futura)

8. **Integração RAG:** Repositórios de legislação (Planalto), jurisprudência (STJ, STF).
9. **Multi-agente:** Agente verificador automático entre etapas.
10. **Log de auditoria:** Registro de análises, inputs e outputs (CNJ 615/2025).
11. **Classificação de risco:** /analisar = baixo; /decidir = alto.

---

## FONTES CONSOLIDADAS

- Oxford - Brazil AI: https://www.techandjustice.bsg.ox.ac.uk/research/brazil
- Columbia SIPA: https://www.sipa.columbia.edu/aidriven-innovations-brazilian-judiciary
- Rest of World: https://restofworld.org/2025/brazil-ai-courts-lawsuits/
- CNJ Resolução 615/2025: https://atos.cnj.jus.br/atos/detalhar/6001
- CNJ Resolução 332/2020: https://atos.cnj.jus.br/atos/detalhar/3429
- CNJ Sinapses: https://www.cnj.jus.br/sistemas/plataforma-sinapses/
- UNESCO Guidelines: https://www.unesco.org/en/articles/guidelines-use-ai-systems-courts-and-tribunals
- EU AI Act Annex III: https://artificialintelligenceact.eu/annex/3/
- Duke Judicature: https://judicature.duke.edu/articles/judging-ai-generative-ai-courts/
- ABA Guidelines: https://www.americanbar.org/groups/judicial/resources/judges-journal/2025-spring/guidelines-judicial-officers-responsible-use-artificial-intelligence/
- Stanford Hallucinations: https://onlinelibrary.wiley.com/doi/full/10.1111/jels.12413
- Stanford RAG: https://dho.stanford.edu/wp-content/uploads/Legal_RAG_Hallucinations.pdf
- Nature Framework: https://www.nature.com/articles/s41598-025-30306-9
- Nature LLMs Legal: https://www.nature.com/articles/s41599-025-05924-3
- Taylor & Francis LLMs Judges: https://www.tandfonline.com/doi/full/10.1080/07418825.2026.2618254
- STF Victor: https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=471331&ori=1
- UNDP Sinapses: https://www.undp.org/pt/brazil/news/plataforma-sinapses-reune-150-modelos-de-inteligencia-artificial
- Prometea: https://inter-american-law-review.law.miami.edu/prometea-revolutionizing-judicial-efficiency-in-argentina-through-artificial-intelligence-powered-legal-solutions/
