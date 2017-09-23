import random
#import string
import sys

size = 9
diff = 25
seenboard = []
mineboard = []
pretty = False

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
if (len(sys.argv) != 3):
    print ("Incorrect arguments")
    print ("First arg is size, second is difficulty")
    exit()
size = int(sys.argv[1])
diff = int(sys.argv[2])
genBoard()
showBoard()
print "Generated new board"