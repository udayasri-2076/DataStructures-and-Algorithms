
def SumOfDigits(n):

    t_sum=0
    while(n>0):
        d=n%10
        t_sum=t_sum+d
        n=n//10

    print("Sum of the Digits is: ",t_sum)

n=int(input("entr n: "))
SumOfDigits(n)

'''
entr n: 789
Sum of the Digits is:  24
'''