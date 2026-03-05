#Ascii value of all characters in string

'''
Docstring for Dsa in python.basics.ascii of all ch

Write a Python program to find the ASCII values of all characters in a given string.
You are required to:
Read a string S from the user. Print the ASCII value of each character in the string, separated by spaces.

Input:Hello
Output:72 101 108 108 111
'''

S=input()

for ch in S:
    asc=ord(ch)
    print(asc,end=" ")

#Output:Alex
        #65 108 101 120 