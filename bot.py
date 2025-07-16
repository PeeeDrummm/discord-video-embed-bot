import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Habilita leitura de mensagens dos usuários
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot está online como {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content
    modified = False

    # Twitter e X
    if "twitter.com" in content or "x.com" in content:
        content = content.replace("twitter.com", "vxtwitter.com")
        content = content.replace("x.com", "vxtwitter.com")
        modified = True

    # TikTok
    if "www.tiktok.com" in content:
        content = content.replace("www.tiktok.com", "www.vxtiktok.com")
        modified = True

    # Reddit
    if "www.reddit.com" in content:
        content = content.replace("www.reddit.com", "www.vxreddit.com")
        modified = True

    if modified:
        try:
            await message.delete()
            await message.channel.send(f"{message.author.mention} {content}")
        except discord.Forbidden:
            print("⚠️ Permissões insuficientes para apagar ou enviar mensagens.")

    await bot.process_commands(message)

bot.run(TOKEN)