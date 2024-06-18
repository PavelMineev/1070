from config import *
from logic import *
import discord
from discord.ext import commands
from config import TOKEN

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot started")


@bot.command()
async def start(ctx: commands.Context):
    await ctx.send(f"Привет, {ctx.author.name}. Чтобы узнать список команд, введи !help_me")


@bot.command()
async def help_me(ctx: commands.Context):
    await ctx.send(
        "`!start` - начать работу с ботом и получить приветственное сообщение.\n"
        "`!help_me` - получить список доступных команд.\n"
        "`!show_city <city_name>` - отобразить указанный город на карте.\n"
        "`!remember_city <city_name>` - сохранить город в список избранных.\n"
        "`!show_my_cities` - показать все сохраненные города."
    )


@bot.command()
async def show_city(ctx: commands.Context, *, city_name=""):
    if not city_name:
        await ctx.send("Неверный формат. Укажите название города на английском языке через пробел после команды.")
        return
    manager.create_graph(f'{ctx.author.id}.png', [city_naпшеme])  # Создание карты для города
    await ctx.send(file=discord.File(f'{ctx.author.id}.png'))


@bot.command()
async def show_my_cities(ctx: commands.Context, *, city_name=""):
    cities = manager.select_cities(ctx.author.id)  # Получение списка городов пользователя

    if cities:
        manager.create_graph(f'{ctx.author.id}_cities.png', cities)  # Создание карты для всех городов
        await ctx.send(file=discord.File(f'{ctx.author.id}_cities.png'))
    else:
        await ctx.send("У вас пока нет сохраненных городов.")


@bot.command()
async def remember_city(ctx: commands.Context, *, city_name=""):
    if manager.add_city(ctx.author.id, city_name):  # Проверка и добавление города в БД
        await ctx.send(f'Город {city_name} успешно сохранен!')
    else:
        await ctx.send("Неверный формат. Укажите название города на английском языке через пробел после команды.")


if __name__ == "__main__":
    manager = DB_Map("database.db")
    bot.run(TOKEN)
