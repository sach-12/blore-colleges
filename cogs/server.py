import discord
from discord.ext import commands

class server(commands.Cog):

    def __init__(self, client):
        self.client = client

    #events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot is online : {self.client.user}")
    
    
    @commands.command(aliases = ['gomma', 'ungamman'])
    async def _gomma(self, ctx):
        await ctx.channel.send(":tengue_fold:")

def setup(client):
    client.add_cog(server(client))