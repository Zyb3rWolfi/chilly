import discord
from discord.ext import commands
import time

client = commands.Bot(command_prefix="!", help_commmand=None)
client.remove_command('help')
version = "0.0.1"
extensions = ['cogs.moderationCommands', 'cogs.basic', 'cogs.events', 'cogs.randomcmds']
if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)

@client.event
async def on_ready():
    print("Bot is online!", version)

client.run()# TOKEN GOES HERE