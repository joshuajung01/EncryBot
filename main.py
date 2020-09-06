import os
import discord
import math
import string
from EncryptionFunctions import *
import time
from discord.ext import commands

token = os.environ["DISCORD_TOKEN"]

Encrypted_Data = {}
Decrypt_Data = {}

bot = commands.Bot(command_prefix="!!")


@bot.command(name="encrypt", help='Send encrypted messages: !!encrypt @role "message goes here" ')
async def encrypt(ctx, role: discord.Role, message):
    global Encrypted_Data

    ID = time.time()
    messageText, key = encrypter(message)
    Encrypted_Data[ID] = messageText

    await ctx.message.delete()

    for member in ctx.guild.members:
        if role in member.roles or member.name == ctx.message.author.name:
            await member.send(ctx.message.author.name + " is sending you a secret message: "
                              + Encrypted_Data[ID] + "\nYour unique ID is: " + str(ID) +
                              "\n Your key is: " + str(key))


@bot.command(name="decrypt", help='Send decrypted messages: !!decrypt 1234 1')
async def decrypt(ctx, id, key):
    global Encrypted_Data
    global Decrypt_Data
    id = float(id)
    key = int(key)
    Decrypt_Data[key] = Encrypted_Data.get(id)
    await ctx.message.delete()
    decryptedMsg = decrypter(str(Decrypt_Data.get(key)), key)
    await ctx.message.author.send("Here is your decrypted Message: \n" + decryptedMsg)


@bot.command(name="jam", help='Send decrypted messages: !!decrypt 1234 1')
async def jam(ctx):
    ctx.message.author
    for member in ctx.guild.members:
        if member != ctx.message.author and member.voice != None:
            await member.edit(mute=True)


@bot.command(name="grapple", help='Grapple to other voice channels: !!grapple channel_name')
async def grapple(ctx, message):
    channel = discord.utils.get(ctx.guild.voice_channels, name=message, bitrate=64000)
    await ctx.message.author.edit(voice_channel=channel)
    await ctx.message.channel.send(ctx.message.author.name + " is grappling to channel " + message + "!!")
    await ctx.message.channel.send("https://i.pinimg.com/originals/7f/d1/c5/7fd1c5f2e65b37aae2d9d8277c1944d9.gif")

@bot.command(name="self-destruct", help='Self-Destruct!')
async def self_destruct(ctx):
    channel = discord.utils.get(ctx.guild.voice_channels, name="asdgasgasdg", bitrate=64000)
    await ctx.message.author.edit(voice_channel=channel)
    await ctx.message.channel.send(ctx.message.author.name + " has self-destructed !!")
    await ctx.message.channel.send("https://media1.giphy.com/media/oe33xf3B50fsc/giphy.gif")

bot.run(token, bot=True)
