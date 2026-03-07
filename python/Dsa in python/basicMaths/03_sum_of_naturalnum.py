'''
Input : num = 8
Output : 36

Where first 8 number is 1, 2, 3, 4, 5, 6, 7, 8
Sum of numbers = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36
'''

def sum_of_naturalnum(n):
    sum=0
    for i in range(n+1):
        sum=sum+i
    print(sum)

n=int(input("Enter any number: "))
sum_of_naturalnum(n)
