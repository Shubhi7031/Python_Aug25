# Question 1: Create a dictionary of student names and their ages
print("Question 1: Create a dictionary of student names and their ages")
# Your code here

student ={

   "Alice":12,
   "John": 14
}

print(student)

# Question 2: Add a new key-value pair to dictionary {'a': 1, 'b': 2, 'c': 3}
print("\nQuestion 2: Add a new key-value pair to dictionary {'a': 1, 'b': 2, 'c': 3}")
# Your code here

dict={

    "a":1,
    "b":2,
    "c":3
}

dict["d"]=4
print(dict)

# Question 3: Get all keys from dictionary {'name': 'John', 'age': 25, 'city': 'New York'}
print("\nQuestion 3: Get all keys from dictionary {'name': 'John', 'age': 25, 'city': 'New York'}")
# Your code here

dict= {'name': 'John', 'age': 25, 'city': 'New York'}

print(dict.keys())

# Question 4: Get all values from dictionary {'python': 3, 'java': 2, 'c++': 1}
print("\nQuestion 4: Get all values from dictionary {'python': 3, 'java': 2, 'c++': 1}")
# Your code here

dict= {'python': 3, 'java': 2, 'c++': 1}

print(dict.values())

# Question 5: Check if key 'age' exists in {'name': 'Alice', 'age': 30, 'city': 'London'}
print("\nQuestion 5: Check if key 'age' exists in {'name': 'Alice', 'age': 30, 'city': 'London'}")
# Your code here

dict= {'name': 'Alice', 'age': 30, 'city': 'London'}

if "age" in dict:
    print("present in dictionary")
else:
    print("not present in dictionary")

# Question 6: Remove key 'temp' from {'a': 1, 'b': 2, 'temp': 3, 'c': 4}
print("\nQuestion 6: Remove key 'temp' from {'a': 1, 'b': 2, 'temp': 3, 'c': 4}")
# Your code here

dict ={'a': 1, 'b': 2, 'temp': 3, 'c': 4}

dict.pop("temp")

print(dict)


# Question 7: Find the sum of all values in {'math': 85, 'science': 92, 'english': 78}
print("\nQuestion 7: Find the sum of all values in {'math': 85, 'science': 92, 'english': 78}")
# Your code here

dict= {'math': 85, 'science': 92, 'english': 78}
sum1=0
for values in dict:
    sum1=sum1+ dict[values]
print(sum1)

# Question 8: Create a dictionary with squares of numbers 1 to 5
print("\nQuestion 8: Create a dictionary with squares of numbers 1 to 5")
# Your code here

squares={}

for i in range(1,6):
    squares[i]= i*i
print(squares)

# Question 9: Count frequency of each character in string "hello"
print("\nQuestion 9: Count frequency of each character in string 'hello'")
# Your code here

from collections import Counter

text= "hello"
freq= Counter(text)

print(freq)

# Question 10: Merge two dictionaries {'a': 1, 'b': 2} and {'c': 3, 'd': 4}
print("\nQuestion 10: Merge two dictionaries {'a': 1, 'b': 2} and {'c': 3, 'd': 4}")
# Your code here

dict1=  {'a': 1, 'b': 2}
dict2= {'c': 3, 'd': 4}

dict1.update(dict2)
print(dict1)

# Question 11: Create a nested dictionary: {'person': {'name': 'Alice', 'age': 25}}
print("\nQuestion 11: Create a nested dictionary: {'person': {'name': 'Alice', 'age': 25}}")
# Your code here

dict1={

    "person":{

        "name":"Alice",
        "age":25
    }
}
print(dict1)

# Question 12: Access nested value 'name' from {'person': {'name': 'Alice', 'age': 25}}
print("\nQuestion 12: Access nested value 'name' from {'person': {'name': 'Alice', 'age': 25}}")
# Your code here

dict1= {'person': {'name': 'Alice', 'age': 25}}

print(dict1["person"]["name"])


# Question 13: Create a dictionary with list values: {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
print("\nQuestion 13: Create a dictionary with list values: {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}")
# Your code here

dict1={

    "fruits":["apple","banana"],
    "colors":["red","blue"]
    }

print(dict1)


# Question 14: Add 'orange' to the 'fruits' list in nested dictionary
print("\nQuestion 14: Add 'orange' to the 'fruits' list in nested dictionary")
# Your code here

dict1= {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}

dict1["fruits"].append("orange")
print(dict1)


# Question 15: Create a dictionary with tuple values: {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
print("\nQuestion 15: Create a dictionary with tuple values: {'coordinates': (10, 20), 'rgb': (255, 0, 0)}")
# Your code here

dict1= {

    "coordinates":(10,20),
    "rgb":(255,0,0)
}
print(dict1)

# Question 16: Extract first coordinate from nested tuple
print("\nQuestion 16: Extract first coordinate from nested tuple")
# Your code here

dict1= {

    "coordinates":(10,20),
    "rgb":(255,0,0)
}

print(dict1["coordinates"][0])

# Question 17: Create a dictionary with set values: {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
print("\nQuestion 17: Create a dictionary with set values: {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}")
# Your code here

dict1= {

    "vowels":{"a","e","i"},
    "consonants":{"b","c","d"}
}
print(dict1)


# Question 18: Add 'o' to vowels set in nested dictionary
print("\nQuestion 18: Add 'o' to vowels set in nested dictionary")
# Your code here

dict1= {

    "vowels":{"a","e","i"},
    "consonants":{"b","c","d"}
}
dict1["vowels"].update("o")
print(dict1)

# Question 19: Create a 3-level nested dictionary: {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
print("\nQuestion 19: Create a 3-level nested dictionary: {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}")
# Your code here

dict1={

    "company":{
        "department":{
            "employee":{
                "name":"john",
                "id":123
            }
        }
    }
}

print(dict1)

# Question 20: Access employee name from 3-level nested dictionary
print("\nQuestion 20: Access employee name from 3-level nested dictionary")
# Your code here

dict1={

    "company":{
        "department":{
            "employee":{
                "name":"john",
                "id":123
            }
        }
    }
}

dict1["company"]["department"]["employee"]

# Question 21: Create a dictionary with mixed data types: {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
print("\nQuestion 21: Create a dictionary with mixed data types: {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}")
# Your code here

dict1={

    "int":42,
    "float":3.14,
    "str":"hello",
    "bool": True
}

print(dict1)

# Question 22: Check data type of each value in mixed dictionary
print("\nQuestion 22: Check data type of each value in mixed dictionary")
# Your code here

dict1={

    "int":42,
    "float":3.14,
    "str":"hello",
    "bool": True
}

print(type(42))
print(type(3.14))
print(type("hello"))
print(type(True))

# Question 23: Create a dictionary with function values: {'len': len, 'str': str, 'int': int}
print("\nQuestion 23: Create a dictionary with function values: {'len': len, 'str': str, 'int': int}")
# Your code here

dict1={

    "len":len,
    "str":str,
    "int":int
}
print(dict1)

# Question 24: Apply each function to "123" using dictionary
print("\nQuestion 24: Apply each function to '123' using dictionary")
# Your code here

dict1={

    "len":len,
    "str":str,
    "int":int
}

value="123"
print(dict1["len"](value))
print(dict1["str"](value))
print(dict1["int"](value))

# Question 25: Create a dictionary with lambda functions: {'double': lambda x: x*2, 'square': lambda x: x**2}
print("\nQuestion 25: Create a dictionary with lambda functions: {'double': lambda x: x*2, 'square': lambda x: x**2}")
# Your code here

dict1={

    "double": lambda x:x*2,
    "square": lambda x:x**2

}

print(dict1)

# Question 26: Apply each lambda function to 5
print("\nQuestion 26: Apply each lambda function to 5")
# Your code here

dict1={

    "double": lambda x:x*2,
    "square": lambda x:x**2

}

print(dict1["double"](5))
print(dict1["square"](5))

# Question 27: Create a dictionary with class values: {'list': list, 'dict': dict, 'set': set}
print("\nQuestion 27: Create a dictionary with class values: {'list': list, 'dict': dict, 'set': set}")
# Your code here

dict1={

    "list":list,
    "dict":dict,
    "set":set
}
print(dict1)

# Question 28: Create instances using class dictionary
print("\nQuestion 28: Create instances using class dictionary")
# Your code here

del dict
dict1={

    "list":list,
    "dict":dict,
    "set":set
}

my_dict= dict1["dict"]({ 1:"a",2:"b",3:"c"})
print(my_dict)

# Question 29: Create a dictionary with None values: {'a': None, 'b': None, 'c': None}
print("\nQuestion 29: Create a dictionary with None values: {'a': None, 'b': None, 'c': None}")
# Your code here

dict1={

    "a":None,
    "b":None,
    "c":None
}

print(dict1)

# Question 30: Replace all None values with 0
print("\nQuestion 30: Replace all None values with 0")
# Your code here

dict1={

    "a":None,
    "b":None,
    "c":None
}

for values in dict1:
    dict1[values]= 0
print(dict1)


# Question 31: Create a dictionary with boolean values: {'is_active': True, 'is_admin': False}
print("\nQuestion 31: Create a dictionary with boolean values: {'is_active': True, 'is_admin': False}")
# Your code here

dict1= {
    "is_active": True,
    "is_admin": False
}

print(dict1)

# Question 32: Count True values in boolean dictionary
print("\nQuestion 32: Count True values in boolean dictionary")
# Your code here

dict1= {
    "is_active": True,
    "is_admin": False
}
count=0
for value in dict1.values():
    if value is True:
        count= count+1
print(count)


# Question 33: Create a dictionary with complex numbers: {'z1': 3+4j, 'z2': 1+2j}
print("\nQuestion 33: Create a dictionary with complex numbers: {'z1': 3+4j, 'z2': 1+2j}")
# Your code here

dict1= {

    "z1": 3+4j,
    "z2": 1+2j
}
print(dict1)


# Question 34: Find magnitude of each complex number
print("\nQuestion 34: Find magnitude of each complex number")
# Your code here

dict1= {

    "z1": 3+4j,
    "z2": 1+2j
}

print(abs(dict1["z1"]))
print(abs(dict1["z2"]))


# Question 35: Create a 4-level nested dictionary
print("\nQuestion 35: Create a 4-level nested dictionary")
# Your code here

dict1= {
    "level1":{
        "level2":{
            "level3":{
                "level4": " you have at level 4"
            }
        }
    }
}

# Question 36: Access deepest value in 4-level nested dictionary
print("\nQuestion 36: Access deepest value in 4-level nested dictionary")
# Your code here

dict1= {
    "level1":{
        "level2":{
            "level3":{
                "level4": " you have at level 4"
            }
        }
    }
}

deepest_value= dict1["level1"]["level2"]["level3"]["level4"]

print(deepest_value)

# Question 37: Create a dictionary with range values: {'r1': range(3), 'r2': range(5)}
print("\nQuestion 37: Create a dictionary with range values: {'r1': range(3), 'r2': range(5)}")
# Your code here

dict1={

    "r1": range(3),
    "r2":range(5)
}
print(dict1)

# Question 38: Convert each range to list
print("\nQuestion 38: Convert each range to list")
# Your code here

dict1={

    "r1": range(3),
    "r2":range(5)
}
print(f"before list dicitionary is: {dict1}")

for keys in dict1:
    dict1[keys]= list(dict1[keys])

print(f"after list dictionary is : {dict1}")


# Question 39: Create a dictionary with generator values
print("\nQuestion 39: Create a dictionary with generator values")
# Your code here

gen1= (x*x for x in range(3))
gen2= (x+10 for x in range(3))

dict1={

    "squares": gen1,
    "plus_10": gen2
}

print(dict1)

# Question 40: Convert each generator to list
print("\nQuestion 40: Convert each generator to list")
# Your code here

gen1= (x*x for x in range(3))
gen2= (x+10 for x in range(3))

dict1={

    "squares": gen1,
    "plus_10": gen2
}

for value in dict1:
    dict1[value]= list(dict1[value])
print(dict1)

# Question 41: Create a dictionary with iterator values
print("\nQuestion 41: Create a dictionary with iterator values")
# Your code here

iter1= iter([1,2,3])
iter2= iter(("a","b","c"))

dict1={

    "numbers": iter1,
    "letters": iter2
}

print(dict1)

# Question 42: Extract all elements from each iterator
print("\nQuestion 42: Extract all elements from each iterator")
# Your code here

iter1= iter([1,2,3])
iter2= iter(("a","b","c"))

dict1={

    "numbers": iter1,
    "letters": iter2
}

for key in dict1:
    dict1[key]= list(dict1[key])
    print(dict1[key])

# Question 43: Create a dictionary with nested lists: {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}
print("\nQuestion 43: Create a dictionary with nested lists: {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}")
# Your code here

dict1={

    "matrix":[[1,2],[3,4]],
    "vector":[5,6,7]
}

# Question 44: Find sum of each nested list
print("\nQuestion 44: Find sum of each nested list")
# Your code here

# Question 45: Create a dictionary with nested dictionaries: {'config': {'db': {'host': 'localhost', 'port': 5432}}}
print("\nQuestion 45: Create a dictionary with nested dictionaries: {'config': {'db': {'host': 'localhost', 'port': 5432}}}")
# Your code here

dict1= {

    "config":{
        "db": {
            "host": "localhost",
            "port": 5432
            }
        }
    }

print(dict1)

# Question 46: Access database port from nested configuration
print("\nQuestion 46: Access database port from nested configuration")
# Your code here

dict1= {

    "config":{
        "db": {
            "host": "localhost",
            "port": 5432
            }
        }
    }

print(dict1["config"]["db"]["port"])

# Question 47: Create a dictionary with nested tuples: {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
print("\nQuestion 47: Create a dictionary with nested tuples: {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}")
# Your code here

dict1= {

    "points": ((1,2),(3,4)),
    "rgb":((255,0,0),(0,255,0))
}
print(dict1)

# Question 48: Extract first point coordinates
print("\nQuestion 48: Extract first point coordinates")
# Your code here

dict1= {

    "points": ((1,2),(3,4)),
    "rgb":((255,0,0),(0,255,0))
}

print(dict1["points"][0])

# Question 49: Create a dictionary with nested sets: {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}
print("\nQuestion 49: Create a dictionary with nested sets: {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}")
# Your code here

dict1= {

    "groups":[{1,2,3},{4,5,6}],
    "categories":[{"a","b"},{"c","d"}]
}
print(dict1)

# Question 50: Find union of all nested sets
print("\nQuestion 50: Find union of all nested sets")
# Your code here 
