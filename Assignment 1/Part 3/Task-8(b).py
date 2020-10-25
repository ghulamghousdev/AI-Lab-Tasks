def chooseRandomWord(listOfWords):
    import random
    word = (''.join(random.choices(listOfWords)))
    print(word) # just for practise purposes the word is printed
    guessed = []
    falseGuesses = []
    while True:
        clue = ""
        wordGuessed = ""
        for letter in word:
            if letter in guessed:
                clue = clue + letter+" " # this word is used as we need to print the gussed word as - - - - - 
                wordGuessed = wordGuessed + letter # To store letters to check if the word is guessed or not
            else:
                clue = clue + "_ "
                wordGuessed = wordGuessed + "-"
        if (wordGuessed == word):
            print("Congratulations you guessed the word:", word)
            break
        print("Guess a letter in the word:", clue)
        guessedChar = input()
        if (guessedChar in guessed or guessedChar in falseGuesses):
            print("Already guessed",guessedChar)
        elif (guessedChar in word):
            print("Correct")
            guessed.append(guessedChar)
        else:
            print("Incorrect")
            falseGuesses.append(guessedChar)

            

def main():
    listOfWords = ['APPLE', 'BILBO', 'CHORUSED', 'DISIMAGINE','ENSURING', 'FORMALISING', 'GLITCHES',
                   'HARMINE', 'INDENTATION', 'JACKED', 'KALPACS', 'LAUNDRY', 'MASKED', 'NETTED',
                   'OXFORD', 'PARODY', 'QUOTIENTS', 'RACERS', 'SADNESS', 'THYREOID', 'UNDUE',
                   'VENT', 'WEDGED', 'XERIC', 'YOUTHHOOD', 'ZIFFS']
    chooseRandomWord(listOfWords)
if __name__ == "__main__":
    main()
