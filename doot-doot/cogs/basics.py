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
        self.bot = bot

    def __unload(self):
        # cog unloading, cleaup if needed
        pass

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        cogs = []
        cog = cog.lower()
        for c in ctx.bot.cogs:
            cogs.append(c.replace('Cog', '').lower())

        if cog in cogs:
            self.bot.unload_extension("cogs." + cog)
            self.bot.load_extension("cogs." + cog)
            await ctx.send(f'**{cog}** has been reloaded.')
        else:
            await ctx.send(f"I can't find that cog.")

    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def shutdown(self, ctx):
        """kills the bot"""
        await ctx.send("you're such a turnoff")
        await self.bot.logout()
        await self.bot.close()

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Shows the Gateway Ping"""
        t1 = time.perf_counter()
        await ctx.trigger_typing()
        t2 = time.perf_counter()
        await ctx.send(f":hourglass: gateway ping: {round((t2 - t1) * 1000)}ms :hourglass:")

    @commands.command()
    async def github(self, ctx):
        """gives you my source code"""
        await ctx.send("Want to report bug? \n submit feature request? \n make new feature? \n bot code is avaible on github page: \n <https://github.com/ks00908/doot-doot>")

    @commands.command()
    async def invite(self, ctx):
     """invite me to your server!"""
     embed=discord.Embed(title="Inviting the bot is easy!", colour=discord.Colour(0x7289DA), url="https://discordapp.com", description="Invite doot-doot to your server using this handy link: [Discord bot invite Oauth](https://discordapp.com/oauth2/authorize?client_id=593170973193273344&permissions=3145984&scope=bot) \n if you don't see your server make sure you are logged to right account at [Discord web client](https://www.discordapp.com)", timestamp=datetime.datetime.utcfromtimestamp(1561488324))
     await ctx.send(embed)

def setup(bot):
    bot.add_cog(basics(bot))
