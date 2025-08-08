import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(color=0xAA00FF)
        embed.set_image(url=member.avatar.url)
        embed.set_footer(text="GachaPlex — Created by Uzi | https://discord.gg/h5jYF4aA")
        await ctx.send(embed=embed)

    @commands.command()
    async def eightball(self, ctx, *, question):
        responses = [
            "Yes", "No", "Maybe", "Definitely", "I wouldn't count on it",
            "Absolutely", "Ask again later"
        ]
        embed = discord.Embed(
            title="8ball",
            description=f"**Question:** {question}\n**Answer:** {random.choice(responses)}",
            color=0xAA00FF
        )
        embed.set_footer(text="GachaPlex — Created by Uzi | https://discord.gg/h5jYF4aA")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Fun(bot))
