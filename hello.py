import discord
import asyncio
import os

TOKEN = os.getenv('TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print('login succeed!')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    if message.author != client.user:
        if message.content == "/hi":
            msg = message.author.mention + "Fuck!"
        await message.channel.send(msg)


client.run(TOKEN)