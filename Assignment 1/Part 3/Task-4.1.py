def checkPalindrome(stringToCheck):
    reverseOfString = ''.join(reversed(stringToCheck)) #This will return reverse of string
    flag = False
    if (stringToCheck == reverseOfString):
        flag = True
    if (flag):
        print('Yes, word',stringToCheck,'is a palindrome')
    else:
        print('No, word',stringToCheck,'is not a pallindrome')
    
stringToCheck = "dunud"
checkPalindrome(stringToCheck)
