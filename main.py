import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="c ", help_commmand=None)
client.remove_command('help')
version = "0.0.5"
extensions = ['cogs.moderationCommands', 'cogs.basic', 'cogs.events', 'cogs.randomcmds', 'event.moderation']
if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)

@client.event
async def on_ready():
    print("Bot is online!", version)
    while True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="You All"))

# -----------------------------
with open('token.txt') as f:
    TOKEN = f.readline()
# -----------------------------
client.run(os.environ['TOKEN'])

# Either create a new file named TOKEN.txt & paste your bot token 
# Or Remove selected code above & replace TOKEN with your discord token.