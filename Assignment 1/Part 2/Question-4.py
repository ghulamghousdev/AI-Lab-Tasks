# the following function finds fibonacci series using Lambda Function:
def findFibonacciList(number):
    fibonacciList = [0, 1]
    any(map(lambda _: fibonacciList.append(sum(fibonacciList[-2:])),range(2, number)))
    return fibonacciList[:number]

#calling function
number=int(input("Enter the number: "))
print("Fibonacci series of ",number,": ",findFibonacciList(number)) 
