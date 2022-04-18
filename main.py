from decouple import config
import discord
import cv2
import pytesseract

client = discord.Client()

def somefunc(filename):
    img = cv2.imread(filename)
    content = pytesseract.image_to_string(img)
    contents = content.split()
    for i in contents:
        if i == 'BOOYAH!':
            return True
    return False

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
        try:
            for attachment in message.attachments:
                filename = attachment.filename
                with open("text.txt","r") as f:
                    content = f.readlines()

                for i in content:
                    if i == filename + '\n':
                        await message.channel.send("Reuse")
                        break
                else:
                    content.append(filename + '\n')                       
                    await attachment.save(filename)
                    print(attachment.content_type, attachment.url, filename)
                    with open("text.txt","w") as f:
                        f.writelines(content)
                    val = somefunc(filename)
                    if val:
                        await message.channel.send("Booyah You Scored Points")
                    else:
                        await message.channel.send("Hmm! I couldn't find BOOYAH in the Photo")
        except AttributeError:
            await message.channel.send("Has no Image")


client.run(config('Token'))