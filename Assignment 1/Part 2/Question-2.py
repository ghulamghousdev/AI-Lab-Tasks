def getUniqueValues(versionDictionary):
    print("Dictionary List is: ", versionDictionary)
    uniqueValues = [] #Declaring an list to store unique values
    for dictionary in versionDictionary:
        for a in dictionary.values():
            if a not in uniqueValues:
                uniqueValues.append(a)
    return (uniqueValues)
    


#calling the function
sampleData = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
uniqueValues = getUniqueValues(sampleData)
print("Unique Values are :", uniqueValues)
