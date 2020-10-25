listOfList={'2018-CS-30':[('DSA',2),('Algo',2.5),('AI',3)],'2018-CS-31':[('DSA',3),('Algo',3.5),('PF',2.8)],'2018-CS-32':[('OOP',3),('DB',3.5),('PF',2.8)]}

# With for loop
def withForLoop(rec):
    highestNumber = 0
    for a in rec:
        b = rec[a]
        for n in b:
            if n[0] == 'DSA' and n[1] > highestNumber:
                highestNumber = n[1]
    return(highestNumber)


# Without for loop
def withoutForLoop(listOfRecords):
    highestNumber = 0
    index = 0
    keysOfDictionary = list(listOfRecords.keys())
    while index < len(listOfRecords):
        if(listOfRecords[keysOfDictionary[index]][0][1] > highestNumber):
            highestNumber = listOfRecords[keysOfDictionary[index]][0][1]
        index = index + 1
    return (highestNumber)

print(withForLoop(listOfList))
print(withoutForLoop(listOfList))
