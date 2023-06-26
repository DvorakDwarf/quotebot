#TODO
#Consider slash commands
#Find other way to insert author
#Possibly date

import discord
from discord.ext import commands
import os
import random
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

#Connecting to database
try:
    connection = connect(
        host="localhost",
        user=SQL_USERNAME,
        password=SQL_PASSWORD,
        database=DATABASE,
    )
except Error as e:
    print(e)


@bot.event
async def on_ready():
    print("Bot started")


@bot.command(name="addquote")
async def addquote(ctx):
    msg = ctx.message.content[10:]

    # #32 is max discord username character limit
    # if author == None or len(author) > 32:
    #     await ctx.send("Invalid author bozo")
    #     return

    if len(msg) > MAX_QUOTE_LENGTH:
        await ctx.send("Invalid quote dumbass")
        return

    # print(author)
    #JANK, still works
    print(msg)
    insert_query = f"INSERT INTO quotes (quote) VALUES ('{msg}')"
    with connection.cursor() as cursor:
        cursor.execute(insert_query)
        connection.commit()
        cursor.execute("SELECT * FROM quotes")
        result = cursor.fetchall()
        for row in result:
            print(row)

@bot.command(name="random")
async def pick_random(ctx):
    with connection.cursor() as cursor:
        cursor.execute("SELECT quote, author FROM quotes")
        result = cursor.fetchall()
        print(result)
        print(type(result))
        # await ctx.send(random.choice(result)[0] +  " - " )
    
bot.run(TOKEN)

