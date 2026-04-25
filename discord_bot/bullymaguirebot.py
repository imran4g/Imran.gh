
import discord
import random
import datetime
from discord.ext import commands

TOKEN = "Token here"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def helpme(ctx):
    e = discord.Embed(
        title="Welcome to bullyMaguire",
        description="Here are the commands to for a surprise",
        color=0xFF0000
    )
    e.set_thumbnail(url="https://static.wikia.nocookie.net/kingdomheartsfanon/images/e/ec/Bully_Maguire_headshot.jpg/revision/latest?cb=20201219032845")

    e.add_field(name="!helpme", value="To see these commands", inline=False)
    e.add_field(name="!needhelp", value="For extra help", inline=False)
    e.add_field(name="!hello", value="Greetings from Bully Maguire", inline=True)
    e.add_field(name="!time", value="Fun times", inline=False)
    e.add_field(name="!rent", value="...", inline=True)
    e.add_field(name="!back", value="ouch", inline=True)
    e.add_field(name="!watchout", value="◔_◔", inline=True)
    e.add_field(name="!moves", value="♪", inline=True)
    e.add_field(name="!cry", value="sad times", inline=True)
    e.add_field(name="!bully", value="...", inline=True)
    e.add_field(name="!sorry", value="not sorry", inline=True)
    e.add_field(name="!bye", value="cya", inline=True)
    e.add_field(name="!bullyback", value="sadness", inline=True)

    e.add_field(name="!ping", value="latency check", inline=True)
    e.add_field(name="!coinflip", value="heads or tails", inline=True)
    e.add_field(name="!roll", value="roll dice", inline=True)
    e.add_field(name="!choose", value="pick from options", inline=True)
    e.add_field(name="!userinfo", value="user info", inline=True)
    e.add_field(name="!serverinfo", value="server info", inline=True)
    e.add_field(name="!say", value="make bot speak", inline=True)
    e.add_field(name="!now", value="current time", inline=True)

    e.set_footer(text="End of Commands")
    await ctx.send(embed=e)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hey there, {ctx.author.name}!')

@bot.command()
async def time(ctx):
    await ctx.send('Pizza time', file=discord.File('ppp.gif'))

@bot.command()
async def bye(ctx):
    await ctx.send('See ya chump', file=discord.File('seeya.gif'))

@bot.command()
async def needhelp(ctx):
    await ctx.send(f"{ctx.author.name} I missed the part where that's my problem", file=discord.File('problem.gif'))

@bot.command()
async def watchout(ctx):
    await ctx.send('~inhale...~', file=discord.File('scream.gif'))

@bot.command()
async def moves(ctx):
    await ctx.send('Now dig on this', file=discord.File('dig.gif'))

@bot.command()
async def cry(ctx):
    await ctx.send('awe', file=discord.File('cry.gif'))

@bot.command()
async def rent(ctx):
    await ctx.send('...', file=discord.File('rent.gif'))

@bot.command()
async def bully(ctx):
    await ctx.send('dun~dun', file=discord.File('dirt.gif'))

@bot.command()
async def sorry(ctx):
    await ctx.send('want forgiveness?', file=discord.File('forgive.gif'))

@bot.command()
async def back(ctx):
    await ctx.send('owwww', file=discord.File('back.gif'))

@bot.command()
async def bullyback(ctx):
    await ctx.send('sniff', file=discord.File('mecry.gif'))

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def coinflip(ctx):
    await ctx.send(random.choice(["Heads", "Tails"]))

@bot.command()
async def roll(ctx, sides: int = 6):
    await ctx.send(f"You rolled {random.randint(1, sides)}")

@bot.command()
async def choose(ctx, *choices):
    await ctx.send(random.choice(choices))

@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(f"User: {member.name} | ID: {member.id}")

@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    await ctx.send(f"Server: {guild.name} | Members: {guild.member_count}")

@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

@bot.command()
async def now(ctx):
    await ctx.send(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

bot.run(TOKEN)
