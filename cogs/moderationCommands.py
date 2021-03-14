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
        await ctx.message.delete()
    
    # -----------------------------------
    # Ban Command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, name : discord.Member, *, reason):
        await ctx.send(name.name + "Has been banned")
        await name.ban(reason=reason)
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send ("**Missing Argument!** `/ban [user] [reason]`")

    # -----------------------------------
    # Unban User 
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_disc = member.split('#')

        for banned_entry in banned_users:
            user = banned_entry.user

            if (user.name, user.discriminator) == (member_name, member_disc):

                await member.send("You have been banned!")
                await ctx.guild.unban(user)
                await ctx.send(member_name + " has been unbanned")
                return
        
        await ctx.send(member+" was not found")
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send ("**Missing Argument!** `/unban [user]`")
    # -----------------------------------
def setup(bot):
    bot.add_cog(commandEvent(bot))