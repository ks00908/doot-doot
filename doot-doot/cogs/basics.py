#imports time
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import time
from datetime import datetime

import logging


class basics(commands.Cog):

 def __init__(self, bot):
     # creation of the cog, do init stuff here, also gets and stores the bot
     self.bot: commands.Bot = bot

 def __unload(self):
     # cog unloading, cleaup if needed
     pass




 @commands.command()
 @commands.guild_only()
 @commands.has_permissions(administrator=True)
 async def shutdown(self, ctx):
     """kills the bot"""
     await ctx.send("you're such a turnoff")
     await self.bot.logout()
     await self.bot.close()

 @commands.command()
 async def ping(self, ctx:commands.Context):
     """Shows the Gateway Ping"""
     t1 = time.perf_counter()
     await ctx.trigger_typing()
     t2 = time.perf_counter()
     await ctx.send(f":hourglass: gateway ping: {round((t2 - t1) * 1000)}ms :hourglass:")

 @commands.command()
 async def github(self, ctx):
     """gives you my source code"""
     await ctx.send("Want to report bug? \n submit feature request? \n make new feature? \n bot code is avaible on github page: \n <https://github.com/ks00908/doot-doot>")
def setup(bot):
 bot.add_cog(basics(bot))