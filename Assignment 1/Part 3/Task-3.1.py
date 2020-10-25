import random

def findIntersection(list1, list2):
    newList = [element for element in list1 if element in list2]
    print("Common elements are: ",newList)

upperRange1 = int(input("Enter Upper range for list1: "))
noOfElements1 = int(input("Enter number of elements for list1: "))

upperRange2 = int(input("Enter Upper range for list2: "))
noOfElements2 = int(input("Enter number of elements for list2: "))

list1 = [random.randrange(1, upperRange1, 1) for i in range(noOfElements1)] 
list2 = [random.randrange(1, upperRange2, 1) for i in range(noOfElements2)] 

print("List1: ", list1)
print("List2: ", list2)

findIntersection(list1, list2)
