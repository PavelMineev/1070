from config import *
from logic import *
import discord
from discord.ext import commands
from config import TOKEN

command_prefix = "!"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=command_prefix, intents=intents)


@bot.event
async def on_ready():
    print("Bot started")


if __name__ == "__main__":
    manager = DB_Map(DATABASE)
    bot.run(TOKEN)
