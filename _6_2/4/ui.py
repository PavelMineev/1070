import discord
from discord import ui, ButtonStyle, TextStyle
from gen import generate_image
import asyncio

print(2)
class TestModal(ui.Modal, title='Какую картинку вы хотите сгенерировать?'):
    prompt = ui.TextInput(label='Запрос')

    async def on_submit(self, interaction: discord.Interaction):
        if not interaction.response.is_done():
            await interaction.response.defer()
        generate_image(self.prompt, interaction.channel.id, interaction.message.id)
        # await interaction.message.edit(content=f'Запрос: {self.prompt}\n', attachments=[discord.File(path)])
        print(1)



class GenereteImg(ui.Button):
    def __init__(self,
                 label="Сгенерировать картинку",
                 style=ButtonStyle.green,
                 row=0):
        super().__init__(label=label, style=style, row=row)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(TestModal())


class StartView(ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(GenereteImg())
