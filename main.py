import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is online!")

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

client.run("ODIwNjQwNzY5MzAzNzczMjI1.YE4HRg.t9tV0FvRPm0LSgc5K6_VSqQzcAk")