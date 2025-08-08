import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.welcome_channel_id = None  # Set this in config or command

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if self.welcome_channel_id:
            channel = self.bot.get_channel(self.welcome_channel_id)
            if channel:
                embed = discord.Embed(
                    title="Welcome!",
                    description=f"Welcome to {member.guild.name}, {member.mention}!",
                    color=0xAA00FF
                )
                embed.set_footer(text="GachaPlex — Created by Uzi | https://discord.gg/h5jYF4aA")
                await channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def setwelcome(self, ctx, channel: discord.TextChannel):
        self.welcome_channel_id = channel.id
        await ctx.send(f"Welcome channel set to {channel.mention}")

async def setup(bot):
    await bot.add_cog(Welcome(bot))
