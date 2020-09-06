import os
import discord
import math
import string
from EncryptionFunctions import *
import time

token = os.environ["DISCORD_TOKEN"]
client = discord.Client()

# {Unique ID: String to encrypt}
Encrypted_Data = {}

# {Key: String to Decrypt}
Decrypt_Data = {}

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    global Encrypted_Data
    global Decrypt_Data
    if message.content.find("!!ping") != -1 and not message.author.bot:
        await message.channel.send("Pong!")

    elif message.content.find("!!encrypt") != -1 and not message.author.bot:
        try:
            ID = time.time()
            str_message = message.content
            arr = str_message.split(" ")
            str_message = arr[2]
            str_message, key = encrypt(str_message)
            Encrypted_Data[ID] = str_message
            await message.delete()
            await message.author.send(message.author.name + " is sending you a secret message: "
                                      + Encrypted_Data[ID] + "\nYour unique ID is: " + str(ID) +
                                      "\nYour key is: "+ str(key))
            await message.channel.send("Message sent")

        except Exception as e:
            if not message.author.bot:
                await message.channel.send("Bruh Error!: ")
                await message.channel.send(e)

    if message.content.find("!!decrypt") != -1 and not message.author.bot:
        try:
            arr_sent = message.content.split(' ')
            ID_decrypt = float(arr_sent[1])
            sent_key = int(arr_sent[2])
            Decrypt_Data[sent_key] = Encrypted_Data.get(float(ID_decrypt))
            # Make sure to implement decrypt with given key
            str_decrypt_msg = decrypt(str(Decrypt_Data.get(sent_key)), sent_key)
            await message.delete()
            await message.author.send("Your decrypted msg is:" + str_decrypt_msg)
            await message.channel.send("Message sent")

        except Exception as e:
            if not message.author.bot:
                await message.channel.send("Bruh Error!: ")
                await message.channel.send(e)

    elif message.content.find("!!jam") != -1 and not message.author.bot:
        try:
            await message.channel.send("SCAAAAAAAA asdfasdf asdf  Meow. Meow. Meow. Meow. :a: :a: :a: bois bois bois bois :a: :a: :a: :a: :a: :a: :a: :a:"
                                       "ASFDASFSAF a sdf asf  q @@@@@@@@ fdh sfd re  fa sfaaf lurl lurl lurl lurl lurl f ad faf assaf My ROFLCopter goes soi soi soi", tts=True)
            await message.channel.send(
                "tit twister mister blister deadly twister on daddys fister sister was fister by mister magister on testosteronsister"
                " Ooogly Gooogly Ooogly Gooogly Ooogly Gooogly ooluuu luuluu ooluu lulu ooluuu"
                "A rofl Train goes tichdvdxtche tichdvdxtche dododobobobobgjubgjubgjubdododobobobobgjubgjubgjub The lawnmower goes shersheeeeeeerrerererereeeerrr",
                tts=True)

        except Exception as e:
            if not message.author.bot:
                await message.channel.send("Bruh Error!: ")
                await message.channel.send(e)

    elif message.content.find("!!Joshua") != -1 and not message.author.bot:
        await message.channel.send("Oh he's dumb af")

    elif message.content.find("!!help") != -1 and not message.author.bot:
        #See commands to control bot
        await message.channel.send("Here are the controls for EncryBot:\n"
                                   "!!encrypt - Encrypts message and messages role member key to unlock\n" 
                                   "!!decrypt - Messages the role member the key\n"
                                   "!!help - See controls for EncryBot\n")

from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command(pass_context=True)
async def message_role(ctx, role: discord.Role, *, message):
    for member in ctx.message.server.members:
        if role in member.roles:
            await bot.send_message(member, message)
client.run(token)

