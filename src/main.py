#TODO
#Possibly date

import discord
from discord import app_commands
from discord.ext import commands
import os
import random
from dotenv import load_dotenv
from mysql.connector import connect, Error

#Load secrets in .env (you need to make one)
load_dotenv()

PREFIX = os.getenv("PREFIX")
TOKEN = os.getenv("TOKEN")
MAX_QUOTE_LENGTH = int(os.getenv("MAX_QUOTE_LENGTH"))
SQL_USERNAME = os.getenv("SQL_USERNAME")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_TABLE = os.getenv("SQL_TABLE")

#Bot setup
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

#Connecting to database
#Arguably the bot should exit if this fails
try:
    connection = connect(
        host="localhost",
        user=SQL_USERNAME,
        password=SQL_PASSWORD,
        database=DATABASE,
    )
except Error as e:
    print(e)
    os._exit(os.EX_UNAVAILABLE)

@client.event
async def on_ready():
    await tree.sync()
    print("Bot started")

#It's the 21st century, we use slash commands

#This one adds a quote with an author to the database
@tree.command(name="addquote", description="Adds a quote to the database so it can be displayed on the website")
async def add_quote(interaction, author: str, quote: str):

    #32 is max discord username character limit
    if len(author) > 32:
        await interaction.response.send_message("Long author name bozo")
        return

    #Make sure people don't overflow anything
    if len(quote) > MAX_QUOTE_LENGTH:
        await interaction.response.send_message("Long quote dumbass")
        return

    #The SQL, ew
    insert_query = f"INSERT INTO {SQL_TABLE} (quote, author) VALUES ('{quote}', '{author}')"
    with connection.cursor() as cursor:
        cursor.execute(insert_query)
        connection.commit()

    await interaction.response.send_message("Quote succesfully saved")

#Pick a random quote and send it in chat
#Potentially expand to being able to pick quotes
@tree.command(name="randomquote", description="Sends a random server quote")
async def pick_random(interaction):
    with connection.cursor() as cursor:
        cursor.execute("SELECT quote, author FROM {SQL_TABLE}")
        result = random.choice(cursor.fetchall())

        quote = result[0]
        author = result[1]

        #Change up formatting if you like
        await interaction.response.send_message(quote + f" - {author}")
    
client.run(TOKEN)

