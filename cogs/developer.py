import discord
from discord.ext import commands
import asyncio
from themes import coloring

async def type(ctx):
    async with ctx.typing():
            await asyncio.sleep(0.5)


class MyView(discord.ui.View):
    @discord.ui.button(label="IMG", style=discord.ButtonStyle.gray, disabled=True)
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("Woah how did you click this button") 

class Developer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def ping(self, ctx):
        await type(ctx)
        embed = discord.Embed(title='Pong!', description=f'Pong! {round(self.bot.latency * 1000)}ms', color=coloring.GRAY)
        await ctx.send(embed=embed)
                              
async def setup(bot):
    await bot.add_cog(Developer(bot))