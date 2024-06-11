from discord.ext import commands, tasks
import discord
from config import TOKEN

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

user_id = 0 # Добавь свой user_id

@bot.event
async def on_ready():
    my_func.start()

@tasks.loop(seconds=10)
async def my_func():
    user = await bot.fetch_user(user_id)
    await user.send("Hello!")


bot.run(TOKEN)
