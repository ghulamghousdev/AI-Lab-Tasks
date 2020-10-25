listOfList={'2018-CS-30':[('DSA',3),('Algo',2.5),('AI',3)],
            '2018-CS-31':[('LA',3),('Algo',3.5),('PF',2.8)],
            '2018-CS-32':[('OOP',3),('DB',3.5),('PF',2.8)]}

def withForLoop(listOfRecords):
    listOfGPA = []
    
    for eachStudent in listOfRecords.values():
        GPA = 0
        for subj in eachStudent:
            GPA  = GPA + subj[1] * 3 
        GPA = GPA / (len(eachStudent) * 3)
        listOfGPA.append(GPA)
    return listOfGPA

def withoutForLoop(listOfRecords):
    listOfGPA = []
    GPA = 0
    a = 0
    keysOfStudentDict = list(listOfRecords.keys())
    while a < len(listOfRecords):
        b = 0
        while b < len(listOfRecords[keysOfStudentDict[a]]):
            GPA = GPA + listOfRecords[keysOfStudentDict[a]][b][1] * 3
            b = b + 1
        GPA = GPA / (len(listOfRecords[keysOfStudentDict[a]]) * 3)
        listOfGPA.append(GPA)
        GPA = 0
        a = a + 1
    return listOfGPA

print(withForLoop(listOfList))
print(withoutForLoop(listOfList))
