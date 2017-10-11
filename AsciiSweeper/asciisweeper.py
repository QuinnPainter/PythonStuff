import random
#import string
import sys

size = 9
diff = 25
seenboard = []
mineboard = []
pretty = True

def genBoard():
    for y in xrange(size):
        mineboard.append("O" * size)
        seenboard.append("O" * size)
    for d in xrange(diff):
        minepos = [random.randint(0, size - 1), random.randint(0, size - 1)]
        mineboard[minepos[0]] = mineboard[minepos[0]][:minepos[1]] + "M" + mineboard[minepos[0]][minepos[1] + 1:]
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
            if (number < 10):
                print str(number) + "  " + seenboard[r]
            else:
                print str(number) + " " + seenboard[r]
        print ""
        print "   " + "".join(str(e)[0] for e in numbers)
        print "   " + "".join(numberrow2)
    else:
        for r in xrange(size):
            print seenboard[r]
def gameLoop():
    action = getInput()
def getInput():
    input = raw_input().lower() #case insensitive
    command = input[:4] #the command is always the first 4 letters: help, exit, flag, bomb
    details = input[4:]
    if command == "help":
        print "Type 'bomb' and coordinates of bomb to trigger, in format 'x, y'"
        print "example: bomb 5, 7"
        print "Type 'flag' before coordinates to flag those coordinates"
        print "example: flag 5, 6"
        print "Type 'exit' to exit"
        return getInput()
    elif command == "exit":
        sys.exit()
    elif command == "bomb":
        print("todo")
    elif command == "flag":
        print("todo")
    else:
        print "Invalid input. Type 'help' for command help."
        return getInput()
if (len(sys.argv) != 3):
    print ("Incorrect arguments")
    print ("First arg is size, second is difficulty")
    exit()
size = int(sys.argv[1])
diff = int(sys.argv[2])
genBoard()
showBoard()
print "Generated new board. Type 'help' for help."
gameLoop()