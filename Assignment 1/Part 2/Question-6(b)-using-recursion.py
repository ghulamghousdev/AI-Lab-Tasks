listOfList={
    '2018-CS-30':[('DSA',2),('Algo',2.5),('AI',3)],
    '2018-CS-31':[('DSA',3),('Algo',3.5),('PF',2.8)],
    '2018-CS-32':[('OOP',3),('DB',3.5),('PF',2.8)]
}

def calcGPA(subjectList):
    if not subjectList:
        return -1.0
    subject = subjectList.pop()
    if subject[0] == "DSA":
        return subject[1]
    return calcGPA(subjectList)

def DicIterate(listOfList):
    if not listOfList:
        return -1.0
    student = listOfList.popitem()
    DSAGPA = calcGPA(student[1])
    nextDSAGPA = DicIterate(listOfList)
    if nextDSAGPA > DSAGPA:
        return nextDSAGPA
    else:
        return DSAGPA

result = DicIterate(listOfList)

if result != -1.0:
    print("The Max Grade in DSA is >> " + str(result))