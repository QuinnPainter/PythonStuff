import random
#import string
import sys
import colorama

size = 9
diff = 25
seenboard = []
mineboard = []
groundchar = "O"
minechar = "M"
flagchar = "F"
groundcolour = colorama.Fore.GREEN
minecolour = colorama.Fore.YELLOW
flagcolour = colorama.Fore.RED
pretty = True

def genBoard():
    for y in xrange(size):
        mineboard.append(groundchar * size)
        seenboard.append(groundchar * size)
    for d in xrange(diff):
        minepos = [random.randint(0, size - 1), random.randint(0, size - 1)]
        mineboard[minepos[0]] = mineboard[minepos[0]][:minepos[1]] + minechar + mineboard[minepos[0]][minepos[1] + 1:]
def showBoard():
    if (pretty == True):
        numbers = range(1, size + 1)
        numberrow2 = []
        for i in xrange(len(numbers)):
            if (numbers[i] > 9):
                numberrow2.append(str(numbers[i])[1])
            else:
                numberrow2.append(" ")
        for r in xrange(size):
            number = numbers[::-1][r]
            printrow = ""
            for c in seenboard[r]:
                if c == groundchar:
                    printrow += groundcolour + c
                elif c == minechar:
                    printrow += minecolour + c
                elif c == flagchar:
                    printrow += flagcolour + c
            if (number < 10):
                print str(number) + "  " + printrow
            else:
                print str(number) + " " + printrow
        print ""
        print "   " + "".join(str(e)[0] for e in numbers)
        print "   " + "".join(numberrow2)
    else:
        for r in xrange(size):
            print seenboard[r]
def gameLoop():
    global seenboard
    action = getInput()
    if action[0] == "flag":
        l = list(seenboard[size - action[2]]) #Convert selected row to list so we can assign a single character, also reverse it so input goes from bottom left instead of top left
        l[action[1] - 1] = flagchar
        seenboard[size - action[2]] = "".join(l) #...and convert it back to string
        showBoard()
    gameLoop()
def getInput():
    input = raw_input().lower() #case insensitive
    command = input[:4] #the command is always the first 4 letters: help, exit, flag
    details = input[4:]
    if command == "help":
        print "Type coordinates, in format 'x, y', to dig a tile"
        print "example: 5, 7"
        print "Type 'flag' before coordinates to flag those coordinates"
        print "example: flag 5, 6"
        print "Type 'exit' to exit"
        return getInput()
    elif command == "exit":
        sys.exit()
    elif command == "flag":
        x, y = cleanCoordinates(details)
        if x == -999:
            print "Invalid input. Type 'help' for command help."
            return getInput()
        elif x == -998:
            print "Coordinates too small or too large. Type 'help' for command help."
            return getInput()
        return ["flag", x, y]
    elif not cleanCoordinates(input)[0] == -999:
        x, y = cleanCoordinates(input)
        if x == -998:
            print "Coordinates too small or too large. Type 'help' for command help."
            return getInput()
        return ["bomb", x, y]
    else:
        print "Invalid input. Type 'help' for command help."
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
if (len(sys.argv) != 3):
    print ("Incorrect arguments")
    print ("First arg is size, second is difficulty")
    exit()
size = int(sys.argv[1])
diff = int(sys.argv[2])
colorama.init(autoreset=True) #Init script required for Colorama
genBoard()
showBoard()
print "Generated new board. Type 'help' for help."
gameLoop()