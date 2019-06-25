import discord
import asyncio
from discord.ext import commands

class airhorn(commands.Cog):

    def __init__(self, client):
        # creation of the cog, do init stuff here, also gets and stores the bot
        self.bot = client
    
    @commands.command()
    @commands.guild_only()
    async def doot(self, ctx):
        """Doots the horn"""
        user = ctx.author
        if not user.voice:
         await ctx.send("You are not in voice channel.")
        else:
             vc = user.voice.channel
             print(f'{str(user)} is in {vc}')
             vc_channel = await vc.connect()
             source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source='airhorn.mp3'))
             vc_channel.play(source, after=lambda: print("player doot"))
             await ctx.send(":thumbsup: dooted the doot")
             while vc_channel.is_playing():
                 await asyncio.sleep(1)
             vc_channel.stop()
             await vc_channel.disconnect()

def setup(client):
    client.add_cog(airhorn(client))