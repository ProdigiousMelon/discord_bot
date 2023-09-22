import discord
import os
from os.path import join, dirname
from dotenv import load_dotenv

#load enviroment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#load discord api instance
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#login success response
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#message response test
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('DISCORD_TOKEN'))