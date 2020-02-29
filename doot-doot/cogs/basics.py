import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import time
from datetime import datetime
import logging

# declaring Cog
class basics(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
# defining owner only command to reload specific cog allowing to update in example airhorn.cog with new sounds without restarting whole bot
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

# owner only command to shutdown bot
    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def shutdown(self, ctx):
        """Kills the bot."""
        await ctx.send("you're such a turnoff")
        await self.bot.logout()
        await self.bot.close()
# ping command to measure how long it takes for bot to contact gateway
    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Shows the Gateway Ping."""
        t1 = time.perf_counter()
        await ctx.trigger_typing()
        t2 = time.perf_counter()
        await ctx.send(f":hourglass: gateway ping: {round((t2 - t1) * 1000)}ms :hourglass:")

# URL to github meant to allow people to easily find code
    @commands.command()
    async def github(self, ctx):
        """Gives you my source code."""
        embed = discord.Embed(
            title="Github repository for DootDoot", colour=0x7289DA,description="Want to report bug?\nsubmit feature request?\nmake new feature?\nbot code is available on github page:\n<https://github.com/ks00908/doot-doot>")
        embed.set_image(url="https://cdn.discordapp.com/avatars/593170973193273344/0a143cd8cfa9077570ebef54f097c882.webp")
        try:
         await ctx.send(embed=embed)
        except discord.Forbidden: #failover on 403 while sending embed. not used in invite becasue it would look awfull
         await ctx.send("Want to report bug?\nSubmit feature request?\nMake new feature?\nBot code is available on github page:\n<https://github.com/ks00908/doot-doot>")
    
# posts link allowing to add bot to your own server    
    @commands.command()
    async def invite(self, ctx):
        """Invite me to your server!"""
        embed = discord.Embed(
            title="Inviting the bot is easy!",
            colour=0x7289DA,
            description="Invite doot-doot to your server using this handy link: [Discord bot invite Oauth](https://discordapp.com/oauth2/authorize?client_id=593170973193273344&scope=bot&permissions=3165184)\nif you don't see your server make sure you are logged to right account at [Discord web client](https://www.discordapp.com)",
        )
        embed.set_image(url="https://cdn.discordapp.com/avatars/593170973193273344/0a143cd8cfa9077570ebef54f097c882.webp")
        try:
         await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("There was an error sending Embed with bot invite. please check if bot has permission to embed links and try again")

# Posts embed with message from bot author and link to patreon for official bot. Custom hosts are free to remove it, but i would appriciate keeping it
    @commands.command()
    async def patreon(self, ctx):
        """Optional support? thats great! No worry though, there wont be paywalls"""
        embed = discord.Embed(
            title="Patreon!",
            colour=0x7289DA,
            description="Hi. \nSo i noticed you took intrest in Patreon command.\nCase is simple, it is purely optional, you wont gain real perks apart from role on server and faster looking into feature requests (when possible).\n However, every dollar of support helps me keep bot afloat and helps me expand my knowledge.\n As i said many times there won't be any paywall on features, I won't EVER require you to pay for feature on official bot.\n Patreon link: https://www.patreon.com/ksmakesbots \n Once again, thank you for any support, including warm words or even virtual hug.\n\n   Krzysztof \"ks\" Szypuła"
        )
        try:
         await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("Bot cannot send embed. Please make sure bot has Embed links permission")

# owner command to change bot playing status            
    @commands.command()
    @commands.is_owner()
    async def setpresence(self,ctx,*, content):
     """Changing bots presence"""
     if len(content) > 0:
         if len(content) > 120:
             await ctx.send("Status text is too long, use 120 characters or less.")
         else:
             await self.bot.change_presence(activity=discord.Game(name=content))
             await ctx.send("Presence sucesfully changed to\n ```"+content+"```")
     else:
         await ctx.send("Presence cannot be empty string")
            
def setup(bot):
    bot.add_cog(basics(bot))
