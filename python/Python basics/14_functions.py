'''
Functions : it is a block of statements that perform a specific task

Syntax:

def func_name(param1,param2...):
#some work
return val 

func_name(arg1,arg2..) #function call

'''

def calc_sum(a,b):
    sum=a+b
    print(sum)
    return sum

calc_sum(5,7) #12 Output

#ALternate method

#function definition
def sum(a,b): #parameters
    return a+b

s=sum(15,17) #functionn call; arguments
print(s)

#average of 3 numbrs

def calc_avg(a,b,c):
    return (a+b+c)/3

avg=calc_avg(15,16,17) #16.0
print(avg)
    
'''
Two types
Built-in - print(),len(),type(),range()
User defined- functions defined by user
 
Default Parameters: Assigning a default value to parameteer, which is used when no argument is passed

'''
#WAF TO PRINT THE LEN OF LIST

cities=["delhi","gurgaon","noida","pune","mumbai","chennai"]
heroes=["thor","ironman","captain","america","shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities) #6
print_len(heroes) #5

#WAF to print the elements of a list in a single linne(list is the parameter)

marks=[99,56,78,45,65,86]

def print_el(list):
    for i in list:
        print(i,end=" ")

print_el(marks) #99 56 78 45 65 86

#WAF TO FIND THE FACTORIAL OF n.(n is the parameter)

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)

fact(5)# 120
