
def Factorial(n):

    fact=1

    for i in range(1,n+1):
        fact=fact*i

    print("Factorial of ",n, "is", fact)


n=int(input("enter n:"))
Factorial(n)

'''
enter n:5
Factorial of  5 is 120
'''