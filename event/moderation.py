import discord
from discord.ext import commands
import datetime

class mod(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, msg):
        filtered_words = ["nigga", "niger", "niga", "nigger"]
        author = msg.author.mention
        for word in filtered_words:
            if word in msg.content:
                await msg.delete()
                await msg.channel.send("**{} Dont Say That Here!**" .format(author)) 
    
    # Logs Deleted Messages
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot:  # Checks for bot message
            channel = message.channel.name # Channel the deleted message is from
            logchannel = discord.utils.get(message.guild.channels, name='message-logs') # Finds the log channel
            embed = discord.Embed(title="Message Log", description="", color= discord.Color.red()) # Embeds
            embed.add_field(name="Message sent by {} has been deleted in `{}`" .format(message.author.display_name, channel), value=message.content, inline=True,)
            embed.set_footer(text='User ID: {} | Message ID: {}' .format(message.author.id, message.id))          
            await logchannel.send(embed=embed) # Finally sends the embed to log channel
    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not after.author.bot:
            if before.content != after.content:
                channel = after.channel.name # Channel the edited message is from
                logchannel = discord.utils.get(after.guild.channels, name='message-logs') # Finds the log channel
                embed = discord.Embed(title="Message Log", description="Message edited in `{}` by {}" .format(channel, after.author.display_name), color= discord.Color.red()) # Embeds
                embed.add_field(name="Before", value=before.content, inline=True,)
                embed.add_field(name="After", value=after.content, inline=False,)
                embed.set_footer(text='User ID: {} | Message ID: {}' .format(after.author.id, before.id))
                await logchannel.send(embed=embed) # Finally sends the embed to log channel
def setup(bot):
    bot.add_cog(mod(bot))