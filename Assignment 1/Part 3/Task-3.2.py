import random
upperRange1 = int(input("Enter Upper range for list1: "))
noOfElements1 = int(input("Enter number of elements for list1: "))
upperRange2 = int(input("Enter Upper range for list2: "))
noOfElements2 = int(input("Enter number of elements for list2: "))
list1 = [random.randrange(1, upperRange1, 1) for i in range(noOfElements1)] 
list2 = [random.randrange(1, upperRange2, 1) for i in range(noOfElements2)] 
print("List1: ", list1)
print("List2: ", list2)

# The main logic is implemented in this one line of code aS the task was to implement it in one line
print("Common elements in both lists are:",[element for element in list1 if element in list2])



