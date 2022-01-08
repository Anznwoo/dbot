import discord
from discord.ext import commands
import os

client = commands.Bot()

@client.event
async def on_ready():

    # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
    await client.change_presence(status=discord.Status.online)

    await client.change_presence(activity=discord.Game(name="퀴리 진행 준비"))
    #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
    print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

async def on_message(message):
    # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
    if message.author.bot:
        return None

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content == "태그미":
        # channel = message.channel

        msg = "<@{}>".format(message.author.id)
        await client.send_message(message.channel,msg)
        # await channel.send(msg)
        return None

@client.command()
async def 안녕(ctx):
    await ctx.send('반갑습니다')


client.run(os.environ['token'])