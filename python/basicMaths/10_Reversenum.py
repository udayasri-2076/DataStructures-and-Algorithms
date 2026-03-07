

def Reversenum(n):
    temp=n
    t_sum=0

    while(n>0):
        d=n%10
        t_sum=t_sum*10+d
        n=n//10
    
    print("The reverse of a number is: ",t_sum)

n=int(input("enter n: "))
Reversenum(n)

'''
enter n: 5678
The reverse of a number is:  8765
'''
