import discord
from discord.ext import commands
import os
import json

# Load config
with open("data/config.json") as f:
    config = json.load(f)

TOKEN = os.getenv("TOKEN")
PREFIX = config.get("prefix", "!")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Branding on startup
@bot.event
async def on_ready():
    print(f"GachaPlex is online — Created by Uzi | https://discord.gg/h5jYF4aA")
    print(f"Logged in as: {bot.user}")

# Help command with branding
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="GachaPlex Help",
        description="A feature-rich Discord bot — Created by Uzi",
        color=0xAA00FF
    )
    embed.add_field(name="Moderation", value="`ban`, `kick`, `mute`, `warn`", inline=False)
    embed.add_field(name="Fun", value="`8ball`, `avatar`", inline=False)
    embed.set_footer(text="GachaPlex — Created by Uzi | https://discord.gg/h5jYF4aA")
    await ctx.send(embed=embed)

# Load cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(TOKEN)
