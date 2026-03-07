#Tuples in Python
#A built-in data type that lets us create immutable sequences of values

t=(2,3,4,5)
print(type(t)) #<class 'tuple'>
print(t[0])  #2
print(t[1]) #3


#Slicing
print(t[1:3]) #(3, 4)

#Tuple Methods
print(t.index(3)) #tuple.index(el),returns index of first occurence 1

t1=(2,3,4,5,2)
print(t1.count(2)) #counts total occurences t1.count(2) is 2


#Practice
#1.WAP to ask the user to enter names of their 3 favourite movies & store them in a list

movies=[]
mov1=input("entr 1st movie")
mov2=input("enter 2nd movie")
mov3=input("enter 3rd movie")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

'''
Output
entr 1st movie:bahubali
enter 2nd movie:kgf
enter 3rd movie:bahubali2
['bahubali', 'kgf', 'bahubali2']
'''

#2.WAP to check if a list contains a palindrome of elements 
l1=["m","a","a","m"]


copy_l1=l1.copy()
copy_l1.reverse()

if(copy_l1 == l1):
    print("palindrome")

else:
    print("not palindrome")

#Output:Palindrome