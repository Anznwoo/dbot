import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

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
        
    # message.content = message의 내용
    if message.content == "!바보":
        # 현재 채널을 받아옴
        channel = message.channel
        # 답변 내용 구성
        msg = "너도 바보"
        # msg에 지정된 내용대로 메시지를 전송
        await channel.send(msg)
        return None


client.run(os.environ['token'])