import discord
from discord.ext import commands

class gomma(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['help'])
    async def _help(self, ctx):
        #botcommand : [[aliases for the bot], 'brief desc', 'example]
        dic = {
            "Help": [['`help`', '`h`'], 'Get help from the bot on available commands', '`+help`\n\u200b'],
            "Ping": [['`Ping`'], 'Find the latency of the bot', '`+Ping`\n\u200b'],
            "Count roles": [['`c`', '`count`'], 'Count the number of people with the given role', '`+count Bots`\n\u200b']
        }
        output = discord.Embed(title="Commands", color=0x379316)
        for cmd in dic:
            commandVal = dic[cmd][0]
            st = ', '.join(commandVal)
            output.add_field(name = cmd, value = st + '\n' + dic[cmd][1] +'\nEg:' + dic[cmd][2], inline = False)
        output.set_footer(text = "The bot prefix is `+`")
        await ctx.send(embed=output)
    
    @commands.command(aliases=['Ping'])
    async def _ping(self, ctx):
        await ctx.send("Pong!!!\n" + str(round(self.client.latency * 1000)) + "ms")

    @commands.command(aliases=['c', 'count'])
    async def _count(self, ctx, *roleName):
        roleName = ' '.join(roleName)
        #convert it back into string and split it at '&' and strip the individual roles
        try:
            roleName = roleName.split('&')
        except:
            pass
        temp = []
        for i in roleName:
            temp.append(i.strip())
        roleName = temp
        await ctx.send("Got request for role " + str(roleName))
        #A command to get number of users in a role
        if roleName == ['']:
            for guild in self.client.guilds:
                await ctx.send("We have {} people here, wow!!".format(len(guild.members)))
        else:
            thisRole = []
            #make a list of all roles in terms of role-id
            for roles in roleName:
                thisRole.append(discord.utils.get(ctx.guild.roles, name=roles))
            for guild in self.client.guilds:
                count = 0
                for member in guild.members:
                    boolean = True
                    #bool will be true only if all the roles passed as args are present
                    for roles in thisRole:
                        if roles not in member.roles:
                            boolean = False
                    if boolean:    
                        count += 1
            await ctx.send(str(count) + " people has role " + str(thisRole))


    # @commands.command(aliases=['migrate'])
    # async def _migrate(self, ctx, categoryint, roleint):
    #     if(self.admin in ctx.author.roles):
    #         category = ctx.guild.get_channel(int(categoryint))
    #         # print(category)
    #         new_category = ctx.guild.get_channel(808902926033879040)
    #         # print(new_category)
    #         role = get(ctx.guild.roles, id=int(roleint))
    #         # print(role)
    #         overwrites = {
    #                 role: discord.PermissionOverwrite(view_channel=True, connect=True),
    #                 self.dyno: discord.PermissionOverwrite(view_channel=True, send_messages=True),
    #                 self.muted: discord.PermissionOverwrite(send_messages=False, speak=False),
    #                 self.nqn: discord.PermissionOverwrite(view_channel=True),
    #                 self.namma_bot: discord.PermissionOverwrite(view_channel=True),
    #                 self.atlas: discord.PermissionOverwrite(view_channel=True, send_messages=False),
    #                 ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False, create_instant_invite=False)
    #             }
    #         for items in category.channels:
    #             if items.name == 'lobby':
    #                 await items.edit(name=role.name, category=new_category, sync_permissions=False, overwrites=overwrites)
    #                 await ctx.channel.send(f"channel name  :  **{items.name}** type  :  **{items.type}** has been moved")
    #             else:
    #                 await items.delete()
    #                 await ctx.channel.send(f"channel name  :  **{items.name}** type  :  **{items.type}** has been deleted")
    #         await category.delete()
    #         await ctx.channel.send(f"channel name  :  **{category.name}** type  :  **{category.type}** has been deleted")
        
    #     else:
    #         await ctx.channel.send("Unauthorised")


def setup(client):
    client.add_cog(gomma(client))