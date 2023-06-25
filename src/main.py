import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

#Secrets
load_dotenv()

PREFIX = os.getenv("PREFIX")
TOKEN = os.getenv("TOKEN")

#Bot setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print("Bot started")

@bot.command(name="addquote")
async def addquote(ctx, quote = None):
    msg = ctx.message

    if quote == None:
        await msg.channel.send("You didn't add a quote dumbass")
        return
        

    print(quote)
    
bot.run(TOKEN)

