info = {
    "name" : "rahul",
    "learning" : "coding",
    "age" : 23,
    "carrier" : "good"
}
# print(info)
# print(info["name"])
# print(info["carrier"])
# print(info["age"])
# print(type(info))

# info["name"] = "rajesh"
# info["surname"] = "sahoo"
# print(info) # the property of mutable(its change their value)


student = {
    "name" : "rahul kumar",
    "subject" : {
        "java" : {
            "core-java" : 78,
            "adv-java" : 87
        },
        "C++"  : 67,
        "python" : 99
    } 
}

# print(student)
# print(student["name"]) # rahul kumar (Dictionary->key)
# print(student["subject"]["python"]) #99 (dictionary->dictionary->key)
# print(student["subject"]["java"]["core-java"]) #78 (dictionary->dictionary->dictionary->key)


student1 = {
    "name" : "rahul kumar",
    "subject" : {
        "java" : 98,
        "C++"  : 67,
        "python" : 99
    }
}

# print(info)
# print(student1.keys()) #(['name', 'subject'])
# print(student1["subject"].keys()) #(['java', 'C++', 'python'])
# print(student1.values()) #(['rahul kumar', {'java': 98, 'C++': 67, 'python': 99}])
# print(student1["subject"].values()) #([98, 67, 99])
# print(student1.items()) #([('name', 'rahul kumar'), ('subject', {'java': 98, 'C++': 67, 'python': 99})])
# print(student1.get("subject")) #{'java': 98, 'C++': 67, 'python': 99}
# student1.update({"city":"bhubaneswar"})
# print(student1) #{'name': 'rahul kumar', 'subject': {'java': 98, 'C++': 67, 'python': 99}, 'city': 'bhubaneswar'}




collection = {1,2,3,2,4,1,5,"hello","world","hello"}

# print(collection) #{1,2,3,4,5,"hello","world"} 
# print(type(collection)) #set

# collection = set() #empty set
# print(type(collection)) #set

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.remove(1)
# collection.clear()
# print(collection) # set()
        
collection1 = {"hello","rahul","rajeev","biswa","world"}
print(collection1.pop()) # randomly popout one element