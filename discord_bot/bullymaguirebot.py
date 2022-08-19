
from turtle import color
import discord
from discord.ext import commands
from discord.ext.commands import bot


TOKEN = 'OTQ3NTg5NTk4NTA5NDI0NzAx.YhvdlQ.cD7wYFTfhc7kykAG3DMLP2uEKL4'
bot = commands.Bot(command_prefix='!')
client = discord.Client()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def helpme(ctx):
    e= discord.Embed(title = "Welcome to bullyMaguire", description="Here are the commands to for a surprise", color=0xFF0000)
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
    e.set_footer(text="End of Commands")
    await ctx.send(embed=e)



@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send('Hey there, {}!'.format(ctx.message.author.name), file=discord.File('tbdance.gif'))

@bot.command(pass_context=True)
async def time(ctx):
    await ctx.send('Pizza time', file=discord.File('ppp.gif'))
    
@bot.command(pass_context=True)
async def bye(ctx):
    await ctx.send('See ya chump', file=discord.File('seeya.gif'))

@bot.command(pass_context=True)
async def needhelp(ctx):
    await ctx.send('{} I missed the part where that\'s my problem'.format(ctx.message.author.name), file=discord.File('problem.gif'))

@bot.command(pass_context=True)
async def watchout(ctx):
    await ctx.send('~inhale...~', file=discord.File('scream.gif'))

@bot.command(pass_context=True)
async def moves(ctx):
    await ctx.send('Now dig on this', file=discord.File('dig.gif'))

@bot.command(pass_context=True)
async def cry(ctx):
    await ctx.send('awe', file=discord.File('cry.gif'))

@bot.command(pass_context=True)
async def rent(ctx):
    await ctx.send('...', file=discord.File('rent.gif'))

@bot.command(pass_context=True)
async def bully(ctx):
    await ctx.send('dun~dun', file=discord.File('dirt.gif'))

@bot.command(pass_context=True)
async def sorry(ctx):
    await ctx.send('want forgiveness?', file=discord.File('forgive.gif'))

@bot.command(pass_context=True)
async def back(ctx):
    await ctx.send('owwww', file=discord.File('back.gif'))

@bot.command(pass_context=True)
async def bullyback(ctx):
    await ctx.send('sniff', file=discord.File('mecry.gif'))

bot.run(TOKEN)