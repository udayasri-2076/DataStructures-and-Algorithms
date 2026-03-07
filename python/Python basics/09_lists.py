#Lists -A built-in datatype that stores set of values. it can store elements of different types(integer,float,string,etc.)

marks=[98,87.5,82.5,45.1]
print(marks)   #[98, 87.5, 82.5, 45.1]
print(type(marks))#<class 'list'>
print(marks[0])   #98
print(len(marks)) #4

#Strings are immutable and lists are mutable 
#Mutable means changable

student=["karan",95.4,17,"delhi"]
print(student[0])  #karan
student[0]="arjun"
print(student)    #['arjun', 95.4, 17, 'delhi']   


#List Slicinng
#Syntax: list_name[starting_idx:ending_idx] ending_idx is not included

scores=[87,64,33,95,76]
print(scores[1:4]) #[64, 33, 95]
print(scores[:4])  #[87, 64, 33, 95]
print(scores[1:])  #[64, 33, 95, 76]
print(scores[-3:-1]) #[33, 95]

#List Methods

list=[2,1,3]
list.append(4) 
print(list)#adds one element at the end [2,1,3,4]

list.sort()
print(list) #sorts in ascending order [1,2,3,4]

list.sort(reverse=True)
print(list) #sorrts in descending order [4,3,2,1]

list.reverse()
print(list) #reverse list [1,2,3,4]

list.insert(0,4)
print(list)#insert element at index(idx,el) [4,1,2,3,4]

list.remove(1)
print(list) #removes 1 from the list [4, 2, 3, 4]

list.pop(1) #list.pop(idx)
print(list) #removes the element of that index [4, 3, 4]

