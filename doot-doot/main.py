import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import datetime
import sys
import traceback

import logging

# Preparing the cogs
initial_extensions = [
    'airhorn',
    'basics'
]

# setting up logger
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord-bot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# prefix, description that appear in !help
client = Bot(description="dooting on the haters", command_prefix="!", pm_help=False)

# Adding the cogs to the bot
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(f"cogs.{extension}")
        except Exception as e:
            print(f"error occured while loading cog")
            print(traceback.format_exc())

# start of bot and event for config


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} (ID:{client.user.id}) | Connected to {len(client.guilds)} servers')
    await client.change_presence(activity=discord.Game(name='Dooting on the haters'))

client.run(token)
