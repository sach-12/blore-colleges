
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv('.env')
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents().all()


BOT_LOGS = 801322661899796501
VERI_CHANNEL = 804368803319250954


client = commands.Bot(command_prefix="+", help_command=None, intents=intents)


@client.command(aliases = ['loadit'])
async def load(ctx, extension):
    bot_devs = discord.utils.get(ctx.guild.roles, id = 804705156452188221)
    if (bot_devs in ctx.author.roles):
        try:
            client.load_extension(f"cogs.{extension}")
            await client.get_channel(BOT_LOGS).send(f"{extension} cogs was loaded successfully")
            if(str(extension) == 'college'):
                await client.get_channel(VERI_CHANNEL).send("Bot's back online")
                await client.get_channel(VERI_CHANNEL).set_permissions(ctx.guild.default_role, send_messages=True)
                await client.get_channel(VERI_CHANNEL).purge(limit=2)
        except Exception as e:
            await ctx.channel.send(f"{e}")
    else:
        await ctx.channel.send("Unauthorised")


@client.command(aliases = ['unloadit'])
async def unload(ctx, extension):
    bot_devs = discord.utils.get(ctx.guild.roles, id = 804705156452188221)
    if (bot_devs in ctx.author.roles):
        try:
            client.unload_extension(f"cogs.{extension}")
            await client.get_channel(BOT_LOGS).send(f"{extension} cogs was unloaded successfully")
            if(str(extension) == 'college'):
                await client.get_channel(VERI_CHANNEL).send("Bot's down for maintenance")
                await client.get_channel(VERI_CHANNEL).set_permissions(ctx.guild.default_role, send_messages=False)
        except Exception as e:
            await ctx.channel.send(f"{e}")
    else:
        await ctx.channel.send("Unauthorised")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(TOKEN)
