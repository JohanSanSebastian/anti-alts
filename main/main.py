try:
    # LOCAL

    # STANDARD LIBARY
    import os
    import sys
    import time

    # PIP
    import yaml
    import discord
    from discord.ext import commands
except:
    print("Couldn't load all the libaries. Please install the libaries listed in requirements.txt.")
    sys.exit(0)

cwd = os.getcwd()

# Set token
try:
    token = open(cwd + "\\token.txt").read()

except:
    print("""Please type in a valid bot token.
    The token can be found at the Discord Developer Portal at 'applications/<application id>/bot'.""")
    sys.exit(0)

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=".", intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client}")

@client.event
async def on_member_join(member):
    print("join")
    if time.time() - member.created_at.timestamp() < 2592000: # 2592000
        print("time")
        channel = client.get_channel(799605130222895114)
        print("channel")
        await channel.send(f"> :no_entry: {member.mention} Alt account detected")
        await member.send("""
        :no_entry: Your account has been blocked on blockabl.

        > **Blocked by:** Bot (blockabl AntiAlt)

        > **Reason:** we believe that this is an alt account.

        > **What does that mean?** You don't have full access to
        > certain features of both the Discord server and the
        > Minecraft server, e.g. writing in Channels, at least on
        > this account.

        > **False-positive! I'm innocent!** If this is NOT an alt account,
        > we apologize for this. Contact us and don't worry.

        > **When do I get unblocked?** If this is in fact an alt account,
        >  don't be suprised if we even KICK or BAN you.

        For further information, contact us via `#support`.
            """)
    else:
        pass


@client.command(name="ping")
async def hello(ctx):
    await ctx.send("Ping!")


@client.command(name="say")
async def say(ctx, *args):
    var = ""
    for s in args:
        var += f"{s} "
    await ctx.send(var)


@client.command(name="check")
async def user(ctx, *args):
    user = ctx.message.author
    mention = ctx.message.author.mention
    id = ctx.message.author.id
    await ctx.send(user)
    await ctx.send(mention)
    await ctx.send(id)


@client.command(name="kill")
@commands.has_permissions(administrator=True)
async def stop_bot(ctx):
    await ctx.send("Terminating the bot...")
    await client.close()
    sys.exit(0)

try:
    client.run(token)
except:
    print("ERROR: Unable to run the client. Did you input a invalid token?")
    sys.exit(0)
