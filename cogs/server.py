import discord
from discord.ext import commands

BOT_LOGS = 801322661899796501


class server(commands.Cog):

    def __init__(self, client):
        self.client = client

    # events
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.wait_until_ready()
        print(f"Bot is online : {self.client.user}")
        await self.client.get_channel(BOT_LOGS).send(f"Bot is online : {self.client.user}")
        guildObj = self.client.get_guild(800581401324945428)
        self.just_joined = discord.utils.get(
            guildObj.roles, id=805084725710422026)

    @commands.command(aliases=['gomma', 'ungamman'])
    async def _gomma(self, ctx):
        await ctx.channel.send(":tengue_fold:")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.add_roles(self.just_joined)


def setup(client):
    client.add_cog(server(client))
