# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a set of first 10 natural numbers
print("Question 1: Create a set of first 10 natural numbers")
# Your code here

set1={1,2,3,4,5,6,7,8,9,10}
print(set1)

# Question 2: Add element 11 to set {1, 2, 3, 4, 5}
print("\nQuestion 2: Add element 11 to set {1, 2, 3, 4, 5}")
# Your code here

set1= {1, 2, 3, 4, 5}
set1.add(11)
print(set1)

print("-"*100)

# Question 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}
print("\nQuestion 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}")
# Your code here

set1= {1, 2, 3, 4, 5, 6}
set1.remove(3)
print(set1)
print("-"*100)


# Question 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
# Your code here
x= {1, 2, 3, 4, 5}
y={4, 5, 6, 7, 8}

print(x.intersection(y))
print("-"*100)

# Question 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
# Your code here

x= {1, 2, 3, 4, 5}
y={4, 5, 6, 7, 8}

print(x.difference(y))
print("-"*100)

# Question 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}
print("\nQuestion 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}")
# Your code here

set1= {1, 2, 3, 4, 6, 7, 8}

if 5 in set1:
    print("5 is present in set")

else:
    print("5 is not present in set")

print("-"*100)

# Question 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}
print("\nQuestion 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}")
# Your code here

set1= {'a', 'b', 'c', 'd', 'e'}
print(len(set1))
print("-"*100)

# Question 8: Create a set of vowels from string "hello world"
print("\nQuestion 8: Create a set of vowels from string 'hello world'")
# Your code here

str1= "hello world"
vowels="AEIOUaeiou" 
set1= set()
for char in str1:
    if char in vowels:
        set1.add(char)
print(set1)

print("-"*100)

# Question 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set
print("\nQuestion 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set")
# Your code here

list1= [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_list1= set(list1)

print(unique_list1)
print("-"*100)


# Question 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}
print("\nQuestion 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}")
# Your code here 

x= {1, 2, 3}
y= {1, 2, 3, 4, 5, 6}

print(x.issubset(y))
print("-"*100)