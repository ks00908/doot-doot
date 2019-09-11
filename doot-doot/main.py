import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
from datetime import datetime
import sys
import traceback

import logging

#setting up configuration
import json

def getConfig(path):
    configFile = open(path, "r")
    return json.loads(configFile.read())

config = getConfig("config.json")

# Preparing the cogs
initial_extensions = [
    'airhorn',
    'basics',
    'jishaku',
    'fun'
]

# setting up logger
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord-bot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# prefix, description that appear in !help
client = Bot(description="dooting on the haters | The Soundboard | 1 in 100 chance to be rickrolled for free when using bot!", command_prefix="Db.", pm_help=False)

# Adding the cogs to the bot
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension("cogs." + extension)
        except Exception as e:
            print(f"error occured while loading cog")
            print(traceback.format_exc())

# loading special extension for Eval
client.load_extension('jishaku')

#initiation of bot and logging in
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} (ID:{client.user.id}) | Connected to {len(client.guilds)} servers')
    await client.change_presence(activity=discord.Game(name='Dooting on the haters | Prefix is D. | for list of commands use D.help'))

@client.event
async def on_guild_join(guild):
 logschannel = config['log_channel']
 guildid = str(guild.id)
 ownerid = str(guild.owner)
 guildname = str(guild.name)
 channel = client.get_channel(logschannel)
 embed = discord.Embed(title="Bot was added to new server", colour=discord.Colour(0x1738d4), description="DootDoot was added to new server\n"+guildid+"\nowned by "+ownerid+"\nguild name: "+guildname, timestamp=datetime.now())
 embed.set_thumbnail(url="https://cdn.onlinewebfonts.com/svg/img_145486.png")
 
 await channel.send(embed=embed)


@client.event
async def on_guild_leave(guild):
 logschannel = config['log_channel']
 guildid = str(guild.id)
 ownerid = str(guild.owner)
 guildname = str(guild.name)
 channel = client.get_channel(logschannel)
 embed = discord.Embed(title="Bot was added to new server", colour=discord.Colour(0x1738d4), description="DootDoot was added to new server\n"+guildid+"\nowned by "+ownerid+"\nguild name: "+guildname, timestamp=datetime.now())
 embed.set_thumbnail(url="https://cdn1.iconfinder.com/data/icons/interface-elements-ii-1/512/Logout-512.png")

 await channel.send(embed=embed)

client.run(config['token'])
