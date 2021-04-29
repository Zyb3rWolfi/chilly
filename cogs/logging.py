import discord
from discord.ext import commands
import datetime

class log(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    mess = False
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        channel = reaction.message.channel
        guild = channel.guild
        message = reaction.message
        if user != self.bot.user:

            if reaction.emoji == '1️⃣':
                delete = self.bot.events.on_message_delete
                delete.update(enable=False)
                check = discord.utils.get(guild.categories, name="Chilly Logs") # Find the Category
                if not check: # If category doesnt exist create the logs

                    cat = await channel.guild.create_category_channel('Chilly Logs')
                    await channel.guild.create_text_channel("Message Logs", category=cat) # Message Logs
                    await channel.guild.create_text_channel("Other Logs", category=cat) # Other Logs
                    await channel.send('**Log Channels Were Succesfully Added!**')
                    await message.remove_reaction('1️⃣', user)
                    return

                else: 
                    await channel.send('**Log Channel Already Exists**')
                    await message.remove_reaction('1️⃣', user)

            if reaction.emoji == '2️⃣':
            
                channel1 = discord.utils.get(guild.channels, name="other-logs") # Other Logs
                channel2 = discord.utils.get(guild.channels, name="message-logs") # Message Logs
                category = discord.utils.get(guild.categories, name="Chilly Logs") # Category/Parent
                if category is not None: # Deletes All The Channels
                    await channel1.delete()
                    await channel2.delete()
                    await category.delete()
                    await channel.send('**Logging Channels Have Been Removed**')
                    await message.remove_reaction('2️⃣', user)
                
                else:
                    await channel.send('**Channels Either Dont Exist Or Have Been Renamed**')
                    await message.remove_reaction('2️⃣', user)

            if reaction.emoji == '❗':
                self.bot.dispatch("wait")



    @commands.command()
    async def test(self, ctx):
        msg = await ctx.send("`1` - Create Logs | `2` - Delete Logs")
        emoji = ['1️⃣', '2️⃣', '❗']
        response = 3
        for i in range(response):
            await msg.add_reaction(emoji[i])



    @commands.Cog.listener()
    async def on_message_delete(self, message):
        x = await self.bot.wait_for("wait")
        if x == True:
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
    bot.add_cog(log(bot))