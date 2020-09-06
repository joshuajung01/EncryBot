import os
import discord
import math
import string
from EncryptionFunctions import *
import time
from discord.ext import commands

token = "NzUxODg2ODI0NTMxNTU4NDUx.X1PnLA.ragMZmtVwpPup2ivt9UgZEaNLsI"#os.environ["DISCORD_TOKEN"]

Encrypted_Data = {}
Decrypt_Data = {}
lm_key = 0

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
    for member in ctx.guild.members:
        if member != ctx.message.author and member.voice != None:
            await ctx.message.channel.send("Communications Jammed. Communications Jammed. Communications Jammed.", tts=True)
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


@bot.command(name="assassinate", help='Assassinate your enemies!')
async def assassinate(ctx, message):
    test = False
    for member in ctx.guild.members:
        if member.nick == message:
            await member.edit(voice_channel=None)
            test = True
    if test:
        await ctx.message.delete()
        await ctx.message.channel.send(message + " died mysteriously...")
        await ctx.message.channel.send('https://media0.giphy.com/media/3owyp8HzuiWAw11OxO/giphy.gif')
    else:
        await ctx.message.channel.send("Failed assassination attempt!")
        await ctx.message.channel.send('https://i.imgur.com/eX4cyYO.gif')

@bot.command(name="meetup", help='Generate a secret location to meet up with allies: !!meetup "Sbisa" ')
async def assassinate(ctx, message=" "):
    global lm_key

    place_val = random.randint(0, 9)
    while(place_val == lm_key):  # Generate again random to reduce likehood of same image being shown twice
        place_val = random.randint(0, 9)

    locations = {"bush library": 0,
                 "evans library": 1,
                 "msc": 2,
                 "zachry": 3,
                 "quadrangle": 4,
                 "etb": 5,
                 "bright": 6,
                 "sbisa": 7,
                 "dixie chicken": 8,
                 "academic building": 9}

    if place_val == 0 and message == " ":  # Bush Library
        await ctx.message.channel.send('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/George_Bush_Presidential_Library.jpg/1200px-George_Bush_Presidential_Library.jpg')
        lm_key = 0
    elif place_val == 1 and message == " ":  # Evans Library
        await ctx.message.channel.send('https://bloximages.chicago2.vip.townnews.com/myaggienation.com/content/tncms/assets/v3/editorial/3/ed/3ed2c6a8-11ca-11e3-a54c-0019bb2963f4/5221280042426.image.jpg')
        lm_key = 1
    elif place_val == 2 and message == " ":  # MSC
        await ctx.message.channel.send('https://newsarchive.arch.tamu.edu/media/photologue/phlogphoto/cache/memory%20cloud4_galleria_large.jpg')
        lm_key = 2
    elif place_val == 3 and message == " ":  # Zachry
        await ctx.message.channel.send('https://zachry.tamu.edu/wp-content/uploads/2018/08/zach-building-july-progress-photo.jpg')
        lm_key = 3
    elif place_val == 4 and message == " ":  # Quadrangle
        await ctx.message.channel.send('https://leadbyexample.tamu.edu/images/story-newquad5.jpg')
        lm_key = 4
    elif place_val == 5 and message == " ":  # ETB
        await ctx.message.channel.send('https://th.bing.com/th/id/OIP.0rhyAu2ziSKwhix5NVL7OwHaDV?pid=Api&rs=1')
        lm_key = 5
    elif place_val == 6 and message == " ":  # Bright
        await ctx.message.channel.send('https://engineering.tamu.edu/_files/_images/_content-images/bright-building-08Jan2019.jpg')
        lm_key = 6
    elif place_val == 7 and message == " ":  # Sbisa
        await ctx.message.channel.send('https://upload.wikimedia.org/wikipedia/commons/9/9c/Sbisa.jpg')
        lm_key = 7
    elif place_val == 8 and message == " ":  # Dixie Chicken
        await ctx.message.channel.send('https://i.pinimg.com/736x/1c/25/5d/1c255d279c6cd6a06ec87d1cc2c51b08--aggie-game-college-station-texas.jpg')
        lm_key = 8
    elif place_val == 9 and message == " ":  # Academic Building
        await ctx.message.channel.send('https://www.thoughtco.com/thmb/oS9b0mb0EbtMbyrAnRpiz7_vfhw=/768x0/filters:no_upscale():max_bytes(150000):strip_icc()/texas-a-and-m-flickr-5a4853a4b39d0300372455a9.jpg')
        lm_key = 9

    elif locations.get(message.lower()) == lm_key:
        await ctx.message.delete()
        await ctx.message.channel.send(f"{ctx.message.author.nick} see you there")

    elif message.upper() == "key".upper():
        await ctx.message.channel.send("Here are the current meeting locations:\n\n"
                                   "Bush Library\n"
                                   "Evans Library\n"
                                   "MSC\n"
                                   "Zachry\n"
                                   "Quadrangle\n"
                                   "ETB\n"
                                   "Bright\n"
                                   "Sbisa\n"
                                   "Dixie Chicken\n"
                                   "Academic Building\n")

    else:
        await ctx.message.channel.send("Intruder Alert! {} is an intruder! Intruder Alert!".format(ctx.message.author.nick), tts=True)

bot.run(token, bot=True)