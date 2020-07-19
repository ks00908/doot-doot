import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from urbandictionary_top import udtop
import aiohttp
from utils.Fr13nd5h1p import Fr13nd5sh1p
from utils.pat import pat

class Fun(commands.Cog):

    def __init__(self, bot):
        # Creation of the cog, do init stuff here, also gets and stores the bot
        self.bot: commands.Bot = bot

    def __unload(self):
        # Cog unloading, cleanup if needed
        pass

    @commands.command()
    async def urban(self, ctx, message):
        """Gives the Urban Dictionary result of the given word"""
        if ctx.channel.is_nsfw():
            try:
                term = udtop(message)
                if term is None:
                    await ctx.send("No result was returned")
                else:
                    embed = discord.Embed(title=message + ":", colour=discord.Colour(0x2773cc),
                                          description=term.definition + "\n\n examples: \n" + term.example)
                    embed.set_footer(text="powered by urbandictionary.com", icon_url="https://i.imgur.com/RvNANOu.png")
                    await ctx.send(content="", embed=embed)
            except discord.Forbidden:
                await ctx.send(
                    "Bot appears to not have 'Embed Links' permission required for urban command. Please allow "
                    "dootdoot to embed links as it is required to send Rich Embeds")
            except TimeoutError:
                await ctx.send(
                    "There was a timeout error. its possible that either host, discord api or Urban Dictionary have "
                    "curently issues. Please try again later and if issues continue contact bot owner.")
            except Exception:
                await ctx.send(
                    "There was an issue handling your request. Please try again later and if issues continue contact "
                    "bot owner.")
        else:
            await ctx.send(
                "Due to nature of Urban dictionary messages it is required to use this command in NSFW channel")

    @commands.command()
    async def xkcd(self, ctx):
        """Lists curently most recent xkcd comic"""
        api_url = "https://xkcd.com/info.0.json"

        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                data = await response.json()

                image_title = data["title"]
                image_url = data["img"]
                embed = discord.Embed(title=image_title, colour=0x2773cc)
                embed.set_image(url=image_url)
                try:
                    await ctx.send(embed=embed)
                except discord.Forbidden:
                    await ctx.send(
                        "Failed to send embed. Please make sure bot has 'Link Embeds' permission then try again")
                except TimeoutError:
                    await ctx.send(
                        "There was a timeout while performing this command. Please try again later and if issues "
                        "continue contact bot owner.")
                except Exception:
                    await ctx.send(
                        "There was an exception while handling your request. Please try again later and if issues "
                        "continue contact bot owner.")

    @commands.command()
    async def hug(self, ctx, target: discord.Member = None):
        """Gives someone a hug"""
        if target is None:
            return await ctx.send("You have to put a mention or user id as an argument!")

        sender = ctx.author
        msg = await Fr13nd5sh1p.send_love(sender.name, target.mention)
        return await ctx.send(msg)

    @commands.command()
    async def pat(self, ctx, target: discord.Member = None):
        """Gives someone a hug"""
        if target is None:
            return await ctx.send("You have to put a mention or user id as an argument!")

        sender = ctx.author
        msg = await pat.send_love(sender.name, target.mention)
        return await ctx.send(msg)

def setup(bot):
    bot.add_cog(Fun(bot))
