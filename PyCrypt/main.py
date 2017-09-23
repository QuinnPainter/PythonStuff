import sys

wordlistFile = "words_alpha.txt"
binhexFile = "binhex.txt"
input = sys.argv[1]

def readDefinitionFile(file):
    with open(file, 'rU') as in_file:
        return in_file.read().split('\n')
wordlist = set(readDefinitionFile(wordlistFile))

print input in wordlist
print readDefinitionFile(binhexFile)