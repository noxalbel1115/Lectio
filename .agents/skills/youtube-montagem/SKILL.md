---
name: youtube-montagem
description: Montar e revisar vídeos de YouTube com Python e FFmpeg, reaproveitando clipes e áudio e verificando exportação e continuidade.
---

# Montagem e revisão

Trabalhe no runtime disponível, local ou na nuvem. Confira Python, FFmpeg e ffprobe. Um computador remoto dependente do Mac ligado não atende a execução autônoma com o Mac desligado.

## Montar

- Leia timeline e seleção do bloco, não todos os históricos do provedor. Registre por plano: fonte, entrada, duração aproveitada, duração editorial e ordem; registre trilhas/níveis separadamente.
- Preserve fontes/versões; escreva derivados em uma pasta de versão. Reuse receita existente quando resolver; ajuste configuração em vez de reescrever a edição inteira.
- Resolva caminhos pela raiz do projeto/script, não por `/Users/...`. Regenere listas de concatenação com caminhos absolutos antigos.
- Faça trim, cortes, reenquadramento e retiming com FFmpeg. Normalize FPS, dimensões, proporção de pixel e formato de cor conforme o alvo escolhido. Não imponha 720p/24 fps a todo vídeo: esses eram parâmetros do projeto antigo.
- Concatene sem recodificar vídeo só quando parâmetros e timestamps forem compatíveis; caso contrário normalize segmentos. Confira duração efetiva: AAC pode acrescentar milissegundos ao contêiner.
- Preserve música e ambiente separados; aplique fades e mixagem reproduzível. Evite regenerar áudio quando edição ou loop natural servirem.
- Use codecs compatíveis com o destino e `+faststart` em MP4 quando pertinente. Espere a renderização terminar antes de anunciar conclusão.

## Verificar com saída compacta

Execute `scripts/inspecionar_video.py` desta skill com o vídeo. Resume metadados em JSON; `--decode` testa decodificação completa; `--amostras DIRETORIO` extrai quadros em 10%, 50% e 90%; `--saida RELATORIO.json` persiste o resultado. Não faz geração paga nem análise visual automática.

- Confira duração, dimensões, FPS, codec e áudio. Faça decodificação completa da entrega final; não repita por mudança de texto sem motivo.
- Inspecione amostras e, adicionalmente, contatos difíceis, deformações conhecidas e pontos de corte. Três quadros não cobrem cada plano de um filme longo.
- Confira níveis e escute o áudio disponível. Distinga amostragem, validação técnica e revisão humana integral; não anuncie revisão que não aconteceu.
- Faça galeria se facilitar a revisão, com uma versão simples por entrega. Localhost pertence ao runtime em que foi aberto, não é endereço público.

Leia [receitas-e-limites.md](references/receitas-e-limites.md) ao reaproveitar a abertura/bloco 02 de “A Ponte da Bondade”. Execute os scripts antigos só com a hierarquia esperada de mídia. Preserve esses vídeos ao iniciar outro projeto.
