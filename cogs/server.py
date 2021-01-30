import discord
from discord.ext import commands

BOT_LOGS = 801322661899796501

class server(commands.Cog):

    def __init__(self, client):
        self.client = client

    #events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot is online : {self.client.user}")
        await self.client.get_channel(BOT_LOGS).send(f"Bot is online : {self.client.user}")
    
    
    @commands.command(aliases = ['gomma', 'ungamman'])
    async def _gomma(self, ctx):
        await ctx.channel.send(":tengue_fold:")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        justjoined_role = discord.utils.get(member.guild.roles, name="Just Joined")
        await member.add_roles(justjoined_role)

def setup(client):
    client.add_cog(server(client))