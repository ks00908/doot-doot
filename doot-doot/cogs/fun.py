import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from urbandictionary_top import udtop
import requests

class fun(commands.Cog):

 def __init__(self, bot):
     # creation of the cog, do init stuff here, also gets and stores the bot
     self.bot: commands.Bot = bot

 def __unload(self):
     # cog unloading, cleaup if needed
     pass
 
 @commands.command()
 async def urban(self, ctx, message):
     """Gives the Urban Dictionary result of the given word"""
     try:     
         term = udtop(message)
         if term == None:
             await ctx.send("No result was returned")
         else:
             embed = discord.Embed(title=message+":", colour=discord.Colour(0x2773cc), description=term.definition+"\n\n examples: \n"+term.example)
             embed.set_footer(text="powered by urbandictionary.com", icon_url="https://i.imgur.com/RvNANOu.png")
             await ctx.send(content="", embed=embed)
     except discord.Forbidden:
         await ctx.send("Bot appears to not have 'Embed Links' permission required for urban command. Please allow dootdoot to embed links as it is required to send Rich Embeds")
     except TimeoutError:
         await ctx.send("There was a timeout error. its possible that either host, discord api or Urban Dictionary have curently issues. Please try again")
     except Exception:
         await ctx.send("There was an issue handling your request. Please try again later.")

 @commands.command()
 async def xkcd(self, ctx):
     """Lists curently most recent xkcd comic"""
     api_url="https://xkcd.com/info.0.json"

     r = requests.get(api_url)
     data = r.json()
     image_title = data["title"]
     image_url = data["img"]
     embed = discord.Embed(title=image_title, colour=0x2773cc)
     embed.set_image(url=image_url)
     try:
         await ctx.send(embed=embed)
     except discord.Forbidden:
         await ctx.send("Failed to send embed. Please make sure bot has 'Link Embeds' permission then try again")
     except TimeoutError:
         await ctx.send("There was a timeout while performing this command. Please try again.")
     except Exception:
         await ctx.send("There was an exception while handling your request. Please try again later.")

def setup(bot):
 bot.add_cog(fun(bot))