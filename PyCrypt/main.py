import sys

binaryFile = "methods/binary.txt"
hexFile = "methods/hexadecimal.txt"
morseFile = "methods/morse.txt"

wordlistFile = "words_alpha.txt"
input = sys.argv[1]
triedMethods = {}


def doNothing(code):
    #Who knows, maybe easier than expected?
    triedMethods["Doing nothing"] = [code, checkEnglish(code)]
def binary(code):
    bin = parseDefinitionLines(readDefinitionLines(binaryFile))
    formattedCode = ""
    for number in code:
        if (number == "0" or number == "1"):
            formattedCode += number
    characters = split_every(8, formattedCode)
    output = ""
    for c in characters:
        try:
            output += bin[c]
        except KeyError:
            #This string is not binary
            pass
    triedMethods["Binary"] = [output, checkEnglish(output)]
def morse(code):
    mor = parseDefinitionLines(readDefinitionLines(morseFile))
    formattedCode = ""
    for c in code:
        if (c == "-" or c == "." or c == " "):
            formattedCode += c
    characters = formattedCode.split(" ")
    output = ""
    for c in characters:
        try:
            output += mor[c]
        except KeyError:
            #This string is not morse
            pass
    triedMethods["Morse code"] = [output, checkEnglish(output)]
    
def allMethods(code):
    doNothing(code)
    binary(code)
    morse(code)
def split_every(n, s):
    #Splits a string s every n characters
    return [ s[i:i+n] for i in xrange(0, len(s), n) ]
def readDefinitionLines(f):
    with open(f, 'rU') as in_file:
        return in_file.read().split('\n')
def parseDefinitionLines(lines):
    definitions = {}
    for line in lines:
        definitions[line[2:]] = line[0]
    return definitions
def checkEnglish(string, hardCheck = True):
    #hardCheck=true loops through dictionary, finding words in sentence
    #hardCheck=false loops through sentence, requires spacing
    englishWordCount = 0
    if (hardCheck):
        for word in lengthSortedDictionary:
            if (word in string):
                englishWordCount += string.count(word)
                string = string.replace(word, "")
    else:
        words = string.split(" ")
        for word in words:
            if(word in dictionary):
                englishWordCount += 1
    return englishWordCount
def getBestSolution():
    currentBest = ["", "", -1]
    for key, value in triedMethods.iteritems():
        if value[1] > currentBest[2]:
            currentBest[0] = key
            currentBest[1] = value[0]
            currentBest[2] = value[1]
    print currentBest[0] + " is the best solution, with " + str(currentBest[2]) + " words"
    print currentBest[1]
dictionary = set(readDefinitionLines(wordlistFile))
lengthSortedDictionary = sorted(list(dictionary), key=len)[::-1]#[::-1] reverses the list

allMethods(input)
#print triedMethods
getBestSolution()