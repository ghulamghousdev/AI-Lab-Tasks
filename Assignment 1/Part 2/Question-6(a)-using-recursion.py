listOfList={'2018-CS-30':[('DSA',3),('Algo',2.5),('AI',3)],
            '2018-CS-31':[('LA',3),('Algo',3.5),('PF',2.8)],
            '2018-CS-32':[('OOP',3),('DB',3.5),('PF',2.8)]}


def calcGPA(subjectList):
    if not subjectList:
        return 0
    return subjectList.pop()[1] + calcGPA(subjectList)

def DicIterate(listOfList):
    if not listOfList:
        return 
    student = listOfList.popitem()
    avgGPA = calcGPA(student[1]) / 3
    print("Student Reg. No " + student[0] + " : GPA " + str(avgGPA))
    DicIterate(listOfList)


DicIterate(listOfList)