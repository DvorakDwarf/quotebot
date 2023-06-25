import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from mysql.connector import connect, Error

#Secrets
load_dotenv()

PREFIX = os.getenv("PREFIX")
TOKEN = os.getenv("TOKEN")
MAX_QUOTE_LENGTH = int(os.getenv("MAX_QUOTE_LENGTH"))
SQL_USERNAME = os.getenv("SQL_USERNAME")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
DATABASE = os.getenv("DATABASE")

#Bot setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print("Bot started")

    #Connecting to database
    try:
        with connect(
            host="localhost",
            user=SQL_USERNAME,
            password=SQL_PASSWORD,
            database=DATABASE,
        ) as connection:
            print(connection)
    except Error as e:
        print(e)



@bot.command(name="addquote")
async def addquote(ctx, author = None, quote = None):
    #32 is max discord username character limit
    if author == None or len(author) > 32:
        await ctx.send("Invalid author bozo")
        return

    if quote == None or quote > MAX_QUOTE_LENGTH:
        await ctx.send("Invalid quote dumbass")
        return


    print(quote)

@bot.command(name="random")
async def random(ctx):
    pass
    
bot.run(TOKEN)

