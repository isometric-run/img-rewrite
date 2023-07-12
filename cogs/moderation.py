import discord
from discord.ext import commands
from themes import coloring

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count: int):
        embed = discord.Embed(title="",
                              description=f"Purged `{count}` messages from {ctx.channel}",
                              color=coloring.GRAY)
        await ctx.channel.purge(limit=count)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Moderation(bot))