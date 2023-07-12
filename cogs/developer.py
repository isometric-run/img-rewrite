import discord
from discord.ext import commands
import asyncio
from themes import coloring

async def type(ctx):
    async with ctx.typing():
            await asyncio.sleep(0.2)

class IMGBRANDING(discord.ui.View):
    @discord.ui.button(label="IMG", style=discord.ButtonStyle.blurple, disabled=True)
    async def IMGButton1(self, button, interaction):
        await interaction.response.send_message("Woah how did you click this button") 

    @discord.ui.button(label="@w3mbu", style=discord.ButtonStyle.green, disabled=True)
    async def MIDDLE(self, button, interaction):
        await interaction.response.send_message("Woah how did you click this button") 

class Developer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def ping(self, ctx):
        await type(ctx)
        embed = discord.Embed(title='Pong!', description=f'Pong! {round(self.bot.latency * 1000)}ms', color=coloring.GRAY)
        await ctx.send(embed=embed, view=IMGBRANDING())
                              
async def setup(bot):
    await bot.add_cog(Developer(bot))