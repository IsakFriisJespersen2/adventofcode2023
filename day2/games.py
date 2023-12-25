def check(sets):
    rules = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    game = [x.strip() for draw in sets for x in draw.split(",") ]
    # print(game)
    y = []
    for draw in game:
        value, color = draw.split(" ")
        y.append(rules[color] < int( value ))

    return not any(y)
res = []
with open("./input.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        id, sets = line.split(":")
        sets = sets.split(";")
        # print(id, check(sets))
        if check(sets):
            res.append(int( id.split(" ")[1] ))

print(sum(res))

import re

def sumPowers():
    sumOfPowers = 0
    file = open("input.txt", "r")
    setsRegex = "(?<=:)(.*)"
    redsRegex = "(\\d+)(?=\\sred)"
    greensRegex = "(\\d+)(?=\\sgreen)"
    bluesRegex = "(\\d+)(?=\\sblue)"

    for line in file:
        redMax = 0
        greenMax = 0
        blueMax = 0
        sets = re.search(setsRegex, line).group(0)
        sets = re.split(";", sets)
        for set in sets:
            currRed = re.search(redsRegex, set)
            if(currRed):
                currRed = int(currRed.group(0))
                if(currRed > redMax): redMax = currRed

            currGreen = re.search(greensRegex, set)
            if(currGreen):
                currGreen = int(currGreen.group(0))
                if(currGreen > greenMax): greenMax = currGreen

            currBlue = re.search(bluesRegex, set)
            if(currBlue):
                currBlue = int(currBlue.group(0))
                if(currBlue > blueMax): blueMax = currBlue
        power = redMax * greenMax * blueMax
        sumOfPowers += power

    print("The sum of the powers of the minimum cubes is: " + str(sumOfPowers))

    file.close()

sumPowers()
