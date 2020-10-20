import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

#welcoming new members
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')
    print(f"sent message to new member {member.name}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.name == "jerry_testing":
        response = "fuck you"
        await message.channel.send(response)
    if message.content == '99!':
        print(message.author)
        response = f"{message.author} 99 laughs"
        await message.channel.send(response)

client.run(TOKEN)