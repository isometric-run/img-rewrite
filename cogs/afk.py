import discord
from discord.ext import commands
from themes import coloring

class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.data = []

    @commands.group()
    async def a(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("test")

    @a.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def afk(self, ctx, *args):
        msg = ' '.join(args)
        self.data.append(ctx.author.id)
        self.data.append(msg)
        await ctx.send(f"{ctx.author.mention} Is now afk. `{msg}`")

    @commands.Cog.listener()
    async def on_message(self, message):
        for i in range(len(self.data)):
            if (f"<@{self.data[i]}>" in message.content) and (not message.author.bot):
                await message.channel.send(f"<@{self.data[i]}> is away right now, they said: {self.data[i+1]}")

    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        embed = discord.Embed(title="", description=f"{user.mention} is not longer **afk**!", color=coloring.GRAY)
        if user.id in self.data:
            i = self.data.index(user.id)
            self.data.remove(self.data[i+1])
            self.data.remove(user.id)
            await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(AFK(bot))