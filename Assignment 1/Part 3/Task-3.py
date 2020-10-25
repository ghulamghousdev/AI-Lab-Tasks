def findIntersection(list1, list2):
    newList = [element for element in list1 if element in list2]
    print("Common elements are: ",newList)


list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]    

print("List1: ", list1)
print("List2: ", list2)
findIntersection(list1, list2)
