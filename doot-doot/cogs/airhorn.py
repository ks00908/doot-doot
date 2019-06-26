import discord
import asyncio
from discord.ext import commands


async def play_file(self, voice_channel, filename):
    voice_channel = await voice_channel.connect()
    source = discord.FFmpegPCMAudio(filename)
    voice_channel.play(source, after=lambda: print("played doot"))
    await ctx.send(":thumbsup: dooted the doot")
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
            print(f'{str(user)} is in {voice_channel}')
            await play_file(ctx.author.voice.channel, "airhorn.mp3")

    @commands.command()
    @commands.guild_only()
    async def bazinga(self, ctx):
        """Plays bazinga effect."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            print(f'{str(user)} is in {voice_channel}')
            await play_file(ctx.author.voice.channel, "bazinga.mp3")


def setup(bot):
    bot.add_cog(airhorn(bot))
