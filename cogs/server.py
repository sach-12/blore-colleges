import discord
from discord.ext import commands
from discord.utils import get

BOT_LOGS = 801322661899796501
RULES_CHANNEL = 804369125014503426

class server(commands.Cog):

    def __init__(self, client, member):
        self.client = client

    # events
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.wait_until_ready()
        await self.client.get_channel(BOT_LOGS).send(f"Bot is online : {self.client.user}")
        self.guildObj = self.client.get_guild(800581401324945428)
        self.just_joined = get(self.guildObj.roles, id=805084725710422026)

        # self.admin = get(self.guildObj.roles, id=801312470928326676)
        # self.mods = get(self.guildObj.roles, id=800581837772292116)
        # self.bot_devs = get(self.guildObj.roles, id=804705156452188221)
        # self.bot_children = get(self.guildObj.roles, id = 805028812520685598)
        # self.dbc = get(self.guildObj.roles, id = 805106749857071104)
        # self.biryani = get(self.guildObj.roles, id = 805106710179479584)
        # self.bbb = get(self.guildObj.roles, id = 805321969117560853)
        # self.masala_dosa = get(self.guildObj.roles, id = 805106647290478602)
        # self.idli_vada = get(self.guildObj.roles, id = 805453201704484896)
        # self.bots = get(self.guildObj.roles, id = 804364008945221693)
        # self.roless = self.client.get_channel(804707604122566676)
        # self.veri = self.client.get_channel(804368803319250954)
        

        # rules1 = discord.Embed(title="Rules", color=0xff00ff)
        # await self.client.get_channel(RULES_CHANNEL).send(file=discord.File(r'rules.jpg'))
        # rules1.add_field(name=":one:  Be Respectful", value="If you're here, you already know what we mean. Go mental but don't take it too far wink\n\u200b", inline=False)
        # rules1.add_field(name=":two:  No racism/sexism AT ALL", value="Profanity is allowed but anything racist/sexist will get you a punishment. You don't get the N-word pass here.\n\u200b", inline=False)
        # rules1.add_field(name=":three:  No spamming unless the channel is meant for it.", value="Don't send a lot of small messages (or big ones) right after each other in the general categories unless you get permission from the mods.\n\u200b", inline=False)
        # rules1.add_field(name=":four:  Server Raiding", value="Allowed only when it's another server we're hitting xD\n\u200b", inline=False)
        # rules1.add_field(name=":five:  Direct & Indirect Threats", value="Threats to other users of DDoS, Death, DoX, abuse, and other malicious threats are absolutely prohibited and disallowed. Anything of this sort will get you a perma-ban.\n\u200b", inline=False)
        # rules1.add_field(name=":six:  Follow the Discord Community Guidelines", value="You can find them here: https://discordapp.com/guidelines\n(None of you are opening that link anyways so idk what the point is but oh well)\n\nThe Admins and Mods will Mute/Kick/Ban with NO MERCY! We're the chillest people you'll meet so if you've got a mute I think you should reconsider your actions.\n\nYour presence in this server implies accepting these rules, including all further changes. These changes might be done at any time without notice, it is your responsibility to check for them. Or not idk.", inline=False)
        # await self.client.get_channel(RULES_CHANNEL).send(embed=rules1)

        # await self.client.get_channel(RULES_CHANNEL).send(file=discord.File(r'roles.jpg'))
        # roles1 = discord.Embed(title = "Roles", color = 0xff00ff)
        # roles1.add_field(name= "\u200b", value=self.admin.mention + " : The all seeing owner of this server. His decision on anything is FINAL!\n", inline=False)
        # roles1.add_field(name="\u200b", value=self.mods.mention + " : The people you'll see the most. They moderate pretty much everything on this server. Listen to them or get whooped.\n", inline=False)
        # roles1.add_field(name="\u200b", value=self.bot_devs.mention + f" : The brainy hoomans behind the bots. Get the {self.bot_children.mention} role from {self.roless.mention}(after verification) if you're interested in bot dev!\n", inline=False)
        # roles1.add_field(name="\u200b", value=self.dbc.mention + " : The highest role achievable with the rank system. These people are legends!\n", inline=False)
        # roles1.add_field(name="\u200b", value=self.biryani.mention + " : Just slightly lesser than legends.\n", inline=False)
        # roles1.add_field(name="\u200b", value=self.bbb.mention + " : They'll get there eventually.\n", inline=False)
        # roles1.add_field(name="\u200b", value=self.masala_dosa.mention + " : Active but ehhhh.\n", inline=False)
        # roles1.add_field(name="\u200b", value=self.idli_vada.mention + " : Either dead or lame.\n", inline=False)
        # roles1.add_field(name="\u200b", value=self.bots.mention + " : Don't need any introduction whatsoever.", inline=False)
        # await self.client.get_channel(RULES_CHANNEL).send(embed=roles1)

        # verification = discord.Embed(title="Verification", color=0xff00ff)
        # verification.add_field(name="\u200b", value=f"If any issue comes up, ping any online moderator. Only ping the {self.mods.mention} role during a **server emergency**. **Do not ping** unnecessarily.\n\nOnce you're done reading this page, type ```+accept```in {self.veri.mention} to get access to the rest of the server")
        # await self.client.get_channel(RULES_CHANNEL).send(embed=verification)



    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.client.get_channel(BOT_LOGS).send(f"{member.mention} joined")
        just_joined = get(member.guild.roles, id=805084725710422026)
        await member.add_roles(just_joined)


    @commands.command(aliases=['gomma', 'ungamman'])
    async def _gomma(self, ctx):
        await ctx.channel.send("why ma")


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        string = str(error)
        await self.client.get_channel(BOT_LOGS).send(string)
        await self.client.get_channel(BOT_LOGS).send(f"{ctx.message.author.mention} made this error in {ctx.message.channel.mention}")

def setup(client):
    client.add_cog(server(client))
