import asyncio
import discord
from discord.ext import commands
import csv
import random

class Exam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.change_presence(status=discord.Status.online)
        await self.change_presence(activity=discord.Game(name="퀴리 진행 준비 1단계"))
        print("봇 이름:", self.user.name,"봇 아이디:", self.user.id,"봇 버전:", discord.__version__)

    @commands.command
    async def 안녕(ctx):
        await ctx.send('반갑습니다')

    @commands.command
    async def 골라줘(ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))


def setup(bot):
    bot.add_cog(Exam(bot))