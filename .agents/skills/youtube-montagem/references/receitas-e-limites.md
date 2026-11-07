# Receitas originais e portabilidade

Raiz local: `/Users/valterdomingosdeandradejunior/Documents/ChatGPT/Youtube 2/output/a-ponte-da-bondade/`.

## Abertura

- `animacao-v2/montagem/montar.py`: doze planos de onze clipes, trim/retiming, crop do segundo intervalo do clipe 04, normalização 1280×720/24 fps, concatenação, mixagem e timeline de 120 s.
- `animacao-v2/montagem/verificar.py`: validação específica da abertura.
- `animacao-v2/montagem/linha-do-tempo.json`: seleção efetivamente usada.
- `animacao-v2/montagem/abertura-2min.mp4` e `abertura-2min-sem-trilha.mp4`: entregas.
- `animacao-v2/montagem/servir.py`: servidor HTTP Range, porta 8743.

## Bloco 02

- `filme-v3/bloco-02/montagem/montar.py`: quinze planos, preferência por fontes v2 disponíveis, trim dos planos 09 e 15, mixagem e junção com abertura. Renderiza bloco de 180 s e prévia acumulada de 300 s.
- `filme-v3/bloco-02/montagem/baixar.py`: baixa URLs dos registros e preserva arquivos existentes com mais de 1000 bytes. Tamanho era uma heurística, não prova de integridade; confira metadados/decodificação. URLs antigas podem expirar.
- `filme-v3/bloco-02/montagem/revisar.py`: pranchas por amostragem, sem alterar fontes.
- `filme-v3/bloco-02/montagem/linha-do-tempo.json`: fontes, intervalos e duração editorial.
- `filme-v3/bloco-02/montagem/bloco-02-encontrar-e-escolher.mp4`: novo bloco.
- `filme-v3/bloco-02/montagem/a-ponte-da-bondade-primeiros-5min.mp4`: prévia mais avançada encontrada.
- `filme-v3/montagem/servir.py`: galeria, porta 8744. URL histórica: `http://127.0.0.1:8744/bloco-02/galeria.html`.

Scripts originais calculam caminhos pela própria localização e esperam a hierarquia de mídia. Copiar só o script quebra essas dependências. Regenere listas de concatenação com caminhos absolutos antigos. Localhost da nuvem não acessa servidor no Mac.

Relatório antigo: decodificação sem erros; vídeo 300 s, contêiner cerca de 300,021 s; H.264, AAC estéreo 48 kHz; média −18,8 dBFS/pico −2,5 dBFS. Não são LUFS nem comprovação de escuta integral.

O script portátil `inspecionar_video.py` desta skill resume metadados, extrai amostras e testa decodificação opcionalmente. Não monta o filme nem substitui julgamento visual/humano.
