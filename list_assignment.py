

# # Question 1: Create a list of first 10 square numbers
print("Question 1: Create a list of first 10 square numbers")

num=1
list1=[]

while num<11:
    list1.append(num*num)
    num=num+1
print(list1)

print("-"*100)

# Question 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nQuestion 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
# Your code here



list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i=0
sum_even=0

while i< len(list1):
    if list1[i]%2==0:
        sum_even=sum_even+list1[i]
    i=i+1

print(sum_even)
print("-"*100)

# Question 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print("\nQuestion 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]")
# Your code here


list1=[1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

updated_list= sorted(set(list1))

print(updated_list)
print("-"*100)


# Question 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order
print("\nQuestion 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order")
# Your code here

list1= [64, 34, 25, 12, 22, 11, 90]

y= sorted((list1),reverse= True)

print(y)
print("-"*100)

# Question 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]
print("\nQuestion 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]")
# Your code here


list1= [15, 23, 31, 42, 56, 78, 91]

sum1= sum(list1)
len1= len(list1)
average= sum1/len1

print(average)
print("-"*100)


# Question 6: Create a list of first 15 Fibonacci numbers
print("\nQuestion 6: Create a list of first 15 Fibonacci numbers")
# Your code here

a=0
b=1
n=0
while n<=15:
    print(a,end=" ")
    a,b=b,a+b
    n=n+1
print(a,b)
print("-"*100)

# Question 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]
print("\nQuestion 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]")
# Your code here

# Question 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]
print("\nQuestion 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]")
# Your code here

list1= [45, 67, 23, 89, 12, 34, 78]

y= sorted(list1, reverse= True)

print(y[1])
print("-"*100)

# Question 8: Reverse the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nQuestion 8: Reverse the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
# Your code here

list1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list1.reverse()
print(list1)
print("-"*100)

# Question 9: Count how many times 5 appears in [1, 5, 2, 5, 3, 5, 4, 5, 6]
print("\nQuestion 9: Count how many times 5 appears in [1, 5, 2, 5, 3, 5, 4, 5, 6]")
# Your code here

list1= [1, 5, 2, 5, 3, 5, 4, 5, 6]

count=0

for num in list1:
    if num==5:
        count=count+1

print(count)
print("-"*100)

# Question 10: Create a list of prime numbers between 1 and 50
print("\nQuestion 10: Create a list of prime numbers between 1 and 50")
# Your code here


list1=[]

for num in range(2,51):
    is_prime= True
    for i in range(2,num):
       if num%i==0:
        is_prime=False
        break
    if is_prime:
        list1.append(num)

print(list1)
print("-"*100)

# Question 11: Flatten nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 11: Flatten nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here


list1=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2=[]

for sublist in list1:
    for items in sublist:
        list2.append(items)

print(list2)
print("-"*100)

# Question 12: Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]
print("\nQuestion 12: Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]")
# Your code here

list1= [1,2,3,4,5]
list2= [4,5,6,7,8]

for i in list1:
    for j in list2:
        if i == j:
            print(i,end=" ")
        
print("-"*100)


# Question 13: Create a list of lists: [[1, 2], [3, 4], [5, 6]]
print("\nQuestion 13: Create a list of lists: [[1, 2], [3, 4], [5, 6]]")
# Your code here

list1= [[1,2],[3,4],[5,6]]
print(list1)

print("-"*100)

# Question 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here

list1=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum1=0
for sublist in list1:
    for items in sublist:
        sum1= sum1+ items

print(sum1)
print("-"*100)

# Question 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here


list1= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transpose= []

for i in range(len(list1[0])):
    new_row=[]
    for row in list1:
        new_row.append(row[i])
    transpose.append(new_row)

print(transpose) 
print("-"*100)

# Question 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]
print("\nQuestion 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]")
# Your code here


list1= [[1, 5, 3], [9, 2, 7], [4, 8, 6]]

for i in range(len(list1[0])):
    max1= max(list1[i])
    print(max1)

print("-"*100)


# Question 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("\nQuestion 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
# Your code here

list3d= [
    [
            [1,2],
            [3,4]

        ],
    [
            [5,6],
            [7,8]


        ]

]
print(list3d)

print("-"*100)


# Question 18: Find the sum of all elements in 3D list [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("\nQuestion 18: Find the sum of all elements in 3D list [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
# Your code here

list3d= [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
sum1=0
for layers in list3d:
    for rows in layers:
        for items in rows:
            sum1= sum1+items

print(sum1)

print("-"*100)

# Question 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here

list1= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for rows in list1:
    for items in rows:
        if items%2==0:
            print(items)


print("-"*100)

# Question 20: Create a list of mixed data types: [1, "hello", 3.14, True, [1, 2, 3]]
print("\nQuestion 20: Create a list of mixed data types: [1, 'hello', 3.14, True, [1, 2, 3]]")
# Your code here

mixed_list= [1,"hello", 3.14, True,[1,2,3]]
print(mixed_list)

print("-"*100)

# Question 21: Find the length of each string in ["apple", "banana", "cherry", "date"]
print("\nQuestion 21: Find the length of each string in ['apple', 'banana', 'cherry', 'date']")
# Your code here

list1= ["apple", "banana", "cherry", "date"]

for items in list1:
    x= len(items)
    print(f"the length if {items} is {x}")

print("-"*100)

# Question 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]")
# Your code here

list_of_tuples= [(1,"a"),(2,"b"),(3,"c")]

print(list_of_tuples)
print("-"*100)

# Question 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]")
# Your code here

list1= [(1, 'a'), (2, 'b'), (3, 'c')]

for rows in list1:
    for items in rows:
        print(items)
        break

print("-"*100)



# Question 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
print("\nQuestion 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]")
# Your code here

list1= [{"name":"Alice","age":25},{"name":"Bob", "age":30}]
print(list1)

print("-"*100)

# Question 25: Extract all 'name' values from list of dictionaries
print("\nQuestion 25: Extract all 'name' values from list of dictionaries")
# Your code here
list1= [{"name":"Alice","age":25},{"name":"Bob", "age":30}]

for persons in list1:
    print(persons["name"])

print("-"*100)


# Question 26: Find the person with maximum age in list of dictionaries
print("\nQuestion 26: Find the person with maximum age in list of dictionaries")
# Your code here

list1= [{"name":"Alice","age":25},{"name":"Bob", "age":30}]

ages= [persons["age"] for persons in list1]


max1= max(ages)
print(max1)

print("-"*100)


# Question 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
print("\nQuestion 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]")
# Your code here

list4d= [

[
    [[1,2],[3,4]],
    
    [[5,6],[7,8]]
    ],

[
    [[9,10],[11,12]],

    [[13,14],[15,16]]
]


]

print("-"*100)

# Question 28: Find the maximum value in 4D list
print("\nQuestion 28: Find the maximum value in 4D list")
# Your code here

list4d= [

[
    [[1,2],[3,4]],
    
    [[5,6],[7,8]]
    ],

[
    [[9,10],[11,12]],

    [[13,14],[15,16]]
]


]
max_value=0
for layers in list4d:
    for matrix in layers:
        for list1d in matrix:
            for num in list1d:
                if num> max_value:
                    max_value= num

print(max_value)
print("-"*100)

# Question 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
print("\nQuestion 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]")
# Your code here

list1=[{1,2,3},{4,5,6},{7,8,9}]
print(list1)
print("-"*100)


# Question 30: Find the union of all sets in list of sets
print("\nQuestion 30: Find the union of all sets in list of sets")
# Your code here

list1=[{1,2,3},{4,5,6},{7,8,9}]
result= list1[0].union(list1[1])
final_result= result.union(list1[2])

print(final_result)
print("-"*100)

# Question 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]
print("\nQuestion 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]")
# Your code here

list1= [1+2j,3+4j,5+6j]
print(list1)
print("-"*100)

# Question 32: Find the magnitude of each complex number in list
print("\nQuestion 32: Find the magnitude of each complex number in list")
# Your code here

list1= [1+2j,3+4j,5+6j]

for num in list1:
    print(f"the magnitude of {num} is {abs(num)}")

print("-"*100)



# Question 33: Create a nested list with different levels: [1, [2, 3], [4, [5, 6]], 7]
print("\nQuestion 33: Create a nested list with different levels: [1, [2, 3], [4, [5, 6]], 7]")
# Your code here

list1= [1,[2,3],[4,[5,6]],7]
print(list1)
print("-"*100)


# Question 34: Count the depth of nesting in [1, [2, 3], [4, [5, 6]], 7]
print("\nQuestion 34: Count the depth of nesting in [1, [2, 3], [4, [5, 6]], 7]")
# Your code here

list1= [1,[2,3],[4,[5,6]],7]
def get_depth(lst):
    if not isinstance(lst,list):
        return 0
    elif not lst:
        return 1
    else:
        return 1 + max(get_depth(item) for item in lst)
depth= get_depth(list1)
print(f"the depth of the list1 is {depth}")
print("-"*100)

# Question 35: Create a list of functions: [len, str, int, float]
print("\nQuestion 35: Create a list of functions: [len, str, int, float]")
# Your code here

list1= [len,str,int,float]
print(list1)
print("-"*100)

# Question 36: Apply each function in list to string "123"
print("\nQuestion 36: Apply each function in list to string '123'")
# Your code here

list1= [len,str,int,float]
input_str= "123"

for func in list1:
    result= func(input_str)
print(f" {result}")
print("-"*100)

# Question 37: Create a list of lambda functions: [lambda x: x*2, lambda x: x**2, lambda x: x+1]
print("\nQuestion 37: Create a list of lambda functions: [lambda x: x*2, lambda x: x**2, lambda x: x+1]")
# Your code here

list1= [lambda x: x*2, lambda x:x**2, lambda x:x+1]
print(list1)
print("-"*100)

# Question 38: Apply each lambda function to 5
print("\nQuestion 38: Apply each lambda function to 5")
# Your code here

list1= [lambda x: x*2, lambda x:x**2, lambda x:x+1]

for func in list1:
    result= func(5)
    print(result)

print("-"*100)

# Question 39: Create a list of classes: [list, dict, set, tuple]
print("\nQuestion 39: Create a list of classes: [list, dict, set, tuple]")
# Your code here

list1=[list, dict, set, tuple]
print(list1)
print("-"*100)

# Question 40: Create instances of each class in list
print("\nQuestion 40: Create instances of each class in list")
# Your code here

list1=[list, dict, set, tuple]

for cls in list1:
    result= cls()
    print(result)

print("-"*100)


# Question 41: Create a list of None values: [None, None, None, None]
print("\nQuestion 41: Create a list of None values: [None, None, None, None]")
# Your code here

list1=[None, None, None, None]
print(list1)
print("-"*100)

# Question 42: Replace all None values with 0 in list
print("\nQuestion 42: Replace all None values with 0 in list")
# Your code here

list1=[None, None, None, None]
list2=[]
for values in list1:
    values= 0
    list2.append(values)

print(list2)
print("-"*100)

# Question 43: Create a list of boolean values: [True, False, True, False]
print("\nQuestion 43: Create a list of boolean values: [True, False, True, False]")
# Your code here

list1= [True, False, True, False]
print(list1)

print("-"*100)

# Question 44: Count True values in boolean list
print("\nQuestion 44: Count True values in boolean list")
# Your code here


list1= [True, False, True, False]
count=0
for values in list1:
    if values==True:
        count= count+1
    

print(count)
print("-"*100)


# Question 45: Create a list of ranges: [range(3), range(5), range(2)]
print("\nQuestion 45: Create a list of ranges: [range(3), range(5), range(2)]")
# Your code here

list1=[range(3), range(5), range(2)]
print(list1)
print("-"*100)

# Question 46: Convert each range to list
print("\nQuestion 46: Convert each range to list")
# Your code here

list1=[range(3), range(5), range(2)]

for r in list1:
    print(list(r))

print("-"*100)

# Question 47: Create a list of generators: [(x for x in range(3)), (x for x in range(5))]
print("\nQuestion 47: Create a list of generators: [(x for x in range(3)), (x for x in range(5))]")
# Your code here

list1=[(x for x in range(3)),(x for x in range(5))]
print(list1)
print("-"*100)

# Question 48: Convert each generator to list
print("\nQuestion 48: Convert each generator to list")
# Your code here

list1=[(x for x in range(3)),(x for x in range(5))]

for r in list1:
    print(list(r))

print("-"*100)

# Question 49: Create a list of iterators: [iter([1, 2, 3]), iter([4, 5, 6])]
print("\nQuestion 49: Create a list of iterators: [iter([1, 2, 3]), iter([4, 5, 6])]")
# Your code here

list1=[iter([1,2,3]),iter([4,5,6])]
print(list1)
print("-"*100)

# Question 50: Extract all elements from each iterator
print("\nQuestion 50: Extract all elements from each iterator")
# Your code here 

list1=[iter([1,2,3]),iter([4,5,6])]

for items in list1:
    print(list(items))

print("-"*100)