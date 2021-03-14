import discord
from discord.ext import commands

class events(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send ("**You dont have the permission to use this command!**")

def setup(bot):
    bot.add_cog(events(bot))