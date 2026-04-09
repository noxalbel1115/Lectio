# Plano: Materiais de Revisão — História da Filosofia

## Contexto

O usuário tem um resumo completo de **História da Filosofia** (`PLATÃO.docx`, ~315K caracteres, ~1660 linhas) cobrindo dos Pré-Socráticos a Kant. Ele já estudou e resumiu — agora quer **memorizar**. O objetivo é criar um arsenal completo de ferramentas de revisão ativa.

O repositório Lectio é uma PWA de plano de leitura bíblica. Os novos materiais serão **páginas HTML separadas** no mesmo repositório, seguindo o mesmo padrão visual (Cormorant Garamond, Crimson Text, paleta burgundy/gold, mobile-first).

**Arquitetura existente:** Single-file HTML com CSS vars em `:root` (burgundy `#6b2737`, gold `#b8860b`, fundo `#faf6ef`), dark mode via `[data-theme="dark"]`, dados JSON inline, estado em `localStorage`, vanilla JS puro sem frameworks.

---

## Divisão do Conteúdo em 9 Módulos

| # | Módulo | Linhas | ~Tamanho | Filósofos principais |
|---|--------|--------|----------|---------------------|
| 1 | Pré-Socráticos Naturalistas | 4-67 | 20K | Tales, Anaximandro, Anaxímenes, Heráclito |
| 2 | Pitagóricos e Filósofos do Ser | 68-156 | 19K | Pitágoras, Xenófanes, Parmênides, Zenão, Melisso |
| 3 | Pluralistas e Atomistas | 157-231 | 11K | Empédocles, Anaxágoras, Leucipo, Demócrito |
| 4 | Sofistas e Sócrates | 232-253 | 7K | Protágoras, Górgias, Sócrates, Socráticos Menores |
| 5 | Platão | 254-456 | 35K | Teoria das Ideias, Alma, Amor, Política |
| 6 | Aristóteles | 457-833 | 55K | Metafísica, Física, Ética, Política, Lógica, Poética |
| 7 | Era Helenística | 834-1200 | 55K | Cinismo, Epicurismo, Estoicismo, Ceticismo |
| 8 | Era Imperial | 1201-1540 | 70K | Estoicismo Romano, Neoplatonismo, Plotino |
| 9 | Bíblia, Filosofia Cristã e Kant | 1541-1666 | 22K | Ideias bíblicas, Kant |

---

## Arquivos a Criar (9 materiais + service worker)

```
Lectio/
├── index.html                   (existente — adicionar link para filosofia/)
├── sw.js                        (existente — atualizar URLS com novos arquivos)
├── filosofia/
│   ├── index.html               ← Hub central (navegação + progresso geral)
│   ├── flashcards.html          ← Flashcards com repetição espaçada SM-2 (~550 cartões)
│   ├── quiz.html                ← Quiz gamificado multi-modo (~370 questões)
│   ├── timeline.html            ← Linha do tempo interativa (~50 filósofos)
│   ├── glossario.html           ← Glossário de ~200 termos filosóficos
│   ├── podcast.html             ← 12 episódios de podcast com TTS
│   ├── comparacoes.html         ← 10 tabelas comparativas entre filósofos
│   ├── mapa-mental.html         ← Mapas mentais interativos SVG (~10 mapas)
│   ├── resumos.html             ← Resumos navegáveis com destaques
│   └── conexoes.html            ← Grafo de influências entre ~40 filósofos
```

Cada arquivo é **self-contained** (CSS + JS + dados JSON embutidos). Todos funcionam offline (~587KB total).

---

## 1. Hub Central (`filosofia/index.html`) — ~9KB

**O que é:** Página de navegação que conecta todos os materiais e mostra progresso geral.

**Features:**
- Cards para cada ferramenta (grade 2 colunas mobile, 3 desktop) com ícones SVG
- Barra de progresso geral (% de flashcards dominados, quizzes completados)
- Seção "Estudo Diário Sugerido" baseada no algoritmo de repetição espaçada
- Seletor de módulo (filtrar por período filosófico)
- Dark mode sincronizado com o app principal (lendo `lectio_v2` do localStorage)
- Link de volta ao Lectio principal

**localStorage key:** `filosofia_hub`

---

## 2. Flashcards (`filosofia/flashcards.html`) — ~95KB

**O que é:** Sistema de repetição espaçada com cartões de pergunta/resposta. **Prioridade máxima** para memorização.

**Dados:** Array JSON embutido com ~550 cartões:
```json
{
  "id": "m1_01",
  "modulo": 1,
  "front": "Qual o princípio (arché) proposto por Tales de Mileto?",
  "back": "A água. Tudo vem da água, tudo conserva a vida com água e tudo termina na água. Não é a água física, mas uma água totalizante, de caráter divino.",
  "tags": ["pre-socraticos", "tales", "arche"],
  "difficulty": 2
}
```

**Tipos de flashcard** (variar para evitar monotonia):
- **Conceito→Definição**: "O que é X?" / definição
- **Filósofo→Ideia**: "Quem propõe X?" / filósofo + contexto
- **Citação→Autor**: citação famosa / quem disse e em que contexto
- **Comparação**: "Diferença entre X em Platão e Aristóteles" / explicação
- **Causa→Consequência**: "Por que X criticou Y?" / motivação filosófica

**Algoritmo SM-2 (repetição espaçada):**
```javascript
// Estado salvo por card: { ease: 2.5, interval: 1, repetitions: 0, nextReview: "2026-04-10" }
function sm2(card, quality) {
  // quality: 0=esqueceu, 3=difícil, 4=bom, 5=fácil
  if (quality < 3) {
    card.repetitions = 0;
    card.interval = 1;
  } else {
    if (card.repetitions === 0) card.interval = 1;
    else if (card.repetitions === 1) card.interval = 3;
    else card.interval = Math.round(card.interval * card.ease);
    card.ease = Math.max(1.3, card.ease + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)));
    card.repetitions++;
  }
  card.nextReview = addDays(today(), card.interval);
}
```

**Interações:**
- Card flip com CSS 3D transform (`rotateY(180deg)`, `backface-visibility: hidden`)
- Swipe left/right como alternativa aos botões
- Botões: "De novo" (0), "Difícil" (3), "Bom" (4), "Fácil" (5)
- Filtro por deck/módulo com tabs
- Modo "Revisão do dia" (só cards com `nextReview <= hoje`)
- Modo "Estudo novo" (cards nunca vistos, 20 por sessão)
- Dashboard: cards por caixa, % dominados, streak
- Progresso salvo em localStorage

**localStorage key:** `filosofia_flashcards`

---

## 3. Quiz/Jogo (`filosofia/quiz.html`) — ~78KB

**O que é:** Jogo gamificado com múltiplos modos para testar conhecimento.

**Dados:** Array JSON embutido com ~370 questões:
```json
{
  "id": "mc_m1_01",
  "modulo": 1,
  "tipo": "multipla",
  "pergunta": "Quem propôs o fogo como princípio (arché)?",
  "opcoes": ["Tales", "Heráclito", "Anaximandro", "Anaxímenes"],
  "resposta": 1,
  "explicacao": "Heráclito de Éfeso propôs o fogo como princípio, representando o eterno devir."
}
```

**Modos de Jogo:**
1. **Modo Clássico** — 10 questões aleatórias, múltipla escolha, pontuação
2. **Verdadeiro ou Falso** — Afirmações rápidas, swipe V/F (~150 questões)
3. **Quem Disse?** — Identifique o filósofo pela ideia/citação
4. **Associação** — Drag & drop para conectar filósofo↔conceito (~50 questões)
5. **Desafio Cronológico** — Ordene eventos/filósofos na ordem correta
6. **Contra o Tempo** — 60 segundos, quantas acertar
7. **Modo Maratona** — Todas as questões de uma seção, sem limite

**Gamificação:**
- Pontuação: rápido (<5s) = 100pts, normal (5-15s) = 75pts, lento (>15s) = 50pts
- Combo: +10 por acerto consecutivo
- Confetti na pontuação perfeita
- Explicação detalhada após cada resposta (crucial para aprendizado)
- Recordes salvos em localStorage
- Seletor de módulo ou "Todos os módulos"

**localStorage key:** `filosofia_quiz`

---

## 4. Linha do Tempo (`filosofia/timeline.html`) — ~29KB

**O que é:** Visualização cronológica dos filósofos (~624 a.C. a ~529 d.C.).

**Dados:** ~50 entradas com nome, datas, escola, contribuição principal, cor por período.

**Períodos com cores:**
- Pré-Socráticos: `#7B68EE`
- Período Clássico: `#6b2737`
- Helenístico: `#b8860b`
- Imperial: `#3d7a47`

**Interações:**
- Scroll horizontal/vertical por eras
- Zoom in/out nos períodos
- Tap para popup com resumo do filósofo
- Linhas de conexão mestre→discípulo
- Filtro por escola/período
- Marcadores de eventos históricos (Guerras Pérsicas, Alexandre, Império Romano)

**Implementação:** CSS Grid com colunas = décadas, linhas = escolas. `overflow-x: auto` para mobile.

**localStorage key:** `filosofia_timeline`

---

## 5. Glossário (`filosofia/glossario.html`) — ~49KB

**O que é:** Dicionário de ~200 termos filosóficos com definições e referências cruzadas.

**Dados:**
```json
{
  "term": "Arché (Arqué)",
  "greek": "ἀρχή",
  "definition": "Princípio primeiro, origem e fundamento de todas as coisas.",
  "context": "Termo central da filosofia pré-socrática...",
  "relatedPhilosophers": ["Tales", "Anaximandro", "Anaxímenes"],
  "relatedTerms": ["physis", "apeiron", "logos"],
  "section": "pre-socraticos"
}
```

**Features:**
- Busca instantânea (filtro por digitação)
- Índice alfabético com scroll-to
- Agrupamento por seção/escola
- Links cruzados clicáveis entre termos
- Destaque da etimologia grega
- Modo "estudo": flip card (ver termo → tentar lembrar definição)

**localStorage key:** `filosofia_glossario`

---

## 6. Podcast (`filosofia/podcast.html`) — ~131KB

**O que é:** 12 episódios em formato conversacional (Professor + Aluno), com TTS nativo.

**Episódios:**
1. "Os Primeiros Filósofos: A Busca pela Arché" — Tales, Anaximandro, Anaxímenes
2. "Heráclito e Parmênides: Movimento vs. Imobilidade"
3. "Pitágoras e os Números como Essência"
4. "Os Pluralistas: Empédocles, Anaxágoras e os Atomistas"
5. "Sofistas: Relativismo e Retórica"
6. "Sócrates: O Parteiro das Ideias"
7. "Platão I: O Mundo das Ideias"
8. "Platão II: Alma, Amor e Política"
9. "Aristóteles I: Metafísica e Lógica"
10. "Aristóteles II: Ética, Política e Poética"
11. "Filosofia Helenística: Epicurismo, Estoicismo e Ceticismo"
12. "Neoplatonismo e a Transição para o Cristianismo"

**Formato:** ~50-80 falas por episódio, tom acessível mas preciso, analogias modernas, "Pontos-chave" e "Questões para reflexão" ao final.

**Interface:**
- Player de texto com scroll sincronizado e highlight da fala atual
- Balões estilizados (host esquerda, expert direita)
- Botão "Ler em Voz Alta" via Web Speech API (`speechSynthesis`, `lang: 'pt-BR'`)
- Modo leitura (tipografia otimizada, fundo sépia)
- Marcação de episódios lidos

**localStorage key:** `filosofia_podcast`

---

## 7. Tabelas Comparativas (`filosofia/comparacoes.html`) — ~42KB

**O que é:** Tabelas side-by-side comparando filósofos em temas transversais.

**10 Comparações planejadas:**
1. Arché dos Pré-Socráticos: Tales vs Anaximandro vs Anaxímenes vs Heráclito vs Pitágoras
2. Ser e Devir: Heráclito vs Parmênides
3. Pluralistas: Empédocles vs Anaxágoras vs Atomistas
4. Conhecimento: Sofistas vs Sócrates vs Platão vs Aristóteles
5. Metafísica: Platão (Ideias) vs Aristóteles (Hilemorfismo)
6. Ética: Platão vs Aristóteles vs Estóicos vs Epicuristas
7. Política: Platão vs Aristóteles
8. Alma: Platão vs Aristóteles vs Estóicos vs Plotino
9. Escolas Helenísticas: Epicurismo vs Estoicismo vs Ceticismo
10. Neoplatonismo: Plotino vs Platão

**Interações:**
- Tabela responsiva (colapsa para cards no mobile)
- Headers sticky ao scrollar
- Células clicáveis para expandir detalhes
- Toggle para mostrar/esconder colunas

**localStorage key:** `filosofia_comparacoes`

---

## 8. Mapas Mentais (`filosofia/mapa-mental.html`) — ~43KB

**O que é:** Diagramas de árvore interativos para cada seção/filósofo (~10 mapas).

**Dados:**
```json
{
  "id": "platao",
  "title": "Platão — Visão Geral",
  "root": {
    "label": "Platão",
    "children": [
      {
        "label": "Teoria das Ideias",
        "color": "#7B68EE",
        "children": [
          { "label": "Mundo Sensível vs Inteligível" },
          { "label": "Participação (méthexis)" },
          { "label": "Hiperurânio" }
        ]
      }
    ]
  }
}
```

**Implementação:** SVG puro, layout radial/horizontal, nós clicáveis que expandem/colapsam, zoom e pan com touch.

**localStorage key:** `filosofia_mapas`

---

## 9. Resumos Navegáveis (`filosofia/resumos.html`) — ~111KB

**O que é:** Versão estruturada do conteúdo original com destaques e seções colapsáveis.

**Features:**
- Texto completo organizado por seções colapsáveis (acordeão)
- Conceitos-chave em `<mark>` com tooltip de definição (linkado ao glossário)
- "Modo destaque": usuário marca trechos importantes (salvo no localStorage)
- Barra lateral com índice de seções
- Indicador de scroll progress
- Botão "Marcar como estudado" por seção
- Botões "Praticar flashcards desta seção" e "Fazer quiz desta seção"

**localStorage key:** `filosofia_resumos`

---

## 10. Mapa de Conexões (`filosofia/conexoes.html`)

**O que é:** Grafo interativo de influências e oposições entre ~40 filósofos.

**Features:**
- Grafo canvas/SVG com filósofos como nós
- Setas de influência (quem influenciou quem) e oposição
- Agrupamento por escola/período com cores
- Clique: destaca conexões + mostra resumo
- Zoom e pan (touch-friendly)
- Legenda de cores

---

## Princípios Pedagógicos Aplicados

| Princípio | Material | Como |
|-----------|----------|------|
| **Recall ativo** | Flashcards, Quiz | Obriga a lembrar antes de ver resposta |
| **Repetição espaçada** | Flashcards (SM-2) | Revisa no momento ótimo antes de esquecer |
| **Interleaving** | Quiz (mix de seções) | Mistura tópicos na mesma sessão |
| **Elaboração** | Podcast, Resumos | Conecta ideias, explica o "porquê" |
| **Dual coding** | Mapa mental, Timeline | Representação visual + textual |
| **Retrieval practice** | Quiz, Flashcards | Recuperar > reler |
| **Contextualização** | Timeline, Comparações | Situa cada ideia no tempo e contra alternativas |
| **Metacognição** | Flashcards (autoavaliação) | Usuário avalia o próprio conhecimento |

---

## Estimativa de Conteúdo por Módulo

| Seção | Linhas | Flashcards | Questões Quiz | Episódios Podcast |
|-------|--------|------------|---------------|-------------------|
| Pré-Socráticos | ~156 | ~60 | ~40 | 2 |
| Pluralistas | ~36 | ~25 | ~15 | 1 |
| Sofistas e Sócrates | ~59 | ~35 | ~25 | 2 |
| Platão | ~194 | ~80 | ~55 | 2 |
| Aristóteles | ~376 | ~120 | ~80 | 2 |
| Era Helenística | ~366 | ~100 | ~65 | 1 |
| Era Imperial | ~339 | ~90 | ~60 | 1 |
| Filosofia Cristã | ~116 | ~40 | ~30 | 1 |
| **Total** | **~1660** | **~550** | **~370** | **12** |

---

## Estratégia de Implementação

### Fase 1 — Fundação (prioridade máxima)
1. Script de extração do DOCX (python-docx → JSON estruturado)
2. Hub central (`filosofia/index.html`)
3. **Flashcards** (`filosofia/flashcards.html`) — maior impacto para memorização

### Fase 2 — Core
4. **Quiz** (`filosofia/quiz.html`) — gamificação e recall ativo
5. **Glossário** (`filosofia/glossario.html`) — referência rápida
6. **Resumos** (`filosofia/resumos.html`) — texto base navegável

### Fase 3 — Enriquecimento
7. Timeline (`filosofia/timeline.html`) — contexto temporal
8. Comparações (`filosofia/comparacoes.html`) — pensamento crítico
9. Podcast (`filosofia/podcast.html`) — aprendizagem auditiva

### Fase 4 — Visual
10. Mapa mental (`filosofia/mapa-mental.html`) — layout SVG complexo
11. Conexões (`filosofia/conexoes.html`) — grafo de influências

### Fase 5 — Integração
12. Atualizar `sw.js` com novos caminhos de cache
13. Adicionar link no `index.html` principal
14. Commit na branch `claude/check-platao-access-Yy6Qt` e push

---

## Sincronização de Tema (em todos os arquivos)

```javascript
function syncTheme() {
  try {
    var s = JSON.parse(localStorage.getItem('lectio_v2') || '{}');
    if (s.theme === 'dark') document.documentElement.setAttribute('data-theme', 'dark');
  } catch(e) {}
}
syncTheme();
```

---

## Verificação Final

1. Abrir cada HTML no navegador e verificar funcionalidade
2. Testar flashcards: virar cartões, classificar, persistência no localStorage
3. Testar quiz: todos os modos, pontuação e explicações
4. Testar timeline: scroll, zoom, clique em filósofos
5. Testar glossário: busca, links cruzados, modo estudo
6. Testar podcast: navegação entre episódios, TTS
7. Testar comparações: tabelas, responsividade
8. Testar mapas mentais: expandir/colapsar, zoom
9. Testar resumos: acordeão, destaques, links para quiz/flashcards
10. Testar conexões: interação com grafo
11. Verificar responsividade mobile em todos
12. Verificar modo escuro em todos
13. Verificar que hub links funcionam
14. Testar offline (service worker)

---

## Arquivos Críticos

- **Fonte de dados:** `PLATÃO.docx` (extrair via python-docx, já instalado)
- **Referência de design:** `index.html` (CSS vars, fontes, paleta burgundy/gold)
- **Service Worker:** `sw.js` (atualizar `URLS` e incrementar `CACHE_NAME` para `lectio-v4`)
- **Branch:** `claude/check-platao-access-Yy6Qt`

---

## Tamanho Estimado Total

| Arquivo | Dados JSON | Total |
|---------|-----------|-------|
| Hub | ~1KB | ~9KB |
| Flashcards | ~80KB (~550 cards) | ~95KB |
| Quiz | ~60KB (~370 questões) | ~78KB |
| Podcast | ~120KB (12 scripts) | ~131KB |
| Timeline | ~15KB | ~29KB |
| Glossário | ~40KB (~200 termos) | ~49KB |
| Comparações | ~30KB (10 tabelas) | ~42KB |
| Mapa mental | ~25KB (10 mapas) | ~43KB |
| Resumos | ~100KB (texto completo) | ~111KB |
| Conexões | ~10KB | ~25KB |
| **Total** | | **~612KB** |
