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

	@commands.command(aliases = ["k", "keywords", "keys"])
	async def _keys(self, ctx):
		list_embed = discord.Embed(title="List of Colleges", description="all keywords and corresponding colleges")
		list_embed.add_field(name=f"{len(self.college_list)} Colleges", value="```css\n"+"\n\n".join(f"[{key}]  :  {self.college_list[key]}" for key in self.college_list) + "\n```")
		await ctx.send(embed = list_embed)

	@commands.command(aliases = ["updateRole", "ur"])
	async def _ur(self, ctx):
		for i in self.college_list:
			if not i in [r.name for r in ctx.guild.roles]:
				await ctx.guild.create_role(name=i)
				await ctx.send(f"{i} role added")
			else :
				await ctx.send(f"{i} role exists")

	@commands.command(aliases = ["addCollege", "ac"])
	async def _add_college(self, ctx, *, prvt=""):
		if prvt == "":
			await ctx.channel.send("enter a valid role")
			return

		role_name = prvt.split("|")[0][:-1]
		nicknames = prvt.split("|")[1][1:].split()

		if role_name in [r.name for r in ctx.guild.roles]:
			await ctx.channel.send("role already exists")
			return

		self.college_list[role_name] = nicknames
		role = await ctx.guild.create_role(name = role_name)
		muted = discord.utils.get(ctx.guild.roles, name="Muted")
		nqn = discord.utils.get(ctx.guild.roles, name="Not Quite Nitro")
		dyno = discord.utils.get(ctx.guild.roles, name="Dyno")
		category = await ctx.guild.create_category(role_name)

		await category.set_permissions(role, read_messages=True, connect=True)
		await category.set_permissions(dyno, view_chaneel=True, send_messages=True)
		await category.set_permissions(muted, send_messages=False, speak=False)
		await category.set_permissions(nqn, view_chaneel=True)
		await category.set_permissions(ctx.guild.default_role, view_chaneel=False)

		await ctx.guild.create_text_channel(role_name, category=category, sync_permissions=True)
		await ctx.guild.create_voice_channel(role_name, category=category, sync_permissions=True)

		await ctx.send(f"private role, category and channels create for {role.mention}")

	@commands.command(aliases = ["deleteCollege", "dc"])
	async def _delete_college(self, ctx, *, role = None):
		if role == None:
			await ctx.channel.send("Please mention a role")
			return

		try:
			role = discord.utils.get(ctx.guild.roles, name=role)
			await ctx.channel.send(f"**{role}** has been deleted")
			await role.delete()
		except:
			await ctx.channel.send("invalid role")
			return
		
		

		await ctx.channel.send("checking for channels")
		for chn in ctx.guild.channels:
			if chn.name == role.name:
				category = chn
				break

		for items in category.channels:
			await ctx.send(f"channel name : **{items.name}** type : **{items.type}** has been deleted")
			await items.delete()
		
		await ctx.send(f"channel name : **{category.name}** type : **{category.type}** has been deleted")
		await category.delete()	
			

		

def setup(client):
	client.add_cog(colleges(client))