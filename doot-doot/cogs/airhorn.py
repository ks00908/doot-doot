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

    @commands.command()
    @commands.guild_only()
    async def justdoit(self, ctx):
        """Tells you to just do it."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "justdoit.mp3")

    @commands.command()
    @commands.guild_only()
    async def clap(self, ctx):
        """Just some clapping."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "clap.mp3")

    @commands.command()
    @commands.guild_only()
    async def oof(self, ctx):
        """Roblox oof."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "oof.mp3")

    @commands.command()
    @commands.guild_only()
    async def nope(self, ctx):
        """Nope."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "nope.mp3")

    @commands.command()
    @commands.guild_only()
    async def suspence(self, ctx):
        """Sudden suspence."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "suddensus.mp3")

    @commands.command()
    @commands.guild_only()
    async def sad(self, ctx):
        """Plays sad music."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "sadmusic.mp3")

    @commands.command()
    @commands.guild_only()
    async def fail(self, ctx):
        """Plays fail sound."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "fail.mp3")

    @commands.command()
    @commands.guild_only()
    async def gay(self, ctx):
        """HA GAY."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "hagay.mp3")

    @commands.command()
    @commands.guild_only()
    async def no(self, ctx):
        """Says no."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "no.mp3")
    @commands.command()
    @commands.guild_only()
    async def godno(self, ctx):
        """plays No god no."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "godno.mp3")

    @commands.command()
    @commands.guild_only()
    async def dootstorm(self, ctx):
        """plays sands storm but with doot."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "dootstorm.mp3")

def setup(bot):
    bot.add_cog(airhorn(bot))
