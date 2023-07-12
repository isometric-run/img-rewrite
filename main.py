import discord
from discord.ext import commands
import os

bot = commands.AutoShardedBot(command_prefix="+",
                              intents=discord.Intents().all(),
                              help_command=None)

@bot.event
async def on_connect():
    os.environ['JISHAKU_NO_UNDERSCORE'] = 'True'
    os.environ['JISHAKU_RETAIN'] = 'True'

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await bot.load_extension('jishaku')

    for f in os.listdir("./cogs"):
	    if f.endswith(".py"):
		    await bot.load_extension("cogs." + f[:-3])

bot.run("MTEyODUyODEyMTI1MjAzMjU1Mg.GHxVvI.LEarIvm8m8yUXMYithtoAEPIExK4HlprLT9Gl0")