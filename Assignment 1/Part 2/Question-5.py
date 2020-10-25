def convertingToLowerCase(listOfStrings):
    newList=[string.lower() for string in listOfStrings if len(string)>5]
    return newList

# calling function
listOfStrings=["Ghous", "Pakistan", "InterNATIONAL", "OLD", "ExaminAtion"]
print(convertingToLowerCase(listOfStrings))
