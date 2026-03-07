#Conditional Statements
'''
Docstring for 7_ifcond
if-elif-else(syntax)

if(condition):
    statement
elif(condition):
    statement2
else:
    statement
'''

age=21
if(age>=18):
    print("can vote and apply for license")
else:
    print("cant vote and not eligible to apply for license")


#2 example

light="green"

if(light=="red"):
    print("stop")

elif(light=="green"):
    print("go")

elif(light=="yellow"):
    print("look")

print("end of the code")

#Output: go
        #end of the code

'''
Grade students based on marks

marks>=90, grade="A"
90>marks>=80, grade="B"
80>marks>=70, grade="C"
70>marks, grades="D"
'''

marks=int(input("enter marks: "))

if(marks>=90):
    grade="A"

elif(marks>=80 and marks<90):
    grade="B"

elif(marks>=70 and marks<80):
    grade="C"

else:
    grade="D"

print("grade of the student ->",grade)

'''
Output:enter marks: 84
grade of the student -> B
'''

 