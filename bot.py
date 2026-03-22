import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ── Load Cogs ──────────────────────────────────────────────
async def load_extensions():
    for filename in ["moderation", "welcome", "tickets"]:
        await bot.load_extension(f"cogs.{filename}")

@bot.event
async def on_ready():
    await load_extensions()
    await bot.tree.sync()
    print(f"✅ {bot.user} is online and ready!")

bot.run(TOKEN)
