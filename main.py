import discord
from discord.ext import commands, tasks
from discord import app_commands
import os
from datetime import datetime

token = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    print(f"✅ 봇 로그인 완료: {bot.user} (ID: {bot.user.id})")
    await tree.sync()

@tree.command(name="ping", description="퐁!을 돌려줍니다.")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("퐁!", ephemeral=True)

if token:
    bot.run(token)
else:
    print("❌ DISCORD_BOT_TOKEN 환경변수가 설정되지 않았습니다.")
