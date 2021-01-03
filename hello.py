import discord
import asyncio
import os

TOKEN = os.environ.get("TOKEN")
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
            emoji = '\N{Reversed Hand with Middle Finger Extended}'
            msg = message.author.mention + " Fuck!"
        await message.add_reaction(emoji)
        await message.channel.send(msg)


client.run(TOKEN)