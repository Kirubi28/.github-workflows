import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')
name_list = {}

allowed_role_id = [1218421605386944603, 1218421454408777788]

def has_allowed_role(ctx):
    """Check if the user invoking the command has the allowed role."""
    return discord.utils.get(ctx.author.roles, id=allowed_role_id) is not None

@bot.command()
@commands.check(has_allowed_role)
async def addname(ctx, name: str, number: int):
    name_list[name] = number
    await ctx.send(f'Added {name} with number {number}')

@bot.command()
@commands.check(has_allowed_role)
async def listnames(ctx):
    if name_list:
        names = '\n'.join([f'{name}: {number}' for name, number in name_list.items()])
        await ctx.send(f'List of names:\n{names}')
    else:
        await ctx.send('Name list is empty')

@bot.command()
@commands.check(has_allowed_role)
async def removename(ctx, name: str):
    if name in name_list:
        del name_list[name]
        await ctx.send(f'Removed {name} from the list')
    else:
        await ctx.send(f'{name} is not in the list')

@bot.command()
@commands.check(has_allowed_role)
async def clearnames(ctx):
    name_list.clear()
    await ctx.send('Cleared the name list')

bot.run('MTIyODg4MzI3NDg5ODYwODEzOQ.GnCRAd.pP4hTor9lmi5kjzxGcPPqQ246Bp3CZbaq-pCU8')
