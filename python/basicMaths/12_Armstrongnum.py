

def Armstrongnum(n):

    t_sum=0
    temp=n

    while(n>0):
        d=n%10
        t_sum=t_sum+(d*d*d)
        n=n//10
    
    if(t_sum==temp):
        print(temp, "is a Armstrong number")

    else:
        print(temp, "is not a Armstrong number")

n=int(input("enter n: "))
Armstrongnum(n)


'''
1.enter n: 343
343 is not a Armstrong number

2.enter n: 153
153 is a Armstrong number
'''