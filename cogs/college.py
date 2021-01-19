import discord
from discord.ext import commands
import os

class colleges(commands.Cog):

	def __init__(self, client):
		self.client = client
		self.college_list = {"PES University" : ["pes", "pesit", "pesu"],
			"National Institute of Engineering" : ["nie"],
			"MS Ramaiah University" : ["msru"],
			"IIIT Banglore" : ["iiitb"],
			"RV College" : ["rv", "rvce"],
			"BMS College" : ["bms", "bmsce"],
			"RNS Institute of Technology" : ["rnsit", "rns"],
			"New Horizon College of Engineering" : ["nhce"],
			"Dayananda Sagar University" : ["ds", "dsu"],
			"Nitte Meenakshi Institute" : ["nitte", "nittem", "nittemit", "nittemi"],
			"BNM Institute" : ["bnm", "bnmi", "bnmit"],
			"Banglore Institute" : ["bi"],
			"Oxford College of Engineering" : ["oce", "oxford"],
			"Christ University" : ["cu", "christ"],
			"Reva University" : ["ru", "revau", "reva"],
			"Sir M Vishvesvaraya Institute" : ["smvit", "smvi", "vit"],
			"CMR University" : ["cmru", "cmr"],
			"JSS Academy of Technical Education" : ["jss", "jssat", "jssate"],
			"Dr. Ambedkar Institute" : ["ait", "dait", "dai", "da"],
			"Presidency University" : ["presidency", "pu"],
			"Jain University" : ["jain", "ju"],
			"SJBIT" : ["sjbit"],		#kekw
			"Kammawari Sangha Institute" : ["ksi", "ksit", "ks"]}
	
	@commands.command(aliases = ["list", "colleges", "l"])
	async def _list(self, ctx):
		list_embed = discord.Embed(title="List of Colleges", description="all keywords and corresponding colleges")
		list_embed.add_field(name=f"{len(self.college_list)} Colleges", value="```css\n"+"\n\n".join(f"[{str(key).zfill(2)}]  :  {val}" for key, val in enumerate(self.college_list)) + "\n```")
		await ctx.send(embed = list_embed)

	@commands.command(aliases = ["updateRole", "ur"])
	async def _ur(self, ctx):
		for i in self.college_list:
			if not i in [r.name for r in ctx.guild.roles]:
				await ctx.guild.create_role(name=i)
				await ctx.send(f"{i} role added")
			else :
				await ctx.send(f"{i} role exists")

	@commands.command(aliases = ["college"])
	async def _clg(self, ctx, clgid):
		clgName = self.college_list[clgid]
		for i in ctx.guild.roles:
			if(clgName == i.name):
				ctx.author.add_role(role=i)

	@commands.command(aliases = ["addCollege", "ac"])
	async def _add_college(self, ctx, *, prvt=""):
		if prvt == "":
			await ctx.channel.send("enter a valid role")
			return
		
		if prvt in [r.name for r in ctx.guild.roles]:
			await ctx.channel.send("role already exists")

		self.college_list += [prvt]
		role = await ctx.guild.create_role(name = prvt)
		category = await ctx.guild.create_category(prvt)

		await category.set_permissions(role, read_messages=True, send_messages=True, connect=True, speak=True)
		await category.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False, connect=False, speak=False)

		await ctx.guild.create_text_channel(prvt, category=category, sync_permissions=True)
		await ctx.guild.create_voice_channel(prvt, category=category, sync_permissions=True)

		await ctx.send(f"private role, category and channels create for {role.mention}")

	@commands.command(aliases = ["deleteCollege", "dc"])
	async def _delete_college(self, ctx, role: discord.Role = None):
		print(role)
		if role == None:
			await ctx.channel.send("please mention a role")
			return
		
		if role not in [r.name for r in ctx.guild.roles]:
			await ctx.channel.send("invlaid role")
			return

		role = discord.utils.get(ctx.guild.roles, name=role)
		await ctx.channel.send(role)


def setup(client):
	client.add_cog(colleges(client))