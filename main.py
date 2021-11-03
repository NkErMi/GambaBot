#
# 1. MAKE SURE USERS CANNOT GAMBLE MORE THAN USER HAS - TJEK
# 2. MAKE A BETTER MESSAGE THAT TELLS HOW MUCH USER HAS TOTAL AFTER GAMBLING - TJEK
# 3. MAKE A ADD FUNCTION
# 4. MAKE A MAX AMOUNT THEY CAN ADD
# 5. MAKE THEY HAVE TO ADD MORE THAN 0
# 6. INVESTIGATE HOW THE BOT CAN MAKE SOUND

# OTAyMjQ2MzY1ODAxODg5ODYy.YXboaA.seK0SNH9OMn22hGVLsCP9jOKH3k
import discord
from gamba_service import GambaService
gs = GambaService()


# GAMBLING BIKS
# 1. COMMAND TO JOIN - SAVE USER IN A LIST
# 2. COMMAND TO GAMBLE MONEY

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is running')

@client.event
async def on_message(message):
    print(message)
    print(message.author.name)
    print(message.content)
    print(message.author.id)

    # If the author of the message is our bot then dont do anything aka return
    if message.author == client.user:
        return

    if not message.content.startswith('$'):
        return

    if message.content == '$join':
        gs.new_user(message.author.id, message.author.name)
        await message.channel.send(message.author.name + ' has joined the gambling')

    if message.content == '$status':
        status = gs.get_status(message.author.id)
        await message.channel.send(status)

    if message.content.startswith('$gamble'):
        result = gs.gamble(message.author.id, message.content)
        await message.channel.send(result)

    if message.content.startswith('$add'):
        add = gs.add(message.author.id, message.content)
        await message.channel.send(add)






client.run('OTAyMjQ2MzY1ODAxODg5ODYy.YXboaA.seK0SNH9OMn22hGVLsCP9jOKH3k')