import discord 
from discord.ext import commands
import asyncio

class commandEvent(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    # Purge Command
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, amount=2):
        await ctx.channel.purge(limit = amount + 1)
        number = amount 
        botmsg = await ctx.send("`{} Messages has been deleted`" .format(number))
        await asyncio.sleep(2)
        await botmsg.delete()
    
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
    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, name : discord.Member, reason):
        await name.kick(reason=reason)
        reason = "**{}** has been kicked. **Reason: `{}`**" .format(name, reason)
        await ctx.send(reason)
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send ("**Missing Argument!** `/kick [user] [reason]`")

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def lock(self, ctx, channel : discord.TextChannel=None):
        channels = channel or ctx.channel
        channel_name = channels.name
        await channels.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send("**Channel:** `{}` **Has Been Locked**" .format(channel_name))
    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def unlock(self, ctx, channel : discord.TextChannel=None):
        channels = channel or ctx.channel
        channel_name = channels.name
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send("**Channel:** `{}` **Has Been Unlocked**" .format(channel_name))

def setup(bot):
    bot.add_cog(commandEvent(bot))