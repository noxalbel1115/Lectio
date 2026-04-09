# Plano: Materiais de Revisão — História da Filosofia

## Contexto

O usuário tem um resumo completo de **História da Filosofia** (`PLATÃO.docx`, ~315K caracteres, ~1660 linhas) cobrindo dos Pré-Socráticos a Kant. Ele já estudou e resumiu — agora quer **memorizar**. O objetivo é criar um arsenal completo de ferramentas de revisão ativa.

O repositório Lectio é uma PWA de plano de leitura bíblica. Os novos materiais serão **páginas HTML separadas** no mesmo repositório, seguindo o mesmo padrão visual (Cormorant Garamond, Crimson Text, paleta burgundy/gold, mobile-first).

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

## Arquivos a Criar

```
/home/user/Lectio/
├── filosofia/
│   ├── index.html              ← Hub central (navegação para todos os materiais)
│   ├── flashcards.html         ← Flashcards interativos (~400+ cartões)
│   ├── quiz.html               ← Jogo de quiz multi-modo (~250+ questões)
│   ├── timeline.html           ← Linha do tempo interativa + Glossário
│   ├── podcast.html            ← Roteiros de podcast (9 episódios)
│   └── conexoes.html           ← Mapa de conexões entre filósofos
```

Cada arquivo é **self-contained** (CSS + JS + dados JSON embutidos). Todos funcionam offline.

---

## 1. Hub Central (`filosofia/index.html`)

**O que é:** Página de navegação que conecta todos os materiais e mostra progresso geral.

**Features:**
- Cards para cada ferramenta (Flashcards, Quiz, Podcast, Timeline, Conexões)
- Barra de progresso geral (% de flashcards dominados, quizzes completados)
- Seletor de módulo (filtrar por período filosófico)
- Dados de progresso lidos do localStorage de cada ferramenta
- Design: mesmo estilo elegante do Lectio (burgundy/gold/serif)

---

## 2. Flashcards (`filosofia/flashcards.html`)

**O que é:** Sistema de repetição espaçada com cartões de pergunta/resposta.

**Dados:** Array JSON embutido com ~400-450 cartões, cada um com:
```json
{
  "id": "m1_01",
  "modulo": 1,
  "frente": "Qual o princípio (arché) proposto por Tales de Mileto?",
  "verso": "A água. Tudo vem da água, tudo conserva a vida com água e tudo termina na água. Não é a água física, mas uma água totalizante, de caráter divino.",
  "tags": ["pre-socraticos", "tales", "arche"]
}
```

**Distribuição:** ~45-50 cartões por módulo.

**Sistema de Revisão — Leitner (5 caixas):**
- Caixa 1: Novos/Errados → revisar toda sessão
- Caixa 2: Revisar a cada 2 sessões
- Caixa 3: Revisar a cada 4 sessões
- Caixa 4: Revisar a cada 8 sessões
- Caixa 5: Dominados → revisar a cada 16 sessões

**Interações:**
- Toque/clique para virar o cartão (animação 3D flip)
- Botões: "Errei" (volta para caixa 1), "Difícil" (mesma caixa), "Fácil" (avança caixa)
- Swipe left/right como alternativa
- Filtro por módulo e por caixa
- Modo "Revisão do Dia" (só mostra cartões devidos)
- Contador de sessão e streak
- Dashboard com estatísticas (cartões por caixa, % dominados)
- Progresso salvo em localStorage

---

## 3. Quiz/Jogo (`filosofia/quiz.html`)

**O que é:** Jogo gamificado com múltiplos modos para testar conhecimento.

**Dados:** Array JSON embutido com ~250+ questões:
```json
{
  "id": "q_m1_01",
  "modulo": 1,
  "tipo": "multipla",  // "multipla" | "vf" | "associacao" | "quem_disse"
  "pergunta": "Quem propôs o fogo como princípio (arché)?",
  "opcoes": ["Tales", "Heráclito", "Anaximandro", "Anaxímenes"],
  "resposta": 1,
  "explicacao": "Heráclito de Éfeso propôs o fogo como princípio, representando o eterno devir e a transformação constante."
}
```

**Modos de Jogo:**
1. **Modo Clássico** — 10 questões aleatórias, múltipla escolha, pontuação
2. **Verdadeiro ou Falso** — Afirmações rápidas, swipe para V ou F
3. **Quem Disse?** — Identifique o filósofo pela ideia/citação
4. **Associação** — Arraste para conectar filósofo↔conceito
5. **Desafio Cronológico** — Ordene eventos/filósofos na ordem correta
6. **Modo Maratona** — Questões infinitas até errar 3x

**Gamificação:**
- Pontuação por questão (base + bônus por tempo)
- Combo: acertos consecutivos multiplicam pontos
- Recordes salvos em localStorage
- Feedback visual: verde/vermelho + explicação após cada resposta
- Seletor de módulo ou "Todos os módulos"

---

## 4. Linha do Tempo + Glossário (`filosofia/timeline.html`)

**O que é:** Visualização cronológica dos filósofos + dicionário de termos.

**Timeline:**
- Linha horizontal scrollável (mobile: vertical)
- ~50 entradas com: nome, datas, escola, contribuição principal
- Cor por escola/período (Naturalistas=azul, Pitagóricos=roxo, Sofistas=laranja, etc.)
- Clique para expandir: resumo do filósofo + conceitos-chave
- Zoom: visão geral (séculos) ↔ detalhe (décadas)

**Glossário (~100 termos):**
- Aba separada (toggle Timeline/Glossário)
- Termos como: arché, physis, logos, nous, eidos, catarsis, eudaimonia, apeiron...
- Busca/filtro por texto
- Categorias: Metafísica, Ética, Lógica, Política, Estética
- Cada termo com: definição, filósofo(s) associado(s), contexto

---

## 5. Podcast (`filosofia/podcast.html`)

**O que é:** 9 roteiros de podcast em formato conversacional, prontos para leitura em voz alta ou uso com TTS.

**Formato:** Diálogo entre dois "apresentadores" (Professor e Aluno curioso):
- Tom acessível mas preciso
- Perguntas naturais que guiam a exploração
- Analogias com situações modernas
- Resumo de "pontos-chave" ao final de cada episódio
- Duração estimada: ~8-12 min de leitura cada

**Episódios:**
1. "O Início de Tudo" — Pré-Socráticos Naturalistas
2. "Números e o Ser" — Pitagóricos e Eleatas
3. "Os Muitos e os Átomos" — Pluralistas e Atomistas
4. "A Arte de Argumentar" — Sofistas e Sócrates
5. "O Mundo das Ideias" — Platão
6. "O Mestre de Todos" — Aristóteles
7. "Como Viver Bem?" — Era Helenística
8. "O Crepúsculo da Filosofia Antiga" — Era Imperial
9. "Fé e Razão" — Bíblia, Cristianismo e Kant

**Interface:**
- Lista de episódios com duração estimada
- Botão "Ler em Voz Alta" (usa Web Speech API para TTS nativo do browser)
- Modo leitura (tipografia otimizada, fundo sépia)
- Marcação de episódios lidos

---

## 6. Mapa de Conexões (`filosofia/conexoes.html`)

**O que é:** Visualização das influências e relações entre filósofos.

**Features:**
- Grafo interativo (canvas/SVG) com filósofos como nós
- Setas de influência (quem influenciou quem)
- Setas de oposição (quem se opôs a quem)
- Agrupamento por escola/período
- Clique em um filósofo: destaca conexões, mostra resumo
- Zoom e pan (touch-friendly)
- Legenda de cores por escola

**Dados:** ~40 filósofos com relações de influência/oposição.

---

## Estratégia de Implementação

### Passo 1: Extrair texto do docx
- Usar python-docx (já instalado) para extrair todo o texto
- Salvar como arquivo temporário de referência

### Passo 2: Criar os arquivos na ordem
1. `filosofia/index.html` (hub) — estrutura base
2. `filosofia/flashcards.html` — maior volume de dados, prioridade máxima
3. `filosofia/quiz.html` — segundo maior, reutiliza conceitos dos flashcards
4. `filosofia/timeline.html` — dados menores, mas visual importante
5. `filosofia/podcast.html` — mais texto narrativo
6. `filosofia/conexoes.html` — visualização de grafos

### Passo 3: Gerar conteúdo
Para cada arquivo, o conteúdo será gerado lendo o documento original e criando:
- Flashcards: perguntas de recall ativo baseadas nos conceitos-chave
- Quiz: questões variadas testando compreensão e memorização
- Timeline: datas e marcos extraídos do texto
- Podcast: narrativas conversacionais reorganizando o conteúdo
- Conexões: relações de influência mencionadas no texto

### Passo 4: Commit e push
- Commit na branch `claude/check-platao-access-Yy6Qt`
- Push para o remote

---

## Verificação

1. Abrir cada HTML no navegador e verificar funcionalidade
2. Testar flashcards: virar cartões, classificar, verificar persistência no localStorage
3. Testar quiz: todos os modos, verificar pontuação e explicações
4. Testar timeline: scroll, zoom, clique em filósofos
5. Testar podcast: navegação entre episódios, TTS
6. Testar conexões: interação com grafo
7. Verificar responsividade mobile
8. Verificar que hub links funcionam
9. Verificar modo escuro (se implementado)

---

## Arquivos Críticos

- **Fonte de dados:** `/home/user/Lectio/PLATÃO.docx` (extrair via python-docx)
- **Referência de design:** `/home/user/Lectio/index.html` (CSS vars, fontes, paleta)
- **Service Worker:** `/home/user/Lectio/sw.js` (atualizar cache para incluir novos arquivos)
- **Manifesto:** `/home/user/Lectio/manifest.json` (sem alteração necessária)
