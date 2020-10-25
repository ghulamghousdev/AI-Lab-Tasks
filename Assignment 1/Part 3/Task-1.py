def printList(sampleList):
    print("Elements less than 5 are:")
    for element in sampleList:
        if element < 5:
            print(element)

sampleList = [1,1,2,3,5,8,13,21,34,55,89]
printList(sampleList)
