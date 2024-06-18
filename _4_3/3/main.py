from discord.ext import commands, tasks
import discord
from config import *
import os
from game_models import Game
from ui_join_team import JoinTeamView

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
game = Game()


@bot.event
async def on_ready():
    print(f"Бот {bot.user.name} успешно запущен! Для старта викторины введи команду !quiz")


@bot.command()
async def quiz(ctx: commands.Context, number_of_teams='2'):
    if ctx.guild and ctx.author == ctx.guild.owner:

        if number_of_teams not in list("123456789"):
            await ctx.send("Неверно указано количество команд (от 1 до 9). Образец: !start 3", delete_after=10)

        else:
            game.number_of_teams = int(number_of_teams)
            game.teams.clear()
            [game.teams.append({}) for _ in range(game.number_of_teams)]
            game.info_message = await ctx.send(content="Выбери команду:",
                                               view=JoinTeamView(game),
                                               delete_after=600000)

    await ctx.message.delete()


bot.run(TOKEN)
