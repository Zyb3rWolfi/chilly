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
    
def setup(bot):
    bot.add_cog(mod(bot))

# mongodb+srv://Zyber:<password>@cluster0.qyo6z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority