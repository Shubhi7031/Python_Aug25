# TUPLE DATATYPE ASSIGNMENT
# ========================

# SOLVED EXAMPLE
# --------------
# Question: Find the sum and product of all elements in a tuple
print("SOLVED EXAMPLE:")
print("Find the sum and product of all elements in a tuple")
numbers = (2, 4, 6, 8, 10)
sum_tuple = sum(numbers)
product = 1
for num in numbers:
    product *= num
print(f"Tuple: {numbers}")
print(f"Sum: {sum_tuple}")
print(f"Product: {product}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a tuple of first 10 natural numbers
print("Question 1: Create a tuple of first 10 natural numbers")

natural_numbers= tuple(range(1,11))
print(natural_numbers)

print("-"*100)



# Question 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("\nQuestion 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)")

x= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"the length of the tuple is {len(x)}")

print("-"*100)

# Question 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')
print("\nQuestion 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')")

x= ('a', 'b', 'c', 'd', 'e')
element3= x[2]

print(f" the 3rd element in tuple is {element3}")

print("-"*100)

# Question 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)
print("\nQuestion 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)")

x= (23, 45, 12, 67, 34, 89, 56)
y= max(x)

print(f"maximum value in tuple is {y}")
print("-"*100)

# Question 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)
print("\nQuestion 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)")

x= (1, 5, 2, 5, 3, 5, 4, 5, 6)
count=0
for values in x:
    if values== 5:
        count=count+1

print(f"no. of times 5 appears is: {count}")
print("-"*100)

# Question 6: Create a tuple of mixed data types (integer, float, string, boolean)
print("\nQuestion 6: Create a tuple of mixed data types (integer, float, string, boolean)")

t= ("data", 4, 6.8, True)

print(f"my tuple is :{t}")
print("-"*100)

# Question 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')
print("\nQuestion 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')")

t=('java', 'python', 'c++', 'javascript')

for i in t:
    if i == "python":
        print(f" the value is at index {t.index(i)}")
        break

print("-"*100)   

# Question 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)
print("\nQuestion 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)")

t= (10, 20, 30, 40, 50)

if 25 in t:
    print("25 exists")
else:
    print("25 not exists")


print("-"*100)

# Question 9: Create a tuple of first 5 even numbers
print("\nQuestion 9: Create a tuple of first 5 even numbers")

t=(2,4,6,8,10)
print(t)

print("-"*100)

# Question 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)
print("\nQuestion 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)")

t= (15, 23, 31, 42, 56, 78)

s= sum(t)
count=0

for i in t:
    count=count+1

average= s/count
print(average)