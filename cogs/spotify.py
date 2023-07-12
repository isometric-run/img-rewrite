import discord
from discord.ext import commands
import datetime, pytz
from themes import coloring

class Spotify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Spotify command
    @commands.group(name="spotify", aliases=["sp"], invoke_without_command=True)
    async def spotify(self, ctx, target: discord.User = None):
        if ctx.command.is_on_cooldown(ctx):
            return
        
        embed = discord.Embed(
            color=coloring.GRAY,
            title="spotify",
            description="track your spotify in real-time"
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.display_avatar)
        embed.add_field(name="category", value="spotify", inline=True)
        embed.add_field(name="aliases", value="`sp`", inline=True)
        embed.add_field(name="usage", value="```>spotify [subcommand]```", inline=False)
        embed.set_footer(text="song, album", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Spotify_icon.svg/1982px-Spotify_icon.svg.png")
        await ctx.send(embed=embed)

    # Spotify command
    @spotify.command(aliases=["cover"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def album(self, ctx, target: discord.User = None):
        target = target or ctx.author
        for activity in target.activities:
            if isinstance(activity, discord.Spotify): 
                embed = discord.Embed(
                    color=coloring.GRAY,
                    description=f"[**{activity.title}**](https://open.spotify.com/track/{activity.track_id})"
                )
                embed.set_author(name=target.display_name, icon_url=target.display_avatar)
                embed.set_footer(text=activity.album)
                embed.set_image(url=activity.album_cover_url)
                return await ctx.send(embed=embed)
            
        embed = discord.Embed(
            color=coloring.GRAY,
            description=f"**{target.display_name}**, I couldn't find your [**Spotify Activity**](https://support.discord.com/hc/en-us/articles/360000167212-Discord-Spotify-Connection)"
        )
        embed.set_author(name=target.display_name, icon_url=target.display_avatar)
        embed.set_footer(text="make sure your status is showing!")
        embed.set_image(url="https://r2.e-z.host/300a8f3b-4721-4cf0-b415-1a823ac14d47/9z6qolgg.png")
        await ctx.send(embed=embed)

    @spotify.command(aliases=["song", "np"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def track(self, ctx, target: discord.Member = None):
        target = target or ctx.author
        for activity in target.activities:
            print(activity)
            if isinstance(activity, discord.Spotify):

                current_time = datetime.datetime.now(pytz.utc)
                start_time = activity.start.replace(tzinfo=pytz.utc)
                elapsed_time = current_time - start_time
                elapsed_minutes, elapsed_seconds = divmod(elapsed_time.seconds, 60)
                total_minutes, total_seconds = divmod(activity.duration.seconds, 60)
                formatted_duration = f"{elapsed_minutes:02d}:{elapsed_seconds:02d} — {total_minutes:02d}:{total_seconds:02d}"
                
                artist = activity.artist.replace(";", ",")
                embed = discord.Embed(
                    color=coloring.GRAY,
                    description=f"[**{activity.title}**](https://open.spotify.com/track/{activity.track_id})\n{artist}"
                )
                embed.set_author(name=target.display_name, icon_url=target.display_avatar)
                embed.set_footer(text=formatted_duration)
                embed.set_thumbnail(url=activity.album_cover_url)
                return await ctx.send(embed=embed)

        embed = discord.Embed(
            color=coloring.GRAY,
            description=f"**{target.display_name}**, I couldn't find your [**Spotify Activity**](https://support.discord.com/hc/en-us/articles/360000167212-Discord-Spotify-Connection)"
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.display_avatar)
        embed.set_footer(text="make sure your status is showing!")
        embed.set_image(url="https://r2.e-z.host/300a8f3b-4721-4cf0-b415-1a823ac14d47/9z6qolgg.png")
        return await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Spotify(bot))