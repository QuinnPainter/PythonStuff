import sys

wordlistFile = "words_alpha.txt"
input = sys.argv[1]
triedMethods = {}


def doNothing(code):
    #Who knows, maybe easier than expected?
    triedMethods["Do nothing"] = [code, checkEnglish(code)]
def binary(code):
    pass


def allMethods(code):
    doNothing(code)
    binary(code)
def readDefinitionFile(f):
    with open(f, 'rU') as in_file:
        return in_file.read().split('\n')
def checkEnglish(string, hardCheck = False):
    #hardCheck=true loops through dictionary, finding words in sentence
    #hardCheck=false loops through sentence, quicker, but requires spacing
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
dictionary = set(readDefinitionFile(wordlistFile))
lengthSortedDictionary = sorted(list(dictionary), key=len)[::-1]#[::-1 reverses the list]

allMethods(input)
print triedMethods
#print readDefinitionFile(binhexFile)