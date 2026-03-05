

def sum_of_num_inrange(n1,n2):
    sum=0

    for i in range(n1,n2+1):
        sum=sum+i
    print(sum)

n1=int(input("enter n1: "))
n2=int(input("enter n2: "))
sum_of_num_inrange(n1,n2)
