import discord
from discord.ext import commands

import logging

import random

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

commandsList = ["$board1", "$board2", "$board3", "$board4", "$board5", "$board6", "$board7", "$board8", "$pickmode", "$pickgame", "$pickgc", "$pickgcwii", "$pickn64", "$bstars", "$duels", "$commands"]

boards5 = {
    1: "Toy Dream",
    2: "Rainbow Dream",
    3: "Pirate Dream",
    4: "Undersea Dream",
    5: "Future Dream",
    6: "Sweet Dream",
    7: "Bowser Nightmare"
}

boards5IMG = {
    1: "assets/ToyDream.webp",
    2: "assets/RainbowDream.webp",
    3: "assets/PirateDream.webp",
    4: "assets/UnderseaDream.webp",
    5: "assets/FutureDream.webp",
    6: "assets/SweetDream.webp",
    7: "assets/BowserNightmare.webp",
}

boards7 = {
    1: "Grand Canal",
    2: "Pagoda Peak",
    3: "Pyramid Park",
    4: "Neon Heights",
    5: "Windmillville",
    6: "Bowser's Enchanted Inferno!"
}

boards7IMG = {
    1: "assets/GrandCanal.jpg",
    2: "assets/PagodaPeak.webp",
    3: "assets/PyramidPark.jpg",
    4: "assets/NeonHeights.webp",
    5: "assets/Windmillville.webp",
    6: "assets/BowserEnchanted.jpg"
}

boards1 = {
    1: "DK's Jungle Adventure",
    2: "Peach's Birthday Cake",
    3: "Yoshi's Tropical Island",
    4: "Wario's Battle Canyon",
    5: "Luigi's Engine Room",
    6: "Mario's Rainbow Castle",
    7: "Bowser's Magma Mountain",
    8: "Eternal Star"
}

boards1IMG = {
    1: "assets/DKAdventure.webp",
    2: "assets/PeachCake.webp",
    3: "assets/YoshiIsland.webp",
    4: "assets/WarioCanyon.webp",
    5: "assets/LuigiEngineRoom.webp",
    6: "assets/MarioCastle.webp",
    7: "assets/BowserMagma.webp",
    8: "assets/EternalStar.webp"
}

boards2 = {
    1: "Pirate Land",
    2: "Western Land",
    3: "Space Land",
    4: "Mystery Land",
    5: "Horror Land",
    6: "Bowser Land"
}

boards2IMG = {
    1: "assets/PirateLand.webp",
    2: "assets/WesternLand.webp",
    3: "assets/SpaceLand.webp",
    4: "assets/MysteryLand.webp",
    5: "assets/HorrorLand.webp",
    6: "assets/BowserLand.webp"
}

boards3 = {
    1: "Chilly Waters",
    2: "Deep Bloober Sea",
    3: "Spiny Desert",
    4: "Woody Woods",
    5: "Creepy Cavern",
    6: "Waluigi's Island"
}

boards3IMG = {
    1: "assets/ChillyWaters.webp",
    2: "assets/BlooberSea.webp",
    3: "assets/SpinyDesert.webp",
    4: "assets/WoodyWoods.webp",
    5: "assets/CreepyCavern.webp",
    6: "assets/WaluigiIsland.webp"
}

boards4 = {
    1: "Toad's Midway Madness",
    2: "Shy Guy's Jungle Jam",
    3: "Goomba's Greedy Gala",
    4: "Boo's Haunted Bash",
    5: "Koopa's Seaside Soiree",
    6: "Bowser's Gnarly Party"
}

boards4IMG = {
    1: "assets/ToadMadness.webp",
    2: "assets/JungleJam.webp",
    3: "assets/GoombaGala.webp",
    4: "assets/HauntedBash.webp",
    5: "assets/SeasideSoiree.webp",
    6: "assets/BowserParty.webp"
}

boards6 = {
    1: "Towering Treetop",
    2: "E.Gadd's Garage",
    3: "Faire Square",
    4: "Snowflake Lake",
    5: "Castaway Bay",
    6: "Clockwork Castle"
}

boards6IMG = {
    1: "assets/ToweringTreetop.jpg",
    2: "assets/GaddGarage.jpg",
    3: "assets/FaireSquare.jpg",
    4: "assets/SnowflakeLake.jpg",
    5: "assets/CastawayBay.jpg",
    6: "assets/ClockworkCastle.jpg"
}

boards8 = {
    1: "DK's Treetop Temple",
    2: "Goomba's Booty Boardwalk",
    3: "King Boo's Haunted Hideaway",
    4: "Shy Guy's Perplex Express",
    5: "Koopa's Tycoon Town",
    6: "Bowser's Warped Orbit"
}

boards8IMG = {
    1: "assets/TreetopTemple.webp",
    2: "assets/GoombaBoardwalk.webp",
    3: "assets/HauntedHideaway.webp",
    4: "assets/PerplexExpress.webp",
    5: "assets/TycoonTown.webp",
    6: "assets/WarpedOrbit.webp"
}

gamesIMG = {
    1: "assets/MP1.webp",
    2: "assets/MP2.jpg",
    3: "assets/MP3.jpg",
    4: "assets/MP4.jpg",
    5: "assets/MP5.webp",
    6: "assets/MP6.jpg",
    7: "assets/MP7.jpg",
    8: "assets/MP8.webp",
}
modes = {
    1: "Classic Mayhem",
    2: "Modern Mayhem"
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

    activity = discord.Game(name="type $commands to get a list of commands")  # Example status: "Playing with the API!"
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.command(name="board5")
async def board5(ctx):
    randint = random.randint(1,7)
    selection = boards5[randint]
    file_path = boards5IMG[randint]
    
    match randint:
        case 1:
            file = discord.File(file_path, filename="ToyDream.webp")
            await ctx.send("## The Selected Mario Party 5 Board is... " + selection, file=file)
        case 2:
            file = discord.File(file_path, filename="RainbowDream.webp")
            await ctx.send("## The Selected Mario Party 5 Board is... " + selection, file=file)
        case 3:
            file = discord.File(file_path, filename="PirateDream.webp")
            await ctx.send("## The Selected Mario Party 5 Board is... " + selection, file=file)
        case 4:
            file = discord.File(file_path, filename="UnderseaDream.webp")
            await ctx.send("## The Selected Mario Party 5 Board is... " + selection, file=file)
        case 5:
            file = discord.File(file_path, filename="FutureDream.webp")
            await ctx.send("## The Selected Mario Party 5 Board is... " + selection, file=file)
        case 6:
            file = discord.File(file_path, filename="SweetDream.webp")
            await ctx.send("## The Selected Mario Party 5 Board is... " + selection, file=file)
        case 7:
            file = discord.File(file_path, filename="BowserNightmare.webp")
            await ctx.send("## The Selected Mario Party 5 Board is... " + selection, file=file)

@bot.command(name="board7")
async def board7(ctx):
    randint = random.randint(1,6)
    selection = boards7[randint]
    file_path = boards7IMG[randint]
    
    match randint:
        case 1:
            file = discord.File(file_path, filename="GrandCanal.jpg")
            await ctx.send("## The Selected Mario Party 7 Board is... " + selection, file=file)
        case 2:
            file = discord.File(file_path, filename="PagodaPeak.webp")
            await ctx.send("## The Selected Mario Party 7 Board is... " + selection, file=file)
        case 3:
            file = discord.File(file_path, filename="PyramidPark.jpg")
            await ctx.send("## The Selected Mario Party 7 Board is... " + selection, file=file)
        case 4:
            file = discord.File(file_path, filename="NeonHeights.webp")
            await ctx.send("## The Selected Mario Party 7 Board is... " + selection, file=file)
        case 5:
            file = discord.File(file_path, filename="Windmillville.webp")
            await ctx.send("## The Selected Mario Party 7 Board is... " + selection, file=file)
        case 6:
            file = discord.File(file_path, filename="BowserEnchanted.jpg")
            await ctx.send("## The Selected Mario Party 7 Board is... " + selection, file=file)

@bot.command(name="board1")
async def board1(ctx):
    randint = random.randint(1,8)
    selection = boards1[randint]
    file_path = boards1IMG[randint]
    
    match randint:
        case 1:
            file = discord.File(file_path, filename="DKAdventure.webp")
            await ctx.send("## The Selected Mario Party 1 Board is... " + selection, file=file)
        case 2:
            file = discord.File(file_path, filename="PeachCake.webp")
            await ctx.send("## The Selected Mario Party 1 Board is... " + selection, file=file)
        case 3:
            file = discord.File(file_path, filename="YoshiIsland.webp")
            await ctx.send("## The Selected Mario Party 1 Board is... " + selection, file=file)
        case 4:
            file = discord.File(file_path, filename="WarioCanyon.webp")
            await ctx.send("## The Selected Mario Party 1 Board is... " + selection, file=file)
        case 5:
            file = discord.File(file_path, filename="LuigiEngineRoom.webp")
            await ctx.send("## The Selected Mario Party 1 Board is... " + selection, file=file)
        case 6:
            file = discord.File(file_path, filename="MarioCastle.webp")
            await ctx.send("## The Selected Mario Party 1 Board is... " + selection, file=file)
        case 7:
            file = discord.File(file_path, filename="BowserMagma.webp")
            await ctx.send("## The Selected Mario Party 1 Board is... " + selection, file=file)
        case 8:
            file = discord.File(file_path, filename="EternalStar.webp")
            await ctx.send("## The Selected Mario Party 1 Board is... " + selection, file=file)

@bot.command(name="board2")
async def board2(ctx):
    randint = random.randint(1,6)
    selection = boards2[randint]
    file_path = boards2IMG[randint]
    
    match randint:
        case 1:
            file = discord.File(file_path, filename="PirateLand.webp")
            await ctx.send("## The Selected Mario Party 2 Board is... " + selection, file=file)
        case 2:
            file = discord.File(file_path, filename="WesternLand.webp")
            await ctx.send("## The Selected Mario Party 2 Board is... " + selection, file=file)
        case 3:
            file = discord.File(file_path, filename="SpaceLand.webp")
            await ctx.send("## The Selected Mario Party 2 Board is... " + selection, file=file)
        case 4:
            file = discord.File(file_path, filename="MysteryLand.webp")
            await ctx.send("## The Selected Mario Party 2 Board is... " + selection, file=file)
        case 5:
            file = discord.File(file_path, filename="HorrorLand.webp")
            await ctx.send("## The Selected Mario Party 2 Board is... " + selection, file=file)
        case 6:
            file = discord.File(file_path, filename="BowserLand.webp")
            await ctx.send("## The Selected Mario Party 2 Board is... " + selection, file=file)

@bot.command(name="board3")
async def board3(ctx):
    randint = random.randint(1,6)
    selection = boards3[randint]
    file_path = boards3IMG[randint]
    
    match randint:
        case 1:
            file = discord.File(file_path, filename="ChillyWaters.webp")
            await ctx.send("## The Selected Mario Party 3 Board is... " + selection, file=file)
        case 2:
            file = discord.File(file_path, filename="BlooberSea.webp")
            await ctx.send("## The Selected Mario Party 3 Board is... " + selection, file=file)
        case 3:
            file = discord.File(file_path, filename="SpinyDesert.webp")
            await ctx.send("## The Selected Mario Party 3 Board is... " + selection, file=file)
        case 4:
            file = discord.File(file_path, filename="WoodyWoods.webp")
            await ctx.send("## The Selected Mario Party 3 Board is... " + selection, file=file)
        case 5:
            file = discord.File(file_path, filename="CreepyCavern.webp")
            await ctx.send("## The Selected Mario Party 3 Board is... " + selection, file=file)
        case 6:
            file = discord.File(file_path, filename="WaluigiIsland.webp")
            await ctx.send("## The Selected Mario Party 3 Board is... " + selection, file=file)

@bot.command(name="board4")
async def board4(ctx):
    randint = random.randint(1,6)
    selection = boards4[randint]
    file_path = boards4IMG[randint]
    
    match randint:
        case 1:
            file = discord.File(file_path, filename="ToadMadness.webp")
            await ctx.send("## The Selected Mario Party 4 Board is... " + selection, file=file)
        case 2:
            file = discord.File(file_path, filename="JungleJam.webp")
            await ctx.send("## The Selected Mario Party 4 Board is... " + selection, file=file)
        case 3:
            file = discord.File(file_path, filename="GoombaGala.webp")
            await ctx.send("## The Selected Mario Party 4 Board is... " + selection, file=file)
        case 4:
            file = discord.File(file_path, filename="HauntedBash.webp")
            await ctx.send("## The Selected Mario Party 4 Board is... " + selection, file=file)
        case 5:
            file = discord.File(file_path, filename="SeasideSoiree.webp")
            await ctx.send("## The Selected Mario Party 4 Board is... " + selection, file=file)
        case 6:
            file = discord.File(file_path, filename="BowserParty.webp")
            await ctx.send("## The Selected Mario Party 4 Board is... " + selection, file=file)

@bot.command(name="board6")
async def board6(ctx):
    randint = random.randint(1,6)
    selection = boards6[randint]
    file_path = boards6IMG[randint]
    
    match randint:
        case 1:
            file = discord.File(file_path, filename="ToweringTreetop.jpg")
            await ctx.send("## The Selected Mario Party 6 Board is... " + selection, file=file)
        case 2:
            file = discord.File(file_path, filename="GaddGarage.jpg")
            await ctx.send("## The Selected Mario Party 6 Board is... " + selection, file=file)
        case 3:
            file = discord.File(file_path, filename="FaireSquare.jpg")
            await ctx.send("## The Selected Mario Party 6 Board is... " + selection, file=file)
        case 4:
            file = discord.File(file_path, filename="SnowflakeLake.jpg")
            await ctx.send("## The Selected Mario Party 6 Board is... " + selection, file=file)
        case 5:
            file = discord.File(file_path, filename="CastawayBay.jpg")
            await ctx.send("## The Selected Mario Party 6 Board is... " + selection, file=file)
        case 6:
            file = discord.File(file_path, filename="ClockworkCastle.jpg")
            await ctx.send("## The Selected Mario Party 6 Board is... " + selection, file=file)

@bot.command(name="board8")
async def board8(ctx):
    randint = random.randint(1,6)
    selection = boards8[randint]
    file_path = boards8IMG[randint]
    
    match randint:
        case 1:
            file = discord.File(file_path, filename="TreetopTemple.webp")
            await ctx.send("## The Selected Mario Party 8 Board is... " + selection, file=file)
        case 2:
            file = discord.File(file_path, filename="GoombaBoardwalk.webp")
            await ctx.send("## The Selected Mario Party 8 Board is... " + selection, file=file)
        case 3:
            file = discord.File(file_path, filename="HauntedHideaway.webp")
            await ctx.send("## The Selected Mario Party 8 Board is... " + selection, file=file)
        case 4:
            file = discord.File(file_path, filename="PerplexExpress.webp")
            await ctx.send("## The Selected Mario Party 8 Board is... " + selection, file=file)
        case 5:
            file = discord.File(file_path, filename="TycoonTown.webp")
            await ctx.send("## The Selected Mario Party 8 Board is... " + selection, file=file)
        case 6:
            file = discord.File(file_path, filename="WarpedOrbit.webp")
            await ctx.send("## The Selected Mario Party 8 Board is... " + selection, file=file)

@bot.command(name="pickgame")
async def pickgame(ctx):
    randint = random.randint(1,8)
    file_path = gamesIMG[randint]

    match randint:
        case 1:
            file = discord.File(file_path, filename="MP1.webp")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 2:
            file = discord.File(file_path, filename="MP2.jpg")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 3:
            file = discord.File(file_path, filename="MP3.jpg")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 4:
            file = discord.File(file_path, filename="MP4.jpg")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 5:
            file = discord.File(file_path, filename="MP5.webp")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 6:
            file = discord.File(file_path, filename="MP6.jpg")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 7:
            file = discord.File(file_path, filename="MP7.jpg")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 8:
            file = discord.File(file_path, filename="MP8.webp")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)

@bot.command(name="pickgc")
async def pickgame(ctx):
    randint = random.randint(4,7)
    file_path = gamesIMG[randint]

    match randint:
        case 4:
            file = discord.File(file_path, filename="MP4.jpg")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 5:
            file = discord.File(file_path, filename="MP5.webp")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 6:
            file = discord.File(file_path, filename="MP6.jpg")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 7:
            file = discord.File(file_path, filename="MP7.jpg")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)

@bot.command(name="pickgcwii")
async def pickgame(ctx):
    randint = random.randint(4,8)
    file_path = gamesIMG[randint]

    match randint:
        case 4:
            file = discord.File(file_path, filename="MP4.jpg")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 5:
            file = discord.File(file_path, filename="MP5.webp")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 6:
            file = discord.File(file_path, filename="MP6.jpg")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 7:
            file = discord.File(file_path, filename="MP7.jpg")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 8:
            file = discord.File(file_path, filename="MP8.webp")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)

@bot.command(name="pickn64")
async def pickgame(ctx):
    randint = random.randint(1,3)
    file_path = gamesIMG[randint]

    match randint:
        case 1:
            file = discord.File(file_path, filename="MP1.webp")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 2:
            file = discord.File(file_path, filename="MP2.jpg")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)
        case 3:
            file = discord.File(file_path, filename="MP3.jpg")
            await ctx.send("## The Selected Game is... Mario Party " + str(randint), file=file)

@bot.command(name="pickmode")
async def pickmode(ctx):
    randint = random.randint(1,2)

    await ctx.send("## The Selected Mode is... " + modes[randint])

@bot.command(name="bstars")
async def bstars(ctx):
    randint = random.randint(1,3)

    if randint == 1:
        
        await ctx.send("## Bonus Stars Will Be... Off")
    elif randint == 2:
        await ctx.send("## Bonus Stars Will Be... On")
    else:
        await ctx.send("## Bonus Stars Will Be... Ztars")

@bot.command(name="duels")
async def duels(ctx):
    randint = random.randint(1,3)

    if randint == 1:
        await ctx.send("## Same Space Duels is set to... Always")
    elif randint == 2:
        await ctx.send("## Same Space Duels is set to... Vanilla")
    else:
        await ctx.send("## Same Space Duels is set to... Never")

@bot.command(name="commands")
async def commands(ctx):
    commandsString = ""

    for _command in commandsList:
        commandsString += _command
        commandsString += "\n"

    await ctx.send("## Here's The List of Commands!")
    await ctx.send(commandsString)