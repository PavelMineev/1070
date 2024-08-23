
import discord
from discord.ext import commands, tasks
from config import TOKEN
from ui import *
import os

command_prefix = "!"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=command_prefix, intents=intents)


@bot.event
async def on_ready():
    print("Bot started")
    task_loop.start()


@tasks.loop(seconds=10)
async def task_loop():
    print("Поиск картинок")
    file_list = os.listdir("images")
    for file_name in file_list:
        print("Найдена картинка " + file_name)
        channel_id, message_id = file_name.split(".")[0].split("_")
        channel = await bot.fetch_channel(int(channel_id))
        print(channel)
        message = await channel.fetch_message(message_id)
        print(message)
        await message.edit(content="None", view=None, attachments=[discord.File(f"images/{file_name}")])
        os.remove(f"images/{file_name}")
        print("Картинка в сообщении обновлена")


@bot.command()
async def img(ctx: commands.Context):
    await ctx.send("Готов к творчеству!", view=StartView())


bot.run(token=TOKEN)
