import os

print("matches started")

bot = "basic_bot,T,python"
enemyBots = ["loser_bot,T,python"]
mapList = ["InsideAndOutAIE", "MoondanceAIE", "StargazersAIE", "WaterfallAIE", "HardwireAIE", "BerlingradAIE"]

gameCount = 0
totalGames = len(enemyBots) * len(mapList)

print("starting " + str(totalGames) + " games")

for enemyBot in enemyBots:
    for map in mapList:
        gameCount = gameCount + 1
        matchString = bot + "," + enemyBot + "," + map
        f = open("matches", "w")
        f.write(matchString)
        f.close()
        print("starting match " + str(gameCount) + " of " + str(totalGames) + ": " + matchString)
        os.system('cmd /c "docker-compose up"')

print("matches ended")
