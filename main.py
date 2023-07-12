import discord
from discord.ext import commands
import os
from themes import coloring

bot = commands.AutoShardedBot(command_prefix="+",
                              intents=discord.Intents().all(),
                              help_command=None,
                              shard_count=1)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument.")
    elif isinstance(error, commands.NotOwner):
        await type(ctx)
        embed = discord.Embed(title="",
                              description="This command is only for the **owner**.",
                              color=coloring.GRAY)
        await ctx.send(embed=embed)
        print(f"[ ✕ ] {ctx.author.name} tried to use {ctx.command.name} but was not the owner.")
    else:
        await ctx.send("An error occurred.")

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