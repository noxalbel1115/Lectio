# Canal — histórias de empresas brasileiras

Preparação de 2026-11-07 no repositório `noxalbel1115/Lectio`, branch `cursor/youtube-skills-preparacao-3e0c`. Isto não é uma tarefa do Codex Cloud e não publica nada no YouTube.

## O que este projeto é

Canal de histórias de empresas brasileiras, com imagens e narração. O piloto ainda não tem empresa, duração, formato, estilo visual nem teto de gasto. Não é continuação de *A Ponte da Bondade*, nem pressupõe público infantil, animação ou 20 minutos.

O app de leitura bíblica na raiz do repositório permanece intacto. O estado fica nesta pasta, fora de `index.html`, `sw.js`, `manifest.json`, `icons/` e `README.md`.

## Skills

Três skills originais do pacote de 2026-11-06, sem skill homônima prévia no `HEAD` e sem substituição:

- `.agents/skills/youtube-producao`
- `.agents/skills/youtube-runway`
- `.agents/skills/youtube-montagem`

Os 13 arquivos conferem com o ZIP (`integridade-skills.sha256`). O índice antigo tem 405 caminhos e 1888561262 bytes declarados; os vídeos não vieram no pacote. O histórico lido foi `youtube-producao/references/historico-e-licoes.md`, igual ao anexo da conversa. O pacote ainda diz que o formato do canal novo estava indefinido em 06/11/2026; esse texto não foi reescrito. O briefing acima é o mais recente e vale só neste estado.

Carregar `youtube-runway` só ao gerar mídia no Runway e `youtube-montagem` só na edição ou revisão. Nenhuma das duas foi usada como roteiro de trabalho nesta preparação.

## Ambiente desta execução

Cursor Cloud Agent. Python 3.12.3, FFmpeg e ffprobe 6.1.1-3ubuntu5. Nenhuma variável de ambiente Runway. Nenhum crédito consultado, comprado ou gasto. A autenticação e o saldo não acompanham as skills. O saldo histórico de 258 créditos no workspace pessoal V, em 06/11/2026, precisa ser reconsultado no ambiente que for gerar mídia.

O GitHub Pages deste repositório publica a raiz de `main` com Jekyll. Não há `.nojekyll` nem `_config.yml`. Pela documentação do GitHub Pages, pastas iniciadas por ponto ficam de fora desse build. Um merge futuro não deve expor esta pasta no site público enquanto essa configuração permanecer. O merge não foi feito.

## Como levar a branch ao Codex

Consultas em 2026-11-07:

- [Codex Cloud](https://learn.chatgpt.com/docs/cloud): o início documentado é abrir o ChatGPT, escolher trabalho em nuvem, selecionar ou criar um ambiente e escolher o repositório GitHub. A página não documenta um seletor de branch.
- [Build skills](https://developers.openai.com/codex/skills): no Codex local e na extensão de IDE, a descoberta de skills de repositório percorre `.agents/skills` do diretório atual até a raiz do Git.

Caminho que a documentação sustenta:

1. Revisar o pull request. O merge em `main` é decisão posterior; sem ele, o checkout padrão do repositório não contém estas skills.
2. No Codex em IDE ou CLI, abrir o clone de `noxalbel1115/Lectio` nesta branch. As skills ficam em `.agents/skills` e podem ser chamadas com `$youtube-producao`, `$youtube-runway` e `$youtube-montagem`.
3. No Codex Cloud, selecionar o repositório `noxalbel1115/Lectio` no ambiente. Como a página de início não mostra escolha de branch, a forma verificada de o ambiente enxergar estes arquivos no checkout padrão é o merge em `main`. Não foi possível, daqui, provar que um ambiente já publicado passa a usar uma branch só porque o pull request existe.

Limite conhecido: o relato [openai/codex#52266](https://github.com/openai/codex/issues/52266), atualizado em 2026-11-03, diz que o Codex Cloud pode não listar sozinho as skills do repositório, mesmo com os arquivos no checkout. A leitura explícita de `SKILL.md` foi o contorno observado por quem abriu o relato. A presença dos arquivos neste pull request não é instalação nem ativação dentro do Codex.

## Próximo passo

Definir o piloto. Antes de geração paga, fechar um bloco que caiba no orçamento reconsultado e validar um trecho representativo. Não comprar créditos e não publicar no YouTube sem instrução explícita.
