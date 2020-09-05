# import os
<<<<<<< HEAD
<<<<<<< HEAD
# import discord discord
=======
# import discord discord discord discord
>>>>>>> 02f44e646fdfafd366eda1d78a4ff9a9e1b2dac6
=======
# import discord discord discord discord discord
>>>>>>> 9c44a1c32a49d2849f06d7163a7b648aef873526
#
# token = os.environ["DISCORD_TOKEN"]
# client = discord.Client()
# waitlist = {}
#
# def findTeamValue(team):
#     """
#     Finds the sum of the "value" of all team members on teh team
#     """
#     value = 0
#     for member in team:
#         value += float(team[member])
#
#     return value
#
#
# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')
#
#
# @client.event
# async def on_message(message):
#     """This method will deal with all messages in the server"""
#
#     global waitlist
#
#     if message.content.find("!!show queue") != -1 and not message.author.bot:
#         # To see who is registered in the queue
#         try:
#             queue = "These are the people in the queue:"
#             if len(waitlist) == 0:
#                 await message.channel.send("There is no one in the queue")
#             else:
#                 for member in waitlist:
#                     queue += "\n" + member
#                 await message.channel.send(queue)
#         except:
#             if not message.author.bot:
#                 await message.channel.send("Unable to show who is in the queue")
#
#
#
#     elif message.content.find("!!register") != -1 and not message.author.bot:
#         # To register in the game
#         try:
#             if len(waitlist) < 11:
#                 if message.author.name in waitlist:
#                     await message.channel.send(
#                         str(message.author.mention) + " is already registered\nRegistration Denied")
#                 else:
#                     arr = str(message.content).split(" ")
#                     if len(arr[1]) < 4 and arr[1].isalnum() and arr[2].isdigit():
#                         waitlist[str(message.author.name)] = (arr[1], arr[2])
#                         await message.channel.send(str(message.author.mention) + " you are registered")
#                     else:
#                         await message.channel.send(
#                             str(message.author.mention) + "Something went wrong please try again\nEx: !register s1 67")
#             else:
#                 await message.channel.send(
#                     "Sorry, " + str(message.author.mention) + "there are already 10 people registered to play")
#         except:
#             await message.channel.send(
#                 "Invalid command\nFormat: !!register Rank LP\n\nEx: !!register g4 50\nRegister as a Gold 4 50 LP player")
#
#
#
#     elif message.content.find("!!unregister") != -1 and not message.author.bot:
#         # To remove yourself from the game
#         try:
#             for member in waitlist:
#                 if str(message.author.name) == member:
#                     waitlist.pop(member)
#                     await message.channel.send(str(message.author.mention) + " you have been successfully unregistered")
#                     break
#         except:
#             if not message.author.bot:
#                 await message.channel.send("Unable to remove from registration")
#
#     elif message.content.find("!!make teams") != -1 and not message.author.bot:
#         # Makes evenly balanced teams and resets the queue
#         team1 = {}
#         team2 = {}
#
#         arr = []
#
#         for member in waitlist:
#             arr.append(member)
#
#         for num in range(len(arr) - 1, 0, -1):
#             for i in range(num):
#                 if findValue(waitlist[arr[i]]) > findValue(waitlist[arr[i + 1]]):
#                     temp = arr[i]
#                     arr[i] = arr[i + 1]
#                     arr[i + 1] = temp
#
#         for member in arr:
#             if findTeamValue(team1) < findTeamValue(team2) and len(team1) < 5:
#                 team1[member] = findValue(waitlist[member])
#             elif len(team2) < 5:
#                 team2[member] = findValue(waitlist[member])
#
#         team1list = "Team 1:"
#         for member in team1:
#             team1list += "\n" + member
#
#         team2list = "\n\nTeam 2:"
#         for member in team2:
#             team2list += "\n" + member
#
#         await message.channel.send(team1list + team2list)
#
#         await message.channel.send("\n\nGood luck, and may the best team win!")
#         waitlist = {}
#
#     if message.content.find("!!remove") != -1 and not message.author.bot:
#         # To remove people in the queue. Must be an administrator in the guild
#         try:
#             # if message.author.server_permissions.administrator:
#             arr = str(message.content).split(" ")
#             removedName = arr[1]
#             if removedName in waitlist:
#                 for member in waitlist:
#                     if removedName == member:
#                         waitlist.pop(member)
#                         await message.channel.send(
#                             str(message.author.mention) + " you have been successfully removed " + removedName)
#                         break
#             else:
#                 await message.channel.send(
#                     str(message.author.mention) + " " + removedName + " is not registered to play in the custom game.")
#             # else:
#             #     await message.channel.send(str(message.author.mention) + " Removing specific people is only availible for administrators.")
#         except:
#             if not message.author.bot:
#                 await message.channel.send("Unable to remove player.")
#
#     if message.content.find("!!clear") != -1 and not message.author.bot:
#         # To clear the queue. Must be an administrator in the guild
#         try:
#             # if message.author.server_permissions.administrator:
#             waitlist = {}
#             await message.channel.send(
#                 str(message.author.mention) + " Registration for the custom game has been cleared.")
#             # else:
#             #     await message.channel.send(str(message.author.mention) + " Clearing registration is only availible for administrators.")
#         except:
#             if not message.author.bot:
#                 await message.channel.send("Unable to clear.")
#
#     elif message.content.find("!!help") != -1 and not message.author.bot:
#         # To see the commands to control the bot
#         await message.channel.send("Here are the commands to control TeamBalanceBot:\n"
#                                    "!!register - Register to play in the custom game\n"
#                                    "!!unregister - Remove yourself from the custom game\n"
#                                    "!!remove - Allow administrators to remove a person from the custom game\n"
#                                    "!!clear - Allow administrators to clear the registration board\n"
#                                    "!!show queue - Shows who is registered to play in the custom game\n"
#                                    "!!make teams - Makes the two balanced teams for the custom game\n"
#                                    "!!help - See the commands to control TeamBalanceBot\n")

