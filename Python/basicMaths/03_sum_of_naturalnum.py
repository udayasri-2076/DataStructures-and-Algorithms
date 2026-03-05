def sum_of_naturalnum(n):
    sum=0
    for i in range(n+1):
        sum=sum+i
    print(sum)

n=int(input("Enter any number: "))
sum_of_naturalnum(n)
