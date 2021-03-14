import discord 
from discord.ext import commands

class commandEvent(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    # Purge Command
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, amount=2):
        await ctx.channel.purge(limit = amount + 1)
        number = amount 
        await ctx.send("`{} Messages has been deleted`" .format(number))
    # -----------------------------------

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, name : discord.Member, *, reason):
        await ctx.send(name.name + "Has been banned")
        await name.ban(reason=reason)

def setup(bot):
    bot.add_cog(commandEvent(bot))