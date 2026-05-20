import os
import discord
from discord.ext import commands

TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"=================================")
    print(f"🎉 SUCCESS! {bot.user} is now ACTIVE!")
    print(f"=================================")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓 I am currently working perfectly! Command success🎉.")

bot.run(TOKEN)
