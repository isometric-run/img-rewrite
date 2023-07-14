import discord
from discord.ext import commands
import os
from themes import coloring
import Paginator

bot = commands.AutoShardedBot(command_prefix="-",
                              intents=discord.Intents().all(),
                              help_command=None,
                              shard_count=1)
DEVGUILD = bot.get_guild(1127713855737442315)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument.")
    elif isinstance(error, commands.CommandOnCooldown):
         embed = discord.Embed(title="",
                               description="<:TimeOut:1128583955772354601> This command is on cooldown.",
                               color=coloring.GRAY)
         embed.set_footer(text=f"Try again in {round(error.retry_after, 2)} seconds.")
         await ctx.send(embed=embed)
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
    await bot.change_presence(activity=discord.Game(name=f"Meet {bot.user.name}!"),
                              status=discord.Status.idle)

    for f in os.listdir("./cogs"):
	    if f.endswith(".py"):
		    await bot.load_extension("cogs." + f[:-3])

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def help(ctx, *, cog_name: str = None): # type: ignore
        if cog_name is None:
            cmd_count = 0
            category_commands = {}
            for cog in bot.cogs.values():
                category = cog.__class__.__name__
                if category not in category_commands:
                    category_commands[category] = []
                for cmd in cog.get_commands():
                    if not cmd.hidden:
                        category_commands[category].append(cmd.name)
                        cmd_count += 1

            embeds = []
            custom_embed = discord.Embed(
                title="", description="", color=coloring.GRAY).set_author(name=bot.user.name, icon_url=bot.user.avatar).add_field(name=f"Help | Total commands `{cmd_count}`", value="Use the **buttons** below to navigate the menus", inline=False)
            embeds.append(custom_embed)

            for category, commands_list in category_commands.items():
                commands_str = "[0;0m, [1;30m".join(commands_list)
                embed = discord.Embed(
                    title=f"{category} Commands", color=coloring.GRAY).set_author(name=bot.user.name, icon_url=bot.user.avatar)
                embed.add_field(name="Commands", value=f"```ansi\n[1;30m{commands_str}[0;0m\n```", inline=False)
                embeds.append(embed)

            await Paginator.Simple(
                PreviousButton=discord.ui.Button(label="<<", style=discord.ButtonStyle.blurple),
                NextButton=discord.ui.Button(label=">>", style=discord.ButtonStyle.blurple)).start(ctx, pages=embeds)
        else:
            cog = bot.get_cog(cog_name)
            if cog is not None:
                commands_list = [cmd.name for cmd in cog.get_commands() if not cmd.hidden]
                commands_str = ", ".join(commands_list)
                if commands_list:
                    embed = discord.Embed(title=f"{cog.qualified_name} Commands", color=coloring.GRAY).set_author(name=bot.user.name, icon_url=bot.user.avatar)
                    embed.add_field(name="Commands", value=f"```ansi\n[1;30m{commands_str}[0;0m\n```", inline=False)
                else:
                    embed = discord.Embed(title=f"{cog.qualified_name} Commands", color=coloring.GRAY).set_author(name=bot.user.name, icon_url=bot.user.avatar)
                    embed.add_field(name="No Commands", value="There are no commands available in this cog.")

                await ctx.send(embed=embed)
            else:
                await ctx.send("Invalid cog name.")

bot.run("MTEyMjQ5MTE0OTAxODQ3MjQ1OA.GpI93v.0YmYJcq4xcsEjAM7qAGTl4cEDYx8d2bwwbOSIc")