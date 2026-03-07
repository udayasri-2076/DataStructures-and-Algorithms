

def Palindrome(n):

    t_sum=0
    temp=n

    while(n>0):
        d=n%10
        t_sum=t_sum*10+d
        n=n//10
    
    if(t_sum==temp):
        print(temp, "is a Palindrome")
    
    else:
        print(temp," is not a Palindrome")

n=int(input("enter n: "))
Palindrome(n)

'''
1.enter n: 121
121 is a Palindrome

2.enter n: 456
456  is not a Palindrome

'''