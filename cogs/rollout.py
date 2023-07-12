import discord
from discord.ext import commands
from themes import coloring
import json
import aiohttp

class Rollouts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group()
    async def p(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("test")

    @p.command()
    async def rollouts(self, ctx, name):
        url = "https://raw.githubusercontent.com/discordexperimenthub/assyst-tags/main/experiment-rollout/data.json"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = json.loads(await response.text())

        if name in data:
            rollout_data = data[name]
            rate = rollout_data.get("rate", 0)
            ranges = rollout_data.get("ranges", [])

            if isinstance(rate, int):
                rate = str(rate) + "%"

            if isinstance(ranges, list) and len(ranges) > 0:
                min_range, max_range = ranges[0]
                ranges_text = f"{min_range} - {max_range}"
                namestr = f"{name}"

                message = f"# {namestr.replace('_', ' ').title()}\n<:ServerSubscritions:1128591973947809853> This feature has rolled out to **{rate}** of all servers **(~2.280.000)!** Ranges: **{ranges_text}.**"
                await ctx.send(message)
            else:
                await ctx.send("Invalid ranges data.")
        else:
            await ctx.send("Name not found in the JSON file.")

async def setup(bot):
    await bot.add_cog(Rollouts(bot))