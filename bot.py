import asyncio
import discord
from game import *
from discord.ext import commands
import os
import random

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():

    # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
    await bot.change_presence(status=discord.Status.online)

    await bot.change_presence(activity=discord.Game(name="퀴리 진행 준비"))
    #await bot.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
    print("봇 이름:", bot.user.name,"봇 아이디:", bot.user.id,"봇 버전:", discord.__version__)

@bot.command()
async def 안녕(ctx):
    await ctx.send('반갑습니다')

@bot.command(description='For when you wanna settle the score some other way')
async def 골라줘(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def 별퀴(self, ctx):
    문제, 정답 = 랜덤별퀴()
    await ctx.send(문제)

    def 정답체크(message):
        if message.channel == ctx.channel and 정답 in message.content:
            return True
        else:
            return False

    try:
        await self.client.wait_for("message", timeout = 20.0, check = 정답체크)
        await ctx.send(정답 + " 정답!")
    except asyncio.TimeoutError:
        await ctx.send("20초 내에 아무도 정답을 맞추지 못했습니다. 새로운 문제를 출제합니다.")


bot.run(os.environ['token'])