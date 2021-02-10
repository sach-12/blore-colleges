import discord
from discord.ext import commands
import os
from time import sleep
from discord.utils import get

BOT_LOGS = 801322661899796501
COLLEGE_LOGS = 808892040321695754
COLLEGES_CATEGORY = 808902926033879040


class colleges(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.college_list = {
            "PES University": ["pes", "pesit", "pesu", "pesuecc", "pes university"],
            "MS Ramaiah Institute of Technology": ["msrit", "rit", "ms ramaiah institute of technology"],
            "MS Ramaiah University": ["msru", "ruas"],
            "IIIT Bangalore": ["iiitb", "iiit bangalore", "iiitb bengaluru"],
            "RV College": ["rv", "rvce", "rv college of engineering", "rvitm", "rvit", "rv institute of technology", "rv institute of technology and management"],
            "BMS College": ["bms", "bmsce", "bms college of engineering", "bmsit", "bms institute of technology"],
            "RNS Institute of Technology": ["rnsit", "rns", "rns institute of technology"],
            "New Horizon College of Engineering": ["nhce", "new horizon",  "new horizon college of engineering"],
            "Dayananda Sagar": ["ds", "dsu", "dayandanda sagar", "dayananda sagar university", "dsit"],
            "Nitte Meenakshi Institute of Technology": ["nitte", "nittem", "nittemit", "nittemi", "nitte meenakshi institute of technology", "nmit"],
            "BNM Institute": ["bnm", "bnmi", "bnmit", "bnm institute"],
            "Banglore Institute of Technology": ["bi", "bit", "banglore institute of technology"],
            "Oxford College of Engineering": ["oce", "oxford", "oxford college of engineering"],
            "Christ University": ["cu", "christ", "christ university"],
            "Reva University": ["ru", "revau", "reva", "reva university"],
            "Sir M Vishvesvaraya Institute of Technology": ["smvit", "smvi", "vit", "sir m vishvesvaraya institute of technology"],
            "CMR University": ["cmru", "cmr", "cmr university"],
            "CMR Institute of Technology": ["cmrit", "cmr institute of technology"],
            "JSS Academy of Technical Education": ["jss", "jssat", "jssate", "jss academy of technical education"],
            "Dr. Ambedkar Institute of Technology": ["ait", "dait", "dai", "da", "drait", "dr ambedkar institute of technology"],
            "Presidency University": ["presidency", "pu", "presidency university"],
            "Jain University": ["jain", "ju", "jain university"],
            "SJBIT": ["sjbit", "sjb institute of technology"],
            "Kammawari Sangha Institute OF Technology": ["ksi", "ksit", "ks", "kammawari sangha institute of technology"],
            "Indian Institute of Science": ["iis", "iisc", "indian institute of science"],
            "Acharya Institute of Technology": ["acharya", "ait", "acharya institute of technology"],
            "AMC Engineering College": ["amc", "amcu", "amc engineering college"],
            "Rajarajeshwari College of Engineering": ["rit", "rajarajeshwari college of engineering"],
            "Global Academy of Technology": ["gat", "global academy of technology"],
            "JSS Science and Technology University": ["jss", "jssst", "jss university", "jce", "jss science and technology university"],
            "National Institute of Engineering": ["nie", "national institute of engineering"],
            "National Institute of Technology Surathkal": ["nit", "nits", "nitk", "nit surathkal", "national institute of technology surathkal"],
            "Manipal Academy of Higher Education": ["manipal", "manipal university", "mahe", "manipal academy of higher education"],
            "Indian Institute of Technology Dharwad": ["iit", "iit dharwad", "iitd", "indian institute of technology dharwad"],
            "Transcend College": ["transcend", "tgi", "transcend college", "transcend group of institutions"],
            "MVJ College of Engineering": ["mvjce", "mvj college of engineering", "mvj"],
            "Cambridge Institute": ["cambridge institute", "cit", "cambridge institute of technology"]
        }

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.wait_until_ready()
        guildObj = self.client.get_guild(800581401324945428)
        self.admin = get(guildObj.roles, id=801312470928326676)
        self.mods = get(guildObj.roles, id=800581837772292116)
        self.bot_devs = get(guildObj.roles, id=804705156452188221)
        self.namma_bot = get(guildObj.roles, id=804742810049445938)
        self.verified = get(guildObj.roles, id=805151093310750761)
        self.just_joined = get(guildObj.roles, id=805084725710422026)
        self.muted = get(guildObj.roles, id=801295084754567169)
        self.dyno = get(guildObj.roles, id=800947868742713344)
        self.nqn = get(guildObj.roles, id=800753707246551111)
        self.atlas = get(guildObj.roles, id=808681096240955433)
        # self.everyone_role = get(guildObj.default_role)


    @commands.command(aliases=['list', 'colleges', 'l'])
    async def _list(self, ctx):
        list_embed = discord.Embed(
            title="List of colleges", description='All keywords and corresponding colleges'
        )
        # list_embed.add_field(name=f"{len(self.college_list)} Colleges", value="```css\n"+"\n\n".join(
        #     f"[{str(key).zfill(2)}]  :  {val}" for key, val in enumerate(self.college_list)
        # ) + "\n```")
        for clg in self.college_list:
            list_embed.add_field(name = clg, value = "```{}```".format(', '.join(self.college_list[clg])))
        await ctx.channel.send(embed=list_embed)

    @commands.command(aliases=['ac', 'addcollege'])
    async def _add_college(self, ctx, *clg):
        clg = list(clg)
        clg = " ".join(clg)
        if ((self.bot_devs in ctx.author.roles) or (self.mods in ctx.author.roles)):
            if clg == "":
                await ctx.channel.send("Enter a valid role")
                return

            if clg in [r.name for r in ctx.guild.roles]:
                await ctx.channel.send("Role already exists")
                return

            role = await ctx.guild.create_role(name=clg)
            category = ctx.guild.get_channel(COLLEGES_CATEGORY)
            overwrites = {
                role: discord.PermissionOverwrite(view_channel=True, connect=True),
                self.dyno: discord.PermissionOverwrite(view_channel=True, send_messages=True),
                self.muted: discord.PermissionOverwrite(send_messages=False, speak=False),
                self.nqn: discord.PermissionOverwrite(view_channel=True),
                self.namma_bot: discord.PermissionOverwrite(view_channel=True),
                self.atlas: discord.PermissionOverwrite(view_channel=True, send_messages=False),
                ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False, create_instant_invite=False)
            }

            await ctx.guild.create_text_channel(clg, category=category, sync_permissions=False, overwrites=overwrites)

            await ctx.channel.send(f"Private role and channel created for {role.mention}")
            await self.client.get_channel(BOT_LOGS).send(f"Private role and channel created for {role.mention}")
        
        else:
            await ctx.channel.send("You are not authorised to do that")

    @commands.command(aliases=['deleteCollege', 'dc'])
    async def _delete_college(self, ctx, *, role=None):
        if (self.bot_devs in ctx.author.roles):
            if ((role == None)):
                await ctx.channel.send("Please mention a valid role")
                return

            try:
                role = discord.utils.get(ctx.guild.roles, name=role)
                await role.delete()
                await ctx.channel.send(f"**{role}** has been deleted")
            except:
                await ctx.channel.send("Invalid role")
                return

            await ctx.channel.send("Checking for channels...")
            category = ctx.guild.get_channel(COLLEGES_CATEGORY)

            for items in category.channels:
                if(items.name == str(role.name).lower().replace(" ", "-")):
                    await items.delete()
                    await ctx.channel.send(f"channel name  :  **{items.name}** type  :  **{items.type}** has been deleted")

            await self.client.get_channel(BOT_LOGS).send(f"**{role}** has been deleted")
        
        else:
            await ctx.channel.send("You are not authorised to do that")

    @commands.command(aliases=['accept', 'Accept'])
    async def _verify(self, ctx):
        if(self.verified in ctx.author.roles):
            await ctx.channel.send("You've already chosen a college. Don't try to scam me you naughty little....")
            return
        else:
            await ctx.channel.send("I hope you went through those rules. Tell me which college you're from and I'll give you access to the server.\nPreferably the full name")
            msg = await self.client.wait_for("message", check=lambda msg: msg.author == ctx.author)
            msg = str(msg.content)
            await ctx.channel.send("I gotcha fam. One of the mods will get you a college role within 24 hours. Welcome to the server and enjoy your stay!")
            sleep(5)
            await ctx.author.add_roles(self.verified)
            await ctx.author.remove_roles(self.just_joined)
            await ctx.channel.purge(limit=4)
            await self.client.get_channel(COLLEGE_LOGS).send(f"{ctx.author.mention}  :  {msg}")



def setup(client):
    client.add_cog(colleges(client))
