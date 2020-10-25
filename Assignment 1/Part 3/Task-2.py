def printDivisors(n):
    newList = [element for element in range(1,n) if n%element == 0]
    return(newList)
    
number = int(input("Enter the number whose divisors you want to get: "))
print("Divisors of ",number," are:")
print(printDivisors(number))
