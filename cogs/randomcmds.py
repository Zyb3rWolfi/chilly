import discord
from discord.ext import commands
import random

class fun(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.cooldown(1, 2)
    @commands.command()
    async def kill(self, ctx, name : discord.Member):
        kill_gif = [
            "https://media1.tenor.com/images/bb4b7a7559c709ffa26c5301150e07e4/tenor.gif?itemid=9955653",
            "https://i.pinimg.com/originals/ff/2d/cd/ff2dcd44504000e320c21ae5682b5369.gif",
            "https://i.chzbgr.com/full/8442235648/h5122C918/whats-the-name-of-that-anime",
            "https://i.pinimg.com/originals/42/d0/40/42d0409bf0f0e88ddbb19f7584ac1bee.gif",
            "https://media1.tenor.com/images/afdae3b811f2bce97ea8d510e988b8ea/tenor.gif?itemid=17870581"
        ]   
        rndm_gif = random.choice(kill_gif)
        author = ctx.message.author.name
        if name.display_name == author:
            await ctx.send("**No! Dont kill yourself.**")
        else:
            sentence = "{} has wiped out {}!" .format(author, name.display_name)
            embed=discord.Embed(title= sentence, description="", color=discord.Color.red())
            embed.set_image(url=rndm_gif)
            await ctx.send(embed=embed)
    @kill.error
    async def kill_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("**Cooldown Activated!** `Try Again in a bit`")

def setup(bot):
    bot.add_cog(fun(bot))