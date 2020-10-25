def printList(sampleList, n):
    return([element for element in sampleList if element < n])


sampleList = [1,1,2,3,5,8,13,21,34,55,89]
number = int(input("Enter the number: "))
print("Elements less than ",number," are:")
print(printList(sampleList, number))
