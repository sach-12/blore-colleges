
import discord
from discord.ext import commands
import os
from time import sleep
from dotenv import load_dotenv

load_dotenv('.env')
TOKEN = os.getenv('DISCORD_TOKEN')


BOT_LOGS = 801322661899796501


client = commands.Bot(command_prefix="!", help_command=None)


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    # admin = discord.utils.get(ctx.guild.roles, name = "Server Boss")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(TOKEN)
