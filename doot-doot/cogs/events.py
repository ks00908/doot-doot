import discord
import random
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import find
from datetime import datetime
import json

def getConfig(path):
    configFile = open(path, "r")
    return json.loads(configFile.read())
config = getConfig("config.json")

class events(commands.Cog):



    def __init__(self, bot):
        self.bot = bot

    @client.event
    async def on_server_join(self, guild):
        logschannel = config['log_channel']
        channel = self.bot.get_channel(logschannel)
        embed = discord.Embed(title="Bot was added to new server", colour=discord.Colour(0x1738d4), description="DootDoot was added to new server\n"+guild.id+" owned by "+guild.owner, timestamp=datetime.now())
        #embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")

        await channel.send(embed)


def setup(bot):
    bot.add_cog(events(bot))
