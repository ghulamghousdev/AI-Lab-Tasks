listOfList={'2018-CS-30':[('DSA',2),('Algo',2.5),('AI',3)],
            '2018-CS-31':[('DSA',3),('AI',1.5),('PF',2.8)],
            '2018-CS-32':[('OOP',3),('DB',3.5),('AI',2.2)]}

def withForLoop(rec):
    count = 0
    for a in rec:
        b = rec[a]
        for n in b:
            if n[0] == 'AI' and n[1] < 2.5:
                count = count + 1
    return(count)

def withoutForLoop(rec):
    count = 0
    a = 0
    keysOfStudentDict = list(rec.keys())
    while a < len(rec):
        b = 0
        while b < 3:
            if(rec[keysOfStudentDict[a]][b][0] == 'AI' and rec[keysOfStudentDict[a]][b][1] < 2.5 ):
                count = count + 1
            b = b + 1
        a = a + 1
    return (count)

print(withForLoop(listOfList))
print(withoutForLoop(listOfList))
