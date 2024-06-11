from discord.ext import commands, tasks
from discord import ui, ButtonStyle
import discord
from config import TOKEN
from db_logic import Database
from PIL import Image
import os

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

buyer = None
current_image_id = 0
current_image_name = ""

db = Database("discord.db")
for image_name in os.listdir("images"):
    db.add_image(image_name)
db.close()


class PurchaseButton(ui.Button):
    def __init__(self, label="Купить", style=ButtonStyle.green, row=0):
        super().__init__(label=label, style=style, row=row)

    async def callback(self, interaction):
        global buyer
        db = Database('discord.db')
        if buyer is None:
            balance = db.get_balance(interaction.user.id)
            if balance >= 100:
                buyer = interaction.user
                balance = db.change_balance(interaction.user.id, -100)
                await interaction.user.send(f"Поздравляем с покупкой! Ваш баланс: {balance}",
                                            file=discord.File("images/"+current_image_name))
                db.add_purchase(interaction.user.id, current_image_id)
            else:
                await interaction.user.send(f"У вас недостаточно денег. Ваш баланс: {balance}")
        else:
            await interaction.user.send(f"Вас опередили! Картину купил {buyer.name}")

        db.close()
        if not interaction.response.is_done():
            await interaction.response.defer()


class PurchaseView(ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(PurchaseButton())


@bot.event
async def on_ready():
    my_func.start()


@bot.command()
async def join(ctx: commands.Context):
    db = Database("discord.db")
    db.add_user(ctx.author.id)
    db.close()
    await ctx.author.send("Добро пожаловать!")


@tasks.loop(seconds=30)
async def my_func():
    global buyer, current_image_id, current_image_name

    buyer = None
    db = Database('discord.db')
    users = db.get_all_users()

    current_image_id, current_image_name = db.get_random_image()
    image = Image.open("images/"+current_image_name)
    resize_coefficient = 0.1
    new_width = int(image.width * resize_coefficient)
    new_height = int(image.height * resize_coefficient)
    image = image.resize((new_width, new_height))
    image.save("thumbnail.png")
    db.close()

    for user_id in users:
        user = await bot.fetch_user(user_id[0])
        await user.send("", file=discord.File("thumbnail.png"), view=PurchaseView())


bot.run(TOKEN)
