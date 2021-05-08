import discord
from discord.ext import commands
import datetime

class log(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    # Logging System Group Commands

    @commands.group()
    async def log(self, ctx):
        t = 2
    # Setup Command
    @commands.has_permissions(manage_channels = True)
    @log.command(name='setup')
    async def setup(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title = "Chilly Logging", description = "Setting Up Log Channels...", colour = discord.Color.blurple())
        error = discord.Embed(title = "Chilly Logging", description = "Log Channels Already Exist, Exiting...", colour = discord.Color.blurple())
        check = discord.utils.get(guild.categories, name="Chilly Logs") # Find the Category
        if not check: # If category doesnt exist create the logs
            send = await ctx.send(embed=embed)
            cat = await ctx.guild.create_category_channel('Chilly Logs')
            await ctx.guild.create_text_channel("Message Logs", category=cat) # Message Logs
            await ctx.guild.create_text_channel("Other Logs", category=cat) # Other Logs
            await send.add_reaction('✅')

        else:
            send2 = await ctx.send(embed=error)
            await send2.add_reaction('⛔')

    @commands.has_permissions(manage_channels = True)
    @log.command(name='remove')
    async def remove(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title = "Chilly Logging", description = "Deleting All Log Channels", colour = discord.Color.blurple())
        error = discord.Embed(title = "Chilly Logging", description = "Log Channels Do Not Exist...", colour = discord.Color.blurple())
        channel1 = discord.utils.get(guild.channels, name="other-logs") # Other Logs
        channel2 = discord.utils.get(guild.channels, name="message-logs") # Message Logs
        category = discord.utils.get(guild.categories, name="Chilly Logs") # Category/Parent
        if category is not None: # Deletes All The Channels
            send = await ctx.send(embed=embed)
            await channel1.delete()
            await channel2.delete()
            await category.delete()
            await send.add_reaction('✅')
        else:
            send2 = await ctx.send(embed=error)
            await send2.add_reaction('⛔')

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        logchannel = discord.utils.get(message.guild.channels, name='message-logs') # Finds the log channel
        if logchannel is not None:
            if not message.author.bot:  # Checks for bot message
                channel = message.channel.name # Channel the deleted message is from
                embed = discord.Embed(title="Message Log", description="", color= discord.Color.red()) # Embeds
                embed.add_field(name="Message sent by {} has been deleted in `{}`" .format(message.author.display_name, channel), value=message.content, inline=True,)
                embed.set_footer(text='User ID: {} | Message ID: {}' .format(message.author.id, message.id))          
                await logchannel.send(embed=embed) # Finally sends the embed to log channel

    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        logchannel = discord.utils.get(after.guild.channels, name='message-logs') # Finds the log channel
        if not after.author.bot and logchannel is not None:    
            if before.content != after.content:
                channel = after.channel.name # Channel the edited message is from
                logchannel = discord.utils.get(after.guild.channels, name='message-logs') # Finds the log channel
                embed = discord.Embed(title="Message Log", description="Message edited in `{}` by {}" .format(channel, after.author.display_name), color= discord.Color.red()) # Embeds
                embed.add_field(name="Before", value=before.content, inline=True,)
                embed.add_field(name="After", value=after.content, inline=False,)
                embed.set_footer(text='User ID: {} | Message ID: {}' .format(after.author.id, before.id))
                await logchannel.send(embed=embed) # Finally sends the embed to log channel

    @commands.Cog.listener()
    async def on_member_join(self, member):
        logchannel = discord.utils.get(member.guild.channels, name='other-logs')
        if logchannel is not None:
            memberId = member.id
            embed = discord.Embed(title="Member Joined", description="<@{}>" .format(memberId, ), color= discord.Color.red()) # Embeds
            embed.set_footer(text='User ID: {}' .format(memberId))
            await logchannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        logchannel = discord.utils.get(member.guild.channels, name='other-logs')
        if logchannel is not None:  
            memberId = member.id
            embed = discord.Embed(title="Member Left", description="<@{}>" .format(memberId, ), color= discord.Color.red()) # Embeds
            embed.set_footer(text='User ID: {}' .format(memberId))
            await logchannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        logchannel = discord.utils.get(member.guild.channels, name='other-logs')
        if logchannel is not None:
            memberId = member.id
            embed = discord.Embed(title="Member Banned", description="<@{}>" .format(memberId, ), color= discord.Color.red()) # Embeds
            embed.set_footer(text='User ID: {}' .format(memberId))
            

def setup(bot):
    bot.add_cog(log(bot))
