import discord
from discord.ext import commands

class gomma(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['help'])
    async def _help(self, ctx):
        #botcommand : [[aliases for the bot], 'brief desc', 'example]
        dic = {
            "help": [['`help`', '`h`'], 'get help from the bot on available commands', '`+help`'],
            "ping": [['`ping`'], 'find the latency of the bot', '`+ping`'],
            "count roles": [['`c`', '`count`'], 'count the number of people with the given role', '`+count Bots`'],
            "find college": [['`accept`'], 'find your college to get access to exclusive college based channels, and then type clg name ', '`+accept` and then after bot promts `PES`']
        }
        output = discord.Embed(title="Commands", color=0xff00ff)
        for cmd in dic:
            commandVal = dic[cmd][0]
            st = ', '.join(commandVal)
            output.add_field(name = cmd, value = st + '\n' + dic[cmd][1] +'\nEg:' + dic[cmd][2])
        output.set_footer(text = "The bot prefix is `+`")
        await ctx.send(embed=output)
    
    @commands.command(aliases=['ping'])
    async def ping(self, ctx):
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
                await ctx.send("Currently in "+str(guild))
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


def setup(client):
    client.add_cog(gomma(client))