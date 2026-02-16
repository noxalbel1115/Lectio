# Plano de Leitura Bíblica 2026 — Prof. Victor Sales Pinheiro

App PWA para acompanhamento do plano de leitura católica da Bíblia.

## Arquivos

```
index.html          → App principal
sw.js               → Service Worker (offline + notificações)
manifest.json       → Manifesto PWA
icons/
  icon-192.png      → Ícone 192x192
  icon-512.png      → Ícone 512x512
  icon-192-maskable.png → Ícone maskable 192x192
  icon-512-maskable.png → Ícone maskable 512x512
```

## Deploy no GitHub Pages (5 minutos)

### 1. Criar repositório

- Acesse https://github.com/new
- Nome: `lectio` (ou o que preferir)
- Marque **Public**
- Clique **Create repository**

### 2. Subir os arquivos

No computador, com Git instalado:

```bash
cd pasta-onde-extraiu-o-zip
git init
git add .
git commit -m "Plano de leitura bíblica 2026"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/lectio.git
git push -u origin main
```

**Alternativa sem Git:** No GitHub, clique em "uploading an existing file" e arraste todos os arquivos (incluindo a pasta icons/).

### 3. Ativar GitHub Pages

- No repositório, vá em **Settings** → **Pages**
- Em "Source", selecione **Deploy from a branch**
- Branch: **main**, pasta: **/ (root)**
- Clique **Save**

### 4. Acessar

Em 1-2 minutos, o app estará disponível em:

```
https://SEU-USUARIO.github.io/lectio/
```

### 5. Instalar no celular

- Abra a URL no Chrome/Safari do celular
- Chrome (Android): menu ⋮ → "Instalar app" ou "Adicionar à tela inicial"
- Safari (iPhone): ícone de compartilhar → "Adicionar à Tela de Início"

## Funcionalidades

- 365 dias de leitura (principal + paralela sapiencial)
- 22 módulos temáticos com descrição teológica
- Diário espiritual (Deus me fala / Eu falo a Deus)
- Oração de abertura (invocação ao Espírito Santo)
- Modo noturno
- Swipe entre dias
- Calendário mensal visual
- Mapa de consistência (estilo GitHub)
- Notificação diária configurável
- Funciona offline (PWA)
- Export: TXT (diário) e JSON (backup completo)
- Import: restaurar backup JSON
- Migração automática de dados do app anterior

## Créditos

Plano de leitura: Prof. Victor Sales Pinheiro
Clube de Leitura Católica da Bíblia — 2026
