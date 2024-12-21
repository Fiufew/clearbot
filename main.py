import os

from dotenv import load_dotenv
from disnake.ext import commands

load_dotenv()

TOKEN = os.environ['TOKEN']
bot = commands.Bot()


@bot.event
async def on_ready():
    print("Бот готов!")


@bot.slash_command()
async def clear(ctx):
    await ctx.response.defer(ephemeral=True)
    deleted = await ctx.channel.purge(limit=100)
    await ctx.edit_original_response(
        content=f'Удалено {len(deleted)} сообщение(й)'
    )


bot.run(TOKEN)
