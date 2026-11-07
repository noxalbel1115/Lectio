---
name: youtube-runway
description: Produzir imagens, planos de vídeo e áudio no Runway para um vídeo de YouTube, controlando continuidade, tarefas assíncronas e créditos.
---

# Planos no Runway

Use na geração de mídia solicitada; carregar a skill não inicia gerações por si só.

## Antes de gerar

- Confirme conexão, workspace, modelos utilizáveis e saldo com a ação de identidade do Runway se ainda não houver confirmação pertinente nesta sessão. Cota do Codex não é saldo do Runway.
- Consulte só as ferramentas necessárias à modalidade. Siga as instruções atuais do conector e carregue uma skill do próprio Runway quando ele exigir para a tarefa.
- Reaproveite referências e tarefas existentes. Reutilize URLs de assets válidos sem novo upload. Arquivos locais precisam do upload aceito pelo conector; um caminho local não é URL pública.
- Calcule o custo do bloco usando preços atuais, incluindo imagens, vídeos, áudio e margem proporcional de correção. Compare com saldo e limite autorizado. Se não couber, apresente bloco menor ou outro formato para escolha; não compre créditos.
- Preserve o modelo expressamente solicitado. Ao recomendar modelo/effort, faça a pesquisa atual pedida pelo usuário, sem seguir cegamente tabelas históricas.

## Construir um plano estável

- Use imagem inicial de cena revisada. Ficha com múltiplas vistas serve para criar a cena, não como quadro inicial da animação.
- Fixe identidade, escala relativa, lado dos acessórios, quantidade de objetos, apoio de patas/mãos e geografia. Confira só os invariantes relevantes à ação.
- Descreva uma ação principal por plano: intenção, movimento, câmera e elementos estáveis. Divida contatos complexos em cortes legíveis.
- Prefira retoque específico quando resolver. Se a mesma correção não progride, mude composição/método ou relate a limitação; não repita indefinidamente gerações pagas.
- No projeto antigo, olhos extras do caracol, hastes do carrinho, contagem de alimentos e lado da bolsa falharam. São exemplos de continuidade, não regras de conteúdo para todo vídeo novo.

## Tarefas, revisão e economia

- Registre por asset/plano: ID editorial, tipo, task ID, referência, modelo, estado, URL/arquivo, custo confirmado ou estimado e decisão de uso. Preserve prompts finais sem replicar retornos aninhados em cada atualização.
- Após submissão aceita, acompanhe o task ID. Timeout/resposta perdida não comprovam falha: reconcilie antes de reenviar uma geração paga.
- Siga viewer e política de polling do conector. Se o viewer acompanha sozinho, não faça consultas paralelas; caso precise consultar, peça só tarefas pendentes.
- Faça lotes pequenos independentes depois de validar o trecho representativo. Confira cada resultado; falha em um item não exige refazer o lote inteiro.
- Antes de repetir uma geração, tente trim, reenquadramento, corte de reação ou elipse que preserve a compreensão. Uma nova geração só para mudar ângulo pode ser dispensável.
- Aproveite intervalos diferentes de um clipe para ações distintas; não repita o mesmo trecho como movimento novo. Retiming moderado pode funcionar: confira o resultado.
- Inspecione amostras de ação, anatomia, interação e cortes. Metadados válidos não comprovam qualidade visual.
- Mantenha música e ambiente separados/reutilizáveis. Um novo trecho não exige nova música se a anterior cumpre a intenção.

## Encerrar o bloco

Reconcilie tarefas aceitas, assets usados e gastos, incluindo tentativas rejeitadas. Preserve versões substituídas fora da seleção final. Entregue ao editor lista de fontes, trechos aproveitáveis e ressalvas, sem exigir leitura de todos os logs.

Leia [economia-observada.md](references/economia-observada.md) apenas se exemplos reais ajudarem a decisão atual. Seus valores são históricos.
