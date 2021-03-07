import random
#import string
import sys

size = 9
diff = 25
seenboard = []
mineboard = []
groundchar = "O"
minechar = "M"
flagchar = "F"
pretty = True

def genBoard():
    for y in range(size):
        mineboard.append(" " * size)
        seenboard.append(groundchar * size)
    availableMinePositions = []
    for y in range(size):
        for x in range(size):
            availableMinePositions.append(str(x) + str(y))
    for d in range(diff):
        mineposInList = random.randint(0, len(availableMinePositions) - 1)
        minepos = [-1, -1]
        minepos[0] = int(availableMinePositions[mineposInList][0])
        minepos[1] = int(availableMinePositions[mineposInList][1])
        del availableMinePositions[mineposInList]
        #minepos = [random.randint(0, size - 1), random.randint(0, size - 1)]
        mineboard[minepos[0]] = mineboard[minepos[0]][:minepos[1]] + minechar + mineboard[minepos[0]][minepos[1] + 1:]
    for position in availableMinePositions:
        #Loop through every coordinate that is not a bomb, and assign it a number
        #If it is not a number or a bomb, it will remain a blank space
        position = [int(position[0]), int(position[1])]
        numberValue = 0
        tilesToCheck = ["TL", "T", "TR", "L", "R", "BL", "B", "BR"]# Protective measures to prevent array index errors and list wrap
        if position[1] == 0:
            #mineboard[position[0]] = mineboard[position[0]][:position[1]] + "L"+ mineboard[position[0]][position[1] + 1:]
            #left edge
            tilesToCheck.remove("TL")
            tilesToCheck.remove("L")
            tilesToCheck.remove("BL")
        if position[1] == size - 1:
            #mineboard[position[0]] = mineboard[position[0]][:position[1]] + "R"+ mineboard[position[0]][position[1] + 1:]
            #right edge
            tilesToCheck.remove("TR")
            tilesToCheck.remove("R")
            tilesToCheck.remove("BR")
        if position[0] == 0:
            #mineboard[position[0]] = mineboard[position[0]][:position[1]] + "T"+ mineboard[position[0]][position[1] + 1:]
            #top edge
            try:
                tilesToCheck.remove("TL")
            except ValueError:
                pass #already removed
            tilesToCheck.remove("T")
            try:
                tilesToCheck.remove("TR")
            except ValueError:
                pass #already removed
        if position[0] == size - 1:
            #mineboard[position[0]] = mineboard[position[0]][:position[1]] + "B"+ mineboard[position[0]][position[1] + 1:]
            #bottom edge
            try:
                tilesToCheck.remove("BL")
            except ValueError:
                pass #already removed
            tilesToCheck.remove("B")
            try:
                tilesToCheck.remove("BR")
            except ValueError:
                pass #already removed
        for tile in tilesToCheck:
            relativeCoordinates = [0, 0]
            if tile == "TL":
                relativeCoordinates = [-1, -1]
            elif tile == "T":
                relativeCoordinates = [0, -1]
            elif tile == "TR":
                relativeCoordinates = [1, -1]
            elif tile == "L":
                relativeCoordinates = [-1, 0]
            elif tile == "R":
                relativeCoordinates = [1, 0]
            elif tile == "BL":
                relativeCoordinates = [-1, 1]
            elif tile == "B":
                relativeCoordinates = [0, 1]
            elif tile == "BR":
                relativeCoordinates = [1, 1]
            checkPosition = [position[0] + relativeCoordinates[1], position[1] + relativeCoordinates[0]]
            if mineboard[checkPosition[0]][checkPosition[1]] == minechar:
                numberValue += 1
        #if (mineboard[position[1]][position[0] - 1] == minechar): #directly to left
        #    numberValue += 1
        #if (mineboard[position[1]][position[0] + 1] == minechar): #directly to right
        #    numberValue += 1
        
        if numberValue > 0:
            mineboard[position[0]] = mineboard[position[0]][:position[1]] + str(numberValue)+ mineboard[position[0]][position[1] + 1:]
def showBoard():
    if (pretty == True):
        numbers = range(1, size + 1)
        numberrow2 = []
        for i in range(len(numbers)):
            if (numbers[i] > 9):
                numberrow2.append(str(numbers[i])[1])
            else:
                numberrow2.append(" ")
        for r in range(size):
            number = numbers[::-1][r]
            printrow = ""
            for c in seenboard[r]: #Replace with "mineboard" to see the mines for debugging
                if c == groundchar:
                    printrow += groundcolour + c
                elif c == minechar:
                    printrow += minecolour + c
                elif c == flagchar:
                    printrow += flagcolour + c
                else:
                    printrow += numcolour + c
            if (number < 10):
                print(str(number) + "  " + printrow)
            else:
                print(str(number) + " " + printrow)
        print("")
        print("   " + "".join(str(e)[0] for e in numbers))
        print("   " + "".join(numberrow2))
    else:
        #for r in range(size):
            #print(mineboard[r])
        for r in range(size):
            print(seenboard[r])
def gameLoop():
    global seenboard
    action = getInput()
    if action[0] == "flag":
        setCharAtPosition(action[1], action[2], flagchar)
        showBoard()
    elif action[0] == "dig":
        #print (mineboard[size - action[2]][action[1]])
        if mineboard[size - action[2]][action[1] - 1] == minechar:
            lose(action[1], action[2])
        reveal(action[1], action[2])
        showBoard()
    gameLoop()
def lose(bombx, bomby):
    print ("You lose") #todo
    sys.exit()
def setCharAtPosition(x, y, char):
    l = list(seenboard[size - y]) #Convert selected row to list so we can assign a single character, also reverse it so input goes from bottom left instead of top left
    l[x - 1] = char
    seenboard[size - y] = "".join(l) #...and convert it back to string
def reveal(x, y):
    #if not seenboard[size - y][x - 1] == groundchar:
     #   return
    revealOneTile(x, y)
    if mineboard[size - y][x - 1] == " ":
        nearTiles = NearbyTileCoords(x, y)
        for tile in nearTiles:
            #print str(seenboard[size - tile[1]][tile[0] - 1])
            if seenboard[size - tile[0]][tile[1] - 1] == groundchar:
                #pass
                reveal(tile[1], tile[0])
    else: #Must be a number
        pass #No need to do anything here yet
def revealOneTile(x, y):
    setCharAtPosition(x, y, mineboard[size - y][x - 1])
def NearbyTileCoords(x, y):
    relativeCoords = []
    worldCoords = []
    tilesToCheck = ["TL", "T", "TR", "L", "R", "BL", "B", "BR"]# Protective measures to prevent array index errors and list wrap
    if x-1 == 0:
        #mineboard[position[0]] = mineboard[position[0]][:position[1]] + "L"+ mineboard[position[0]][position[1] + 1:]
        #left edge
        tilesToCheck.remove("TL")
        tilesToCheck.remove("L")
        tilesToCheck.remove("BL")
    if x-1 == size - 1:
        #mineboard[position[0]] = mineboard[position[0]][:position[1]] + "R"+ mineboard[position[0]][position[1] + 1:]
        #right edge
        tilesToCheck.remove("TR")
        tilesToCheck.remove("R")
        tilesToCheck.remove("BR")
    if y-1 == 0:
        #mineboard[position[0]] = mineboard[position[0]][:position[1]] + "T"+ mineboard[position[0]][position[1] + 1:]
        #top edge
        try:
            tilesToCheck.remove("TL")
        except ValueError:
            pass #already removed
        tilesToCheck.remove("T")
        try:
            tilesToCheck.remove("TR")
        except ValueError:
            pass #already removed
    if y-1 == size - 1:
        #mineboard[position[0]] = mineboard[position[0]][:position[1]] + "B"+ mineboard[position[0]][position[1] + 1:]
        #bottom edge
        try:
            tilesToCheck.remove("BL")
        except ValueError:
            pass #already removed
        tilesToCheck.remove("B")
        try:
            tilesToCheck.remove("BR")
        except ValueError:
            pass #already removed
    for tile in tilesToCheck:
        if tile == "TL":
            relativeCoords.append([-1, -1])
        elif tile == "T":
            relativeCoords.append([0, -1])
        elif tile == "TR":
            relativeCoords.append([1, -1])
        elif tile == "L":
            relativeCoords.append([-1, 0])
        elif tile == "R":
            relativeCoords.append([1, 0])
        elif tile == "BL":
            relativeCoords.append([-1, 1])
        elif tile == "B":
            relativeCoords.append([0, 1])
        elif tile == "BR":
            relativeCoords.append([1, 1])
    for c in relativeCoords:
        worldCoords.append([y + c[1], x + c[0]])
    #print (worldCoords)
    return worldCoords
def getInput():
    cmdInput = input().lower() #case insensitive
    command = cmdInput[:4] #the command is always the first 4 letters: help, exit, flag
    details = cmdInput[4:]
    if command == "help":
        print ("Type coordinates, in format 'x, y', to dig a tile")
        print ("example: 5, 7")
        print ("Type 'flag' before coordinates to flag those coordinates")
        print ("example: flag 5, 6")
        print ("Type 'exit' to exit")
        return getInput()
    elif command == "exit":
        sys.exit()
    elif command == "flag":
        x, y = cleanCoordinates(details)
        if x == -999:
            print ("Invalid input. Type 'help' for command help.")
            return getInput()
        elif x == -998:
            print ("Coordinates too small or too large. Type 'help' for command help.")
            return getInput()
        return ["flag", x, y]
    elif not cleanCoordinates(cmdInput)[0] == -999:
        x, y = cleanCoordinates(cmdInput)
        if x == -998:
            print ("Coordinates too small or too large. Type 'help' for command help.")
            return getInput()
        return ["dig", x, y]
    else:
        print ("Invalid input. Type 'help' for command help.")
        return getInput()
def cleanCoordinates(s):
    try:
        xstring, ystring = s.split(",")
        x = int(xstring)
        y = int(ystring)
    except ValueError:
        return [-999, -999]
    if (x > size or y > size or x < 1 or y < 1):
        return [-998, -998]
    return [x, y]
if (len(sys.argv) != 4 or sys.argv[1] == "help"):
    #print ("Incorrect arguments")
    print ("First arg is size, second is difficulty (number of mines)")
    print ("Third argument is to present with colour and numbers, True or False")
    print ("Example - python asciisweeper.py 5 5 True")
    exit()
size = int(sys.argv[1])
diff = int(sys.argv[2])
pretty = sys.argv[3]
if pretty == "True":
    import colorama
    colorama.init(autoreset=True) #Init script required for Colorama
    groundcolour = colorama.Fore.GREEN# + colorama.Back.GREEN
    minecolour = colorama.Fore.YELLOW
    flagcolour = colorama.Fore.RED
    numcolour = colorama.Fore.YELLOW
    pretty = True
elif pretty == "False":
    pretty = False
else:
    print ("Third argument must be True or False")
genBoard()
showBoard()
print ("Generated new board. Type 'help' for help.")
gameLoop()