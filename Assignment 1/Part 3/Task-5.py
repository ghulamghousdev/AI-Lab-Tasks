def reverseWordsInString(string): 
    wordsInString = string.split(' ')
    reverseString = ' '.join(reversed(wordsInString))
    print("The reversed string is: ", reverseString)

string = str(input("Enter the long string: "))
reverseWordsInString(string)
