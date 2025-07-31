# Tuple is immutable and is faster than list due to its fixed size

x=(1,2,3,4)

print(len(x))

print(x[0])
print(x[1:3])
print(x)

print(x.index(1))

x=(1,2,3,4,20,2.8,"data","school","school")
print(x.count("school"))

for item in x:
   print(item)


print("school" in x)
   

# dictionaries are mutable and unordered collections of key-value pairs

student_info = {
    "student1": {
        "name": "Ayush",
        "age": 12,
        "roll no": 2
    },
    "student2": {
        "name": "Ritu",
        "age": 11,
        "roll no": 3
    },
    "student3":{
       
       "name": "John",
       "age": 11,
       "roll no": 4
       }}

print(student_info["student2"]["name"])

print(student_info.keys())
print(student_info.values())
print(type(student_info))

print(student_info["student2"].keys())

print(student_info["student3"].values())

print(student_info.items())

print(student_info.keys())

