#Dictionnary: Dictionaries are used to store data values in key:value pairs, they are unordered,mutable(changeable) & dont allow duplicate keys

info={
    "name":"shradha",     #key:value
    "cgpa":9,
    "marks":[98,97,95]
}
print(info)

#output: {'name': 'shradha', 'cgpa': 9, 'marks': [98, 97, 95]}

#Nested dictionaries
student={
    "name":"alex",
    "score":{
        "chem":98,
        "phy":97,
        "math":95
    }
}

print(student["score"]["math"]) #Output:95
print(student)

#Output: {'name': 'alex', 'score': {'chem': 98, 'phy': 97, 'math': 95}}

#Dictionary Methods

print(student.keys()) #return all keys.   dict_keys(['name', 'score'])
print(student.values())#returns all values  dict_values(['alex', {'chem': 98, 'phy': 97, 'math': 95}])
print(student.items()) #returns all (key,val) pairs as tuples   dict_items([('name', 'alex'), ('score', {'chem': 98, 'phy': 97, 'math': 95})])
print(student.get("name"))#returns the key according to value  alex
new_dict={"city":"delhi"}
print(student.update(new_dict))