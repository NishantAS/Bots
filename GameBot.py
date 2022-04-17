import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Hello World')

@client.event
async def on_message(message):
    if message.author == client.users:
        return

    msg = message.content
    if msg.startswith('Hi'):
        await message.channel.send("Hello")
    elif msg == "CheckBooyah":
        await message.channel.send("Works")
        if message.embeds is not discord.Embed.Empty:
            await message.channel.send("Has embeds")
            print(message.embeds.image.url)
        else:
            await message.channel.send("Has no embeds")


client.run("OTY0NTMyNDI5NDI1NjM5NDc1.YlmA0w.9wJJTF9Aqt7QCXsEANisJHGG7pM")