import discord
from discord.ext import commands

class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.role_messages = {}  # message_id: {emoji: role_id}

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def addreactionrole(self, ctx, message_id: int, emoji: str, role: discord.Role):
        if message_id not in self.role_messages:
            self.role_messages[message_id] = {}
        self.role_messages[message_id][emoji] = role.id
        await ctx.send(f"Reaction role added: {emoji} → {role.name}")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id in self.role_messages:
            emoji_roles = self.role_messages[payload.message_id]
            if str(payload.emoji) in emoji_roles:
                guild = self.bot.get_guild(payload.guild_id)
                role = guild.get_role(emoji_roles[str(payload.emoji)])
                member = guild.get_member(payload.user_id)
                if role:
                    await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id in self.role_messages:
            emoji_roles = self.role_messages[payload.message_id]
            if str(payload.emoji) in emoji_roles:
                guild = self.bot.get_guild(payload.guild_id)
                role = guild.get_role(emoji_roles[str(payload.emoji)])
                member = guild.get_member(payload.user_id)
                if role:
                    await member.remove_roles(role)

async def setup(bot):
    await bot.add_cog(ReactionRoles(bot))
