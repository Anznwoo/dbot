import discord
from cogs.exam import *
from cogs.game import *
from discord.ext import commands
import os



def main():
    prefix = '!'
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix = prefix, intents=intents)

    for filename in os.listdir('./cogs'):
        if '.py' in filename:
            filename = filename.replace('.py', '')
            bot.load_extension(f"cogs.{filename}")

    bot.run(os.environ['token'])

if __name__ == '__main__':
    main()

    
