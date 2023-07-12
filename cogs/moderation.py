import discord
from discord.ext import commands
from themes import coloring

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clear(self, ctx, count: int):
        embed = discord.Embed(title="",
                              description=f"Purged `{count}` messages from {ctx.channel}",
                              color=coloring.GRAY)
        await ctx.channel.purge(limit=count)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        if reason is None:
            reason = "There is no provided reason"

        embed = discord.Embed(title="",
                              description=f"Kicked {member.mention} for `{reason}`",
                              color=coloring.GRAY)
        dmembed = discord.Embed(title="",
                                description=f"You got kicked from **{ctx.guild.name}** for **{reason}**",
                                color=coloring.GRAY)
        
        await ctx.send(embed=embed)
        await member.send(embed=dmembed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slowmode(self, ctx, seconds: int):
        
        
        embed = discord.Embed(title="",
                            description=f"""> **Slowmode set to** `{seconds}` **by {ctx.author.mention}**""",
                            color=coloring.GRAY)
        embed.set_author(icon_url=self.bot.user.avatar, name=self.bot.user.name)
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Moderation(bot))