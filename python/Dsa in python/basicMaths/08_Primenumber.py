


def Primenumber(n):
    
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1

    if(c==2):
        print(n," is a prime number")
    else:
        print(n," is not a primenumber")

n=int(input("enter n: "))
Primenumber(n)

'''
enter n: 5
5  is a prime number
'''