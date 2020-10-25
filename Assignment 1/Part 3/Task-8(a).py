def chooseRandomWord(listOfWords):
    import random
    return(''.join(random.choices(listOfWords)))

def main():
    listOfWords = ['APPLE', 'BILBO', 'CHORUSED', 'DISIMAGINE','ENSURING', 'FORMALISING', 'GLITCHES',
                   'HARMINE', 'INDENTATION', 'JACKED', 'KALPACS', 'LAUNDRY', 'MASKED', 'NETTED',
                   'OXFORD', 'PARODY', 'QUOTIENTS', 'RACERS', 'SADNESS', 'THYREOID', 'UNDUE',
                   'VENT', 'WEDGED', 'XERIC', 'YOUTHHOOD', 'ZIFFS']
    word = chooseRandomWord(listOfWords)
    print("The randomly choosed word is:", word)
if __name__ == "__main__":
    main()
