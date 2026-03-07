#Strings : String is data type that stores a sequence of characters

#Basic Oprations
#->Concatenation - "hello"+"world"->"helloworld"
#->length of str len(str)

str1="this is a string.\nwe are creatinng in python"
print(str1)

#Concatenation
str1="apna"
str2="college"
final_str=str1+str2
print(final_str)
#Output:apnacollege

#Length of a string
str="apna"
len1=len(str1)
print(len1)
#Output:4

#Indexing- index helps us to access characters in the strng

st="alex is a good boy"
ch=str[0]
print(ch)
#Output:a

#Slicing :Acessing parts of Strings
#Syntax: str[starting_idx:ending_idx]#ending idx is not included

str="ApnaCollege"
print(str[1:4]) #pna
print(str[:4]) #Apna ->it is same as str[0:4]
print(str[1:]) #pnaCollege ->it is same as str[1:len(str)]

#Slicing Negative index
str1="Apple"
print(str1[-3:-1]) #pl

#Strings functions
str2="I am a coder"
print(str2.endswith("er")) #returns true if string ends with substr
print(str2.capitalize()) #capitalizes 1st char
print(str2.replace("coder","dancer")) #str.replace(old,new) replaces all occurence of old withn new
print(str2.find("coder")) #returns index of "coder"
print(str2.count("am")) #counts the occurence of substri in string


#Practice
#WAP to input users firstname and print its length

name=input("enter ur name: ")
print(len(name)) #Output:enter ur name: Raghuveer
                  #9

#2.WAP to find the occurence of '$' in a Strinng
str3="Hi i am the $ symbol $99.99"
print(str3.count("$")) #output:2

 