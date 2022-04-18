from decouple import config
import discord
import cv2
import pytesseract

client = discord.Client()

async def somefunc(filename, message):
    try:
        img = cv2.imread(filename)
        print(pytesseract.image_to_string(img, lang= 'en'))
    except FileNotFoundError:
        await message.channel.send("Oops!")
    

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
                    if i == filename:
                        await message.channel.send("Reuse")
                        break
                else:
                    content.append(filename + '\n')                       
                    await attachment.save(filename)
                    print(attachment.content_type, attachment.url, filename)
                    with open("text.txt","w") as f:
                        f.writelines(content)
                    await somefunc(filename, message)
            # img = cv2.imread(url)
            # string = pytesseract.image_to_string(img, lang= 'en')
            # print(string)

        except AttributeError:
            await message.channel.send("Has no Image")


client.run(config('Token'))