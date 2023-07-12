import discord
from discord.ext import commands
from themes import coloring
import requests

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group()
    async def u(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Specify CMD")

    @u.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def av(self, ctx, user: discord.Member = None): # type: ignore
        if user == None:
            user = ctx.author

        response = requests.get(user.avatar) # type: ignore
        with open("tmp/avatar.jpg", "wb") as file:
            file.write(response.content)

        embed = discord.Embed(title=f"{user.name}`s avatar",
                              color=coloring.GRAY)
        embed.set_image(url=user.avatar)

        await ctx.send(embed=embed)

    @u.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def banner(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        userid = user.id
        fetchuserid = await self.bot.fetch_user(userid)

        response = requests.get(fetchuserid.banner) # type: ignore
        with open("tmp/banner.jpg", "wb") as file:
            file.write(response.content)

        embed = discord.Embed(title="",
                              description="",
                              color=coloring.GRAY)
        embed.set_author(icon_url=user.avatar, 
                         name=f"{user.name}`s banner")
        embed.set_image(url=fetchuserid.banner)

        await ctx.send(embed=embed)

    @u.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def servericon(self, ctx, server: discord.Guild = None):
        server = server or ctx.guild

        response = requests.get(server.icon) # type: ignore
        with open("tmp/servericon.jpg", "wb") as file:
            file.write(response.content)

        embed = discord.Embed(title=f"{server}`s icon",
                              description=f"",
                              color=coloring.GRAY)
        embed.set_image(url=server.icon)
        await ctx.send(embed=embed)

    @u.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def serverbanner(self, ctx, server: discord.Guild = None):
        server = server or ctx.guild

        response = requests.get(server.banner) # type: ignore
        with open("tmp/serverbanner.jpg", "wb") as file:
            file.write(response.content)

        embed = discord.Embed(title=f"{server}`s banner",
                              description=f"",
                              color=coloring.GRAY)
        embed.set_image(url=server.banner)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))