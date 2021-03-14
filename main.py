import discord
from discord.ext import commands
import time

client = commands.Bot(command_prefix="!")
client.remove_command('help')
version = "0.0.1"
extensions = ['cogs.commands', 'cogs.basic', 'cogs.events']
if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)

@client.event
async def on_ready():
    print("Bot is online!", version)

@client.command()
async def ping(ctx):
    await ctx.send("pong!")

ruleslist = [
    "`1` -->> Follow Discord TOS",
    "`2` -->> No Racism Or Discrimination",
    "`3` -->> No Swearing"
]

@client.command()
async def rules(ctx, *, num):
    await ctx.send(ruleslist[int(num) - 1   ])

client.run("ODIwNjQwNzY5MzAzNzczMjI1.YE4HRg.TqYuFeeKVOR5DJxsDfZ9lFFC2Co")