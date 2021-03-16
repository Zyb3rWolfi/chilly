import discord
from discord.ext import commands

class basicCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=['help'])
    async def helpP(self, ctx):
        embed = discord.Embed(title = "Chilly Bot Commands", description = "The Bot Prefix Is `c`", colour = discord.Color.blurple())
        embed.add_field(name="Purge Messages", value="`purge`", inline=True)
        embed.add_field(name="Ban User", value="`ban`", inline=True)
        embed.add_field(name="Unban User", value="`unban`", inline=True)
        embed.add_field(name="Kick User", value="`kick`", inline=True)
        embed.add_field(name="Lock Channels", value="`lock`", inline=True)
        embed.add_field(name="Unlock Channels", value="`unlock`", inline=True)
        embed.add_field(name="Add Log Channels", value="`log create`", inline=True)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(basicCommands(bot))