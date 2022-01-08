import discord
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

    @bot.event
    async def on_ready():
        
        await bot.change_presence(status=discord.Status.online)
        await bot.change_presence(activity=discord.Game(name="퀴리 진행 준비 1단계"))
    
        print("봇 이름:", bot.user.name,"봇 아이디:", bot.user.id,"봇 버전:", discord.__version__)

    bot.run(os.environ['token'])

if __name__ == '__main__':
    main()
