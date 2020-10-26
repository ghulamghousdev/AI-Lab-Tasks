listOfList={'2018-CS-30':[('DSA',2),('Algo',2.5),('AI',3)],
            '2018-CS-31':[('DSA',3),('AI',1.5),('PF',2.8)],
            '2018-CS-32':[('OOP',3),('DB',3.5),('AI',2.2)]}



def calcGPA(subjectList):
    if not subjectList:
        return False
    subject = subjectList.pop()
    if subject[0] == "AI" and subject[1] < 2.5:
        return True
    return calcGPA(subjectList)

def DicIterate(listOfList):
    if not listOfList:
        return 0
    student = listOfList.popitem()
    isLessGPA = calcGPA(student[1])
    if isLessGPA:
        return 1+DicIterate(listOfList)
    else:
        return 0+DicIterate(listOfList)

result = DicIterate(listOfList)

print("There are " + str(result) + " Students that have AI GPA less than 2.5")