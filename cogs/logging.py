import discord
from discord.ext import commands

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log_channel_id = None  # Set via command

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def setlog(self, ctx, channel: discord.TextChannel):
        self.log_channel_id = channel.id
        await ctx.send(f"Log channel set to {channel.mention}")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if self.log_channel_id and not message.author.bot:
            channel = self.bot.get_channel(self.log_channel_id)
            if channel:
                embed = discord.Embed(
                    title="Message Deleted",
                    description=f"**Author:** {message.author}\n**Content:** {message.content}",
                    color=0xFF0000
                )
                embed.set_footer(text="GachaPlex — Created by Uzi | https://discord.gg/h5jYF4aA")
                await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if self.log_channel_id and not before.author.bot:
            channel = self.bot.get_channel(self.log_channel_id)
            if channel:
                embed = discord.Embed(
                    title="Message Edited",
                    description=f"**Author:** {before.author}",
                    color=0xFFA500
                )
                embed.add_field(name="Before", value=before.content or "No content", inline=False)
                embed.add_field(name="After", value=after.content or "No content", inline=False)
                embed.set_footer(text="GachaPlex — Created by Uzi | https://discord.gg/h5jYF4aA")
                await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Logging(bot))
