
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

#token = ""
token = "ODAwNzUwNzM5Nzk0Mjk2ODQy.YAWrPQ.iX42c1afJdEpx_X1FGtZytNj5Jc"
client = commands.Bot(command_prefix = "!", help_command=None)

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(token)
