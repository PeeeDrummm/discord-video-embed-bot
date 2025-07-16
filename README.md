# 🤖 Discord Auto-Embed Bot (Twitter, TikTok, Reddit)

Um bot simples para Discord que transforma automaticamente links de redes sociais em versões com embed (visualização direta), como `vxtwitter.com`, `www.vxtiktok.com` e `www.vxreddit.com`.

---

## 📌 O que o bot faz?

Sempre que um usuário enviar um link de:

- **Twitter ou X** → substitui por `https://vxtwitter.com/...`
- **TikTok** → substitui por `https://www.vxtiktok.com/...`
- **Reddit** → substitui por `https://www.vxreddit.com/...`

O bot apaga a mensagem original e reenvia a nova com o link convertido, mencionando o autor.

---

## 🛠️ Tecnologias

- Python `3.8+`
- [discord.py](https://github.com/Rapptz/discord.py)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 🚀 Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/PeeeDrummm/discord-video-embed-bot.git
cd discord-video-embed-bot
````

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure seu arquivo `.env`

Crie um arquivo `.env` na raiz do projeto com o conteúdo:

```
DISCORD_TOKEN=seu_token_aqui
```

> ⚠️ **Nunca compartilhe esse token publicamente.**

### 4. Execute o bot

```bash
python bot.py
```

---

## 🔐 Criar bot no Discord + Obter o token

1. Vá para [https://discord.com/developers/applications](https://discord.com/developers/applications)

2. Clique em **"New Application"**

   * Dê um nome e clique em **"Create"**

3. Vá em **"OAuth2 > URL Generator"**

   * Marque:

     * ✅ `bot` em **Scopes**
     * ✅ `Send Messages`, `Read Message History` e `Manage Messages` em **Bot Permissions**
     * ✅ `Guild Install` para facilitar o convite ao servidor
   * Copie o link gerado para convidar o bot ao seu servidor

4. Vá em **"Bot"**

   * Ative: ✅ `Message Content Intent`
   * (Opcional) Ative apenas se necessário: `PRESENCE INTENT` e `SERVER MEMBERS INTENT`
   * Em **Bot Permissions**, certifique-se de marcar:

     * ✅ `Send Messages`
     * ✅ `Read Message History`
     * ✅ `Manage Messages`
   * Clique em **"Reset Token"** (ou "Copy Token", se for a primeira vez)

     * Confirme clicando em **“Yes, do it!”**
   * Cole esse token no seu `.env`

---

## 📜 Permissões necessárias no servidor do Discord

* ✅ Ler mensagens
* ✅ Enviar mensagens
* ✅ Gerenciar mensagens (para apagar as originais)

Essas permissões devem estar ativas tanto nas configurações globais do bot quanto nos canais em que ele atuará.

---

<p align="center">
  <img src="https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif" width="60"/><br>
  Feito com ❤️ por <a href="https://github.com/PeeeDrummm">Pedro Afonso</a>
</p>