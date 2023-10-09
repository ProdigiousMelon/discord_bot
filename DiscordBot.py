import discord
import os
import asyncio
import requests
from os.path import join, dirname
from dotenv import load_dotenv

#load enviroment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#user variables
stream_chan_name = 'streaming-promo'
message = "is streaming!!! if it's me, i promise it's a bot and not me talking in the third person..."
streamers = ['Lagopotomus']



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

#message user stream start
async def 

client.run(os.getenv('DISCORD_TOKEN'))