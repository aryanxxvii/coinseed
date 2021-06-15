import discord
from discord.ext import commands
import asyncio
from sqlfunc import *
import random
from datetime import datetime
bot_prefix = "cc ", "<@853570284916572170> ", "<@!853570284916572170> "
intents = discord.Intents.all()
client = commands.Bot(command_prefix=bot_prefix, intents=intents)

class colors:
    default = 0
    teal = 0x1abc9c
    dark_teal = 0x11806a
    green = 0x2ecc71
    dark_green = 0x1f8b4c
    blue = 0x3498db
    dark_blue = 0x206694
    purple = 0x9b59b6
    dark_purple = 0x71368a
    magenta = 0xe91e63
    dark_magenta = 0xad1457
    gold = 0xf1c40f
    dark_gold = 0xc27c0e
    orange = 0xe67e22
    dark_orange = 0xa84300
    red = 0xe74c3c
    dark_red = 0x992d22
    lighter_grey = 0x95a5a6
    dark_grey = 0x607d8b
    light_grey = 0x979c9f
    darker_grey = 0x546e7a
    blurple = 0x7289da
    greyple = 0x99aab5


@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def ping(ctx):
    await ctx.send(f"pong {round(client.latency * 1000)}")



@client.command()
async def server(ctx):
    await ctx.send(ctx.guild.name)
    await ctx.send(ctx.guild.icon_url)
    for member in ctx.guild.members:
        await ctx.send(str(member.name) + " " + str(member.id) + " " + str(member.avatar_url))




#-------------------------------------------------------------------------------

# PERSONAL ACC CREATION
# GUILD ACC CREATION
# BAL CHECK
# PROFILE
# DAILY
# LOANS

#-------------------------------------------------------------------------------


@client.event
async def on_ready():
    print("Bot is ready")
    


# AUTO GUILD ACC CREATION
@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("I have joined and created this server's account/")
        break

    #CHECK IF CHANNEL IS IN DGUILDS
    boolx = sql_check_exist("DGUILDS", guild.id)
    #IF EXISTS
    if boolx:
        #PASS
        pass
    #ELSE
    elif boolx:
        #ADD GUILD
        sql_add("DGUILDS", guild.id, ["SeedCoin", ":coin:"])
            


# ACC CREATION
@client.command()
async def addme(ctx, *, attr=None):
    if attr == None:
        #IF MESSAGE GUILD IN DGUILDS
            userexists = sql_check_exist("DGUILDS", ctx.guild.id)
            if userexists == True:
                allcheckwhich = sql_search("DUSERS", ctx.author.id)
                try:
                    userguild = allcheckwhich[0][1]
                except:
                    userguild = allcheckwhich[1]
                if userguild == ctx.guild.id:
                    await ctx.send('You have already registered your account in this server.')
                else:
                    await ctx.send("You have already registered in another server. To change your server type `cc changeserver`.")

            elif userexists == False:

                try:
                    await ctx.send("Are you sure you want to create your account in this server? You can only have your account registered with ONE server at a time. Type `Y` or `y` if you want to proceed.")
                    answer = await client.wait_for(
                        "message",
                        timeout=30,
                        check=lambda message: message.author == ctx.author and message.channel == ctx.channel
                        )
                    ans = answer.content
                    if ans in ["Y", 'y']:
                        now = datetime.now()
                        doc = now.strftime("%Y-%m-%d %H:%M:%S") #input
                        sql_add("DUSERS", ctx.author.id, [ctx.guild.id, doc, 0, None])

                except asyncio.TimeoutError:
                    await ctx.send("You did not respond.")

                    
    elif attr == "bet":
        await ctx.send("This will create your betting account")



@client.command()
async def profile(ctx, user: discord.User = None): #ADD LOANS
    if user == None:
        embedVar = discord.Embed(
        title=str(ctx.author.name), description="", color = colors.green
        )
        embedVar.set_thumbnail(url=ctx.author.avatar_url)
        embedVar.add_field(name="UU Balance :coin:: ", value="3200", inline=False)
        embedVar.add_field(name="Current Bets :money_with_wings::", value="`England | 2 - 1 | 300 UU`\n`Tie | 1 - 1 | 300 UU`", inline=False)
        embedVar.add_field(name="Bets Won :thumbsup:: ", value="1", inline=False)
        embedVar.add_field(name="Euro Cup Favorite :trophy::", value="Germany:flag_de:", inline=False)
        await ctx.send(embed=embedVar)
    elif user != None:
        embedVar = discord.Embed(
        title=str(user.name), description="", color = colors.purple
        )
        embedVar.set_thumbnail(url=user.avatar_url)
        embedVar.add_field(name="UU Balance :coin:: ", value="3200", inline=False)
        embedVar.add_field(name="Current Bets :money_with_wings::", value="`England | 2 - 1 | 300 UU`\n`Tie | 1 - 1 | 300 UU`", inline=False)
        embedVar.add_field(name="Bets Won :thumbsup:: ", value="1", inline=False)
        embedVar.add_field(name="Euro Cup Favorite :trophy::", value="Germany:flag_de:", inline=False)
        
        #embedVar.add_field(name="Rating :star::", value=str(score)+"/10", inline=True)
        await ctx.send(embed=embedVar)



# DAILY  #here search the cdc from dusers table. add 24 hours using timedelta #cdc = coin daily claim
"""
@client.command()
async def daily(ctx):
    if dailytime < currtime + 24:
        update balance + random.randint(100, 500)

"""
#BALTEST
@client.command()
async def baltest(ctx, amount):
    addbal(int(ctx.author.id), int(amount))
    data = sql_search("DUSERS", int(ctx.author.id))[0]
    embedVar = discord.Embed(
        title=str(ctx.author.name), description=str(ctx.author.id)+" "+str(ctx.guild.id), color = colors.green
        )
    embedVar.set_thumbnail(url=ctx.author.avatar_url)
    embedVar.add_field(name="UU Balance :coin:: ", value=str(data[3]), inline=False)
        #embedVar.add_field(name="Current Bets :money_with_wings::", value="`England | 2 - 1 | 300 UU`\n`Tie | 1 - 1 | 300 UU`", inline=False)
        #embedVar.add_field(name="Bets Won :thumbsup:: ", value="1", inline=False)
        #embedVar.add_field(name="Euro Cup Favorite :trophy::", value="Germany:flag_de:", inline=False)
    await ctx.send(embed=embedVar)
    await ctx.send(str(data))

# CHECK 

@client.command()
async def bal(ctx):
    #disuserid, guildid, doc, coinbal, dt = search("USERS", int(ctx.author.id))
    data = sql_search("DUSERS", int(ctx.author.id))[0]
    embedVar = discord.Embed(
        title=str(ctx.author.name), description=str(ctx.author.id)+" "+str(ctx.guild.id), color = colors.green
        )
    embedVar.set_thumbnail(url=ctx.author.avatar_url)
    embedVar.add_field(name="UU Balance :coin:: ", value=str(data[3]), inline=False)
        #embedVar.add_field(name="Current Bets :money_with_wings::", value="`England | 2 - 1 | 300 UU`\n`Tie | 1 - 1 | 300 UU`", inline=False)
        #embedVar.add_field(name="Bets Won :thumbsup:: ", value="1", inline=False)
        #embedVar.add_field(name="Euro Cup Favorite :trophy::", value="Germany:flag_de:", inline=False)
    await ctx.send(embed=embedVar)
    await ctx.send(str(data))


@client.command()
async def bet(ctx):
    await ctx.send("Today's Match: A vs B\nWhich team do you want to bet on?")
    try:
        team = await client.wait_for(
            "message",
            timeout=30,
            check=lambda message: message.author == ctx.author and message.channel == ctx.channel
            )
        teamcon = team.content
        if teamcon.upper() in ["A", "B", "TIE"]:
            try:
                await ctx.send("What's your score prediction? [3 - 2]")
                score = await client.wait_for(
                    "message",
                    timeout=30,
                    check=lambda message: message.author == ctx.author and message.channel == ctx.channel
                    )
                scorecon = score.content
                lscore = scorecon.split("-")
                ascore = int(lscore[0])
                bscore = int(lscore[1])
                try:
                    await ctx.send("Alright, how much do you want to bet? (in UU)")  #dont hardcore symbol
                    betamt = await client.wait_for(
                        "message",
                        timeout=30,
                        check=lambda message: message.author == ctx.author and message.channel == ctx.channel
                        ) #check is balance is there
                    betamtcon = betamt.content
                    betinpup = betamtcon.upper()
                    betinplist = betinpup.split("UU")
                    intbetamt = int(betinplist[0])
                    await ctx.send(f"`Your Bet:{str(teamcon).capitalize()} | {str(ascore)} - {str(bscore)} | {str(intbetamt)} UU`")
                    
                except TypeError:
                    await ctx.send("You gave wrong input \:(")

                    
                    
                    
                    
            except TypeError:
                await ctx.send("You gave wrong input \:(")

                
                
                        
                
            
    except asyncio.TimeoutError:
            await ctx.send("You did not respond.")
    


        
        
        



client.run("ODUzNTcwMjg0OTE2NTcyMTcw.YMXTRg.yVOUfaAivE9oe9hCfOx9S4aFObc")


















    
