#create a random word from words.txt
import random

wordsFile = open("words.txt", "r")

wordsList = []
myWord = wordsFile.readline()
while myWord != '':
        #as long as there are more words,
        #put the word in the list and read another

        wordsList.append(myWord)
	myWord = wordsFile.readline()

listLength = len(wordsList)

randint = random.randint(0, listLength)
randWord = wordsList[randint]
print("Here is a random word:")
print(randWord)





