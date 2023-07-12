import discord
from discord.ext import commands
import giphy_client
from giphy_client.rest import ApiException
import random
import pyttsx3
import asyncio

async def type(ctx):
    async with ctx.typing():
            await asyncio.sleep(2)

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.engine = pyttsx3.init()

    @commands.command()
    async def gif(seld,ctx,*,q="random"):
        await type(ctx)
        api_key="yVUciQy7vpc1o0JX2WrUACUNaLz8e5GN"
        api_instance = giphy_client.DefaultApi()
        try: 
            api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
            lst = list(api_response.data)
            giff = random.choice(lst)
            link = f"https://media.giphy.com/media/{giff.id}/giphy.gif"

            emb = discord.Embed(title=f"",
                                description=f"[**{q}**]({link})",
                                color=0x2F3136)
            emb.set_image(url = link)
            emb.set_footer(text=f"Requested by {ctx.author.name} ", icon_url=ctx.author.avatar)

            await ctx.channel.send(embed=emb)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

async def setup(bot):
    await bot.add_cog(Fun(bot))