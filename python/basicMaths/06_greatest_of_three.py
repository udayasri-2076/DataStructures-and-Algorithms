

def greatest_of_three(n1,n2,n3):

    print(n1," is greatest element") if(n1>n2 and n1>n3) else print(n2," is greatest") if(n2>n3) else print(n3, "is greatest element")

n1=int(input("enter n1: "))
n2=int(input("enter n2: "))
n3=int(input("enter n3: "))
greatest_of_three(n1,n2,n3)

'''
enter n1: 5
enter n2: 6
enter n3: 3
6  is greatest
'''