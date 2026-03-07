

def sum_of_num_inrange(n1,n2): #4,7
    sum=0

    for i in range(n1,n2+1): #4.7
        sum=sum+i #0+4=4 4+5=9 #9+6=15
    print(sum) #4 9 15

n1=int(input("enter n1: "))
n2=int(input("enter n2: "))
sum_of_num_inrange(n1,n2)

'''
enter n1: 4
enter n2: 6
15
'''