import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging

# --- Configuração Inicial ---
# Carrega variáveis do arquivo .env para segurança
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Configura um sistema de logging para melhor depuração
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s: %(message)s')

# Habilita as intents necessárias para o bot ler mensagens
intents = discord.Intents.default()
intents.message_content = True

# --- Estrutura do Bot ---
# Define o prefixo e as intents para o bot
bot = commands.Bot(command_prefix="!", intents=intents)

# --- Classe (Cog) para Organização ---
class LinkReplacer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.domain_map = {
            "twitter.com": "vxtwitter.com",
            "x.com": "vxtwitter.com",
            "www.tiktok.com": "www.vxtiktok.com",
            "www.reddit.com": "www.vxreddit.com",
            "www.instagram.com": "www.ddinstagram.com",
        }

    # @commands.Cog.listener() - Decorador para eventos dentro de um Cog
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # Ignora mensagens enviadas pelo próprio bot para evitar loops
        if message.author.bot:
            return
        await self.bot.process_commands(message)
        if message.content.startswith(self.bot.command_prefix):
            return

        content = message.content
        modified = False

        for original, replacement in self.domain_map.items():
            if original in content:
                content = content.replace(original, replacement)
                modified = True
        
        if modified:
            try:
                # Deleta a mensagem original do usuário
                await message.delete()
                # Envia a mensagem corrigida mencionando o autor
                await message.channel.send(f"Link corrigido por {message.author.mention}:\n{content}")
                logging.info(f"Link de {message.author} substituído no canal {message.channel}.")
            except discord.Forbidden:
                # Erro específico se o bot não tiver permissão
                logging.warning(f"Permissões insuficientes no canal '{message.channel}' do servidor '{message.guild}'. Não foi possível apagar ou enviar a mensagem.")
            except discord.HTTPException as e:
                # Outros erros relacionados à API do Discord
                logging.error(f"Erro de HTTP ao processar mensagem: {e}")

# --- Eventos Principais do Bot ---
@bot.event
async def on_ready():
    """
    Evento disparado quando o bot está online e pronto.
    """
    print("---")
    print(f"✅ Bot está online como {bot.user}")
    print(f"ID do Bot: {bot.user.id}")
    print("---")
    # Carrega o Cog que criamos
    await bot.add_cog(LinkReplacer(bot))


# --- Ponto de Entrada ---
if __name__ == "__main__":
    if TOKEN is None:
        print("❌ ERRO: O token do Discord não foi encontrado. Verifique seu arquivo .env.")
    else:
        bot.run(TOKEN)
