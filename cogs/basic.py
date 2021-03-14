import discord
from discord.ext import commands

class basicCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=['help'])
    async def helpP(self, ctx):
        embed = discord.Embed(title = "Help", description = "", colour = discord.Color.blurple())
        embed.add_field(name = "Show Help", value = "`!help`", inline = True)
        embed.add_field(name = "Ban User", value = "`!ban`", inline = True)
        embed.add_field(name = "Unban User", value = "`!unban`", inline = True)
        embed.add_field(name = "Purge Message", value = "`!purge`", inline = True)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(basicCommands(bot))