import discord
from discord.ext import commands
import os

class colleges(commands.Cog):

	def __init__(self, client):
		self.client = client
		self.college_list = ["PES University",
			"National Institute of Engineering",
			"MS Ramaiah University",
			"IIIT Banglore",
			"RV College",
			"BMS College",
			"RNS Institute of Technology",
			"New Horizon College of Engineering",
			"Dayananda Sagar University",
			"Nitte Meenakshi Institute",
			"BNM Institute",
			"Banglore Institute",
			"Oxford College of Engineering",
			"Christ University",
			"Reva University",
			"Sir M Vishvesvaraya Institute",
			"CMR University",
			"JSS Academy of Technical Education",
			"Dr. Ambedkar Institute",
			"Presidency University",
			"Jain University",
			"SJBIT",
			"Kammawari Sangha Institute"]
	
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


def setup(client):
	client.add_cog(colleges(client))