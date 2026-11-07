---
name: youtube-producao
description: Planejar e conduzir uma produção de vídeo para YouTube com orçamento, continuidade e contexto enxuto; usar ao iniciar um vídeo ou retomar sua produção.
---

# Produção para YouTube

Conduza o vídeo solicitado até uma entrega revisável. Vídeo novo começa em pasta própria; “A Ponte da Bondade” é referência de método, não obrigação de repetir público, estética, duração ou ausência de falas.

## Começar ou retomar

- Reaproveite o briefing já dado. Pergunte somente o que muda a produção: tema/público, duração/formato, linguagem visual, uso de voz e limite de gasto quando houver geração paga relevante. Agrupe dúvidas essenciais.
- Descubra ferramentas e arquivos presentes no ambiente atual. Skills não transferem conectores ou credenciais. Caminhos `/Users/...` e endereços `127.0.0.1` do Mac não dão acesso à nuvem.
- Para aprender com o trabalho anterior, leia [historico-e-licoes.md](references/historico-e-licoes.md). Para identificar serviços anteriormente disponíveis, consulte [integracoes.md](references/integracoes.md); confirme só os necessários ao vídeo atual.
- Para localizar arquivos antigos, execute `scripts/consultar_caminhos.py` desta skill com palavras do nome. O índice contém os 405 arquivos originais, caminhos absolutos e relativos. `--root` mapeia uma cópia transferida. Não despeje o índice inteiro no contexto.

## Produzir com economia

1. Defina intenção e acontecimentos antes de gerar mídia. Faça decupagem suficiente para o bloco atual; detalhe planos futuros quando necessário.
2. Crie referências de personagem/cenário/objetos com uso previsto. Evite fichas, galerias e variantes sem função na entrega.
3. Valide um trecho representativo antes de multiplicar a técnica por minutos. Avalie se estilo e ação funcionam, além do sucesso técnico da ferramenta.
4. Use `youtube-runway`, se disponível, na geração pelo Runway; use `youtube-montagem`, se disponível, na edição com FFmpeg. Carregue cada skill só na etapa correspondente. Sem elas, execute o fluxo com as ferramentas presentes.
5. Preserve fontes; reaproveite cortes, trilha e ambiente. Respeite o formato escolhido: animação de personagem não equivale a fotografia com zoom.
6. Mantenha um `estado-producao.json` pequeno: briefing vigente, versão, entregas, último plano concluído, tarefas pendentes com IDs, gastos confirmados, limitações e próximo passo. Não replique a conversa inteira em cada checkpoint.

## Contexto e tokens

- Leia primeiro o estado, depois só os trechos necessários. Use busca e extração seletiva de JSON; não carregue todos os logs para achar um caminho.
- Na descoberta de ferramentas, filtre por serviço/ação e obtenha apenas os esquemas necessários. Evite catálogos completos, respostas enormes e URLs repetidas no contexto.
- Guarde retornos brutos quando necessários à rastreabilidade, mas passe ao modelo resumo com ID, estado, custo, arquivo e erro relevante. Evite snapshots cumulativos das mesmas respostas.
- Agrupe leituras/consultas independentes; mantenha dependências e mutações em ordem. Não refaça downloads, leituras ou gerações concluídas sem motivo demonstrado.
- Use scripts para contagens, nomes, duração, montagem e validação. Não reescreva receitas estáveis a cada vídeo nem use raciocínio do modelo para cálculo determinístico.
- Informe mudanças materiais, resultados e bloqueios reais. Evite narrativa extensa de operações e galerias novas a cada tentativa.
- Diferencie tokens do assistente, créditos do provedor e processamento de edição. Este pacote não contém medição histórica de tokens; não invente percentuais de economia.

## Modelos e entrega

Se o usuário pedir escolha de modelo e effort, pesquise o estado atual na web antes de recomendar. Consulte fontes oficiais sobre disponibilidade, preços, esforços e notas da Anthropic conforme a instrução do usuário; inclua OpenAI se comparar Codex e o provedor de mídia pertinente. Cite fontes e data. Modelos históricos não são recomendação atual.

Entregue arquivos/links utilizáveis, duração e parâmetros confirmados, custo conhecido e limites da revisão. Publicar no YouTube exige instrução do usuário; planejar um canal ou produzir um arquivo não autoriza publicação.
