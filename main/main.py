try:
    # LOCAL

    # STANDARD LIBARY
    import os
    import sys

    # PIP
    import yaml
    import discord
    from discord.ext import commands
except:
    print("Couldn't load all the libaries. Please install the libaries listed in requirements.txt.")
    sys.exit(0)

# Set token
try:
    token = ""

except:
    print(
        "Please type in a valid bot token. The token can be found at the Discord Developer Portal at 'applications/<application id>/bot'.")
    print("Type in a bot token or press enter to skip.")
    set_token = input()
    if set_token != "":
        os.environ["scdtoken"] = set_token
        print("Updated the 'scdtoken' to '" + os.environ["scdtoken"] + "'.")
    sys.exit(0)

cwd = os.getcwd()

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello')


@client.command(name='say')
async def say(ctx, *args):
    var = ''
    for s in args:
        var += f'{s} '
    await ctx.send(var)


@client.command(name='user')
async def user(ctx):
    user = ctx.message.author
    mention = ctx.message.author.mention
    id = ctx.message.author.id
    await ctx.send(user)
    await ctx.send(mention)
    await ctx.send(id)


@client.command(name='stop')
@commands.has_permissions(administrator=True)
async def stop_bot(ctx):
    """Stoppt den Bot (Admin)"""

    await ctx.send('Bot stoppt...')
    await client.close()


try:
    client.run(token)

except:
    print("ERROR: Unable to run the client. Did you input a invalid token?")
