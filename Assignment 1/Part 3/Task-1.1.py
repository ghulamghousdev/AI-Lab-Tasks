# 1.1  extra part of Task-1
def printList(sampleList):
    newList=[]
    for element in sampleList:
        if element < 5:
            newList.append(element)
    return(newList)
    
sampleList = [1,1,2,3,5,8,13,21,34,55,89]
print("Elements less than 5 are:")
print(printList(sampleList))
