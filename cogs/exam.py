import asyncio
import discord
from discord.ext import commands
import csv
import random

class Exam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command
    async def 안녕(ctx):
        await ctx.send('반갑습니다')

    @commands.command
    async def 골라줘(ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))


def setup(bot):
    bot.add_cog(Exam(bot))