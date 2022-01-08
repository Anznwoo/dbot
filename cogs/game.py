import asyncio
import discord
from discord.ext import commands
import csv
import random

문제 = ""
정답 = ""
별퀴나왔던문제 = []
등퀴나왔던문제 = []
추등퀴나왔던문제 = []
역등퀴나왔던문제 = []
응퀴나왔던문제 = []
추응퀴나왔던문제 = []
명퀴나왔던문제 = []
기선맞나왔던문제 = []
특선맞나왔던문제 = []
팀이동나왔던문제 = []

#별퀴문제
별퀴 = {'효천고 에이스' : '차명진', '박뱅':'박병호', '대투수':'양현종', '마트박': '박민우', '빨간 장갑의 마술사' : '김동엽', '오지배' : '오지환'}
별퀴리스트 = list(별퀴.keys())

class game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #랜덤별퀴
    @commands.command
    async def 별퀴(self, ctx):
        global 별퀴나왔던문제
        global 문제
        global 정답
        문제 = 별퀴리스트[random.randint(0,len(별퀴리스트)-1)]
        if 별퀴나왔던문제.count(문제) == 0:
            정답 = 별퀴.get(문제)
            별퀴나왔던문제.append(문제)
        else:
            if len(별퀴리스트) == len(별퀴나왔던문제):
                문제 = "더이상 남은 문제가 없습니다."
                정답 = "다른 종류의 문제를 출제해주세요."
            else:
                while 별퀴나왔던문제.count(문제) != 0:
                    문제 = 별퀴리스트[random.randint(0,len(별퀴리스트)-1)]
                if 별퀴나왔던문제.count(문제) == 0:
                    정답 = 별퀴.get(문제)
                    별퀴나왔던문제.append(문제)
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

def setup(bot):
    bot.add_cog(game(bot))