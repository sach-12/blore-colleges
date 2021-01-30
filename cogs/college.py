import discord
from discord.ext import commands
import os
from time import sleep

BOT_LOGS = 801322661899796501


class colleges(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.college_list = {
            "PES University" : ["pes", "pesit", "pesu", "pesuecc", "pes university"],
            "MS Ramaiah Institute of Technology": ["msrit", "rit", "ms ramaiah institute of technology"],
            "MS Ramaiah University": ["msru", "ruas"],
            "IIIT Bangalore": ["iiitb", "iiit bangalore", "iiitb bengaluru"],
            "RV College": ["rv", "rvce", "rv college of engineering", "rvitm", "rvit", "rv institute of technology", "rv institute of technology and management"],
            "BMS College": ["bms", "bmsce", "bms college of engineering", "bmsit", "bms institute of technology"],
            "RNS Institute of Technology": ["rnsit", "rns", "rns institute of technology"],
            "New Horizon College of Engineering": ["nhce", "new horizon",  "new horizon college of engineering"],
            "Dayananda Sagar": ["ds", "dsu", "dayandanda sagar", "dayananda sagar university","dsit"],
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
            "Indian Institute of Technology Dharwad": ["iit", "iit dharwad", "iitd", "indian institute of technology dharwad"]
            }
    

    @commands.command(aliases = ['list', 'colleges', 'l'])
    async def _list(self, ctx):
        list_embed = discord.Embed(
            title="List of colleges", description='All keywords and corresponding colleges'
        )
        list_embed.add_field(name=f"{len(self.college_list)} Colleges", value="```css\n"+"\n\n".join(
            f"[{str(key).zfill(2)}]  :  {val}" for key, val in enumerate(self.college_list)
        ) + "\n```")
        await ctx.channel.send(embed=list_embed)

    
    @commands.command(aliases = ['ac', 'addcollege'])
    async def _add_college(self, ctx, *clg):
        clg=list(clg)
        clg=" ".join(clg)
        if clg == "":
            await ctx.channel.send("Enter a valid role")
            return
        
        if clg in [r.name for r in ctx.guild.roles]:
            await ctx.channel.send("Role already exists")
            return
        
        role = await ctx.guild.create_role(name=clg)
        muted = discord.utils.get(ctx.guild.roles, name="Muted")
        nqn = discord.utils.get(ctx.guild.roles, name="Not Quite Nitro")
        dyno = discord.utils.get(ctx.guild.roles, name="Dyno")
        namma_bot = discord.utils.get(ctx.guild.roles, name="Namma Bot")
        category = await ctx.guild.create_category(clg)

        await category.set_permissions(role, read_messages=True, connect=True)
        await category.set_permissions(dyno, view_channel=True, send_messages=True)
        await category.set_permissions(muted, send_messages=False, speak=False)
        await category.set_permissions(nqn, view_channel=True)
        await category.set_permissions(namma_bot, view_channel=True)
        await category.set_permissions(ctx.guild.default_role, view_channel=False)

        await ctx.guild.create_text_channel('lobby', category=category, sync_permissions=True)
        await ctx.guild.create_text_channel('events', category=category, sync_permissions=True, slowmode_delay=60)
        await ctx.guild.create_voice_channel('general', category=category, sync_permissions=True)

        await self.client.get_channel(BOT_LOGS).send(f"Private role, category and channels created for {role.mention}")


    @commands.command(aliases = ['deleteCollege', 'dc'])
    async def _delete_college(self, ctx, *, role=None):
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
        for chn in ctx.guild.channels:
            if chn.name == role.name:
                category = chn
                break
        
        for items in category.channels:
            await items.delete()
            await ctx.channel.send(f"channel name  :  **{items.name}** type  :  **{items.type}** has been deleted")

        await category.delete()
        await ctx.channel.send(f"channel name  :  **{category.name}** type  :  **{category.type}** has been deleted")


    @commands.command(aliases = ['accept', 'Accept'])
    async def _verify(self, ctx):
        verified = discord.utils.get(ctx.guild.roles, name = "Idly Vada")
        if(verified in ctx.author.roles):
            await ctx.channel.send("You've already chosen a college. Don't try to scam me you naughty little....")
            return
        else:
            await ctx.channel.send("I hope you went through those rules. Tell me which college you're from and I'll give you access to the server.\nOh I can understand abbreviated college names too!!")
            msg = await self.client.wait_for("message", check=lambda msg: msg.author == ctx.author)
            msg = str(msg.content)
            msg = msg.lower()
            bot_parents = discord.utils.get(ctx.guild.roles, name="Bot parents")
            for i in self.college_list.keys():
                college_alias = self.college_list.get(i)
                for j in college_alias:
                    if(j == msg):
                        await ctx.channel.send(f"I gotcha fam. You now have access to {str(i)}'s college specific channels. Enjoy your stay!")
                        role = discord.utils.get(ctx.guild.roles, name = i)
                        sleep(4)
                        await ctx.author.add_roles(role)
                        await ctx.author.add_roles(verified)
                        justjoined_role = discord.utils.get(ctx.author.guild.roles, name="Just Joined")
                        await ctx.author.remove_roles(justjoined_role)
                        await ctx.channel.purge(limit=4)
                        return
            await ctx.channel.send(f"Never heard of the place. Lemme call my masters {bot_parents.mention}")


def setup(client):
    client.add_cog(colleges(client))

        
