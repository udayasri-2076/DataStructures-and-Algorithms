#Set: Set is a collectionn of the unordered items. Each element in the set must be unique & immutable

collection={1,2,3,4,2,3}
print(collection)       #{1, 2, 3, 4}
print(type(collection)) #<class 'set'>

#->Set ignores duplicate values and are mutable but we cant change the elements inn the set

'''
Set Methods
set.add el() #adds an elemennt
set.remove(el) #removes the elem an
set.clear() #empties the set
set.pop() #removes a random value
set.union(set2) #combines both set values & return new
set.intersection(set2) #combines ommon values & returns new
'''

group=set()
group.add(1)
group.add(2)
group.add(3)
print(group) #{1, 2, 3}

group.remove(3)
print(group) #{1, 2}

group.pop() 
print(group) #{2}

group.clear()
print(group) #set()
 
set1={1,2,3,4}
set2={2,3,4}

print(set1.union(set2)) #{1, 2, 3, 4}
print(set1.intersection(set2)) #{2, 3, 4}