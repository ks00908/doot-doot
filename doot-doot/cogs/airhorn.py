import discord
import asyncio
from discord.ext import commands

async def play_file(ctx, filename):
     voice_channel = ctx.author.voice.channel
     print(f'{str(ctx.author)} is in {voice_channel}')
     try:
         voice_channel = await voice_channel.connect()
     except:
         voice_channel.disconnect()
         ctx.send("Exception occured, automatic process atempted to repair it, please try again.")
     
     source = discord.FFmpegPCMAudio(filename)


     voice_channel.play(source, after=lambda: print("played doot"))


     await ctx.send(":thumbsup: played the effect")
     while voice_channel.is_playing():
         await asyncio.sleep(1)

     voice_channel.stop()

     await voice_channel.disconnect()


class airhorn(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def doot(self, ctx):
        """Doots the horn."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "airhorn.mp3")

    @commands.command()
    @commands.guild_only()
    async def bazinga(self, ctx):
        """Plays bazinga effect."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "bazinga.mp3")


def setup(bot):
    bot.add_cog(airhorn(bot))
