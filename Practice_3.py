# List Practice session

x= [34, 89, 24.6, "data",45, 6+9j]

print(len(x))
print(type(x))
print(x[4])

# Note- List is mutable

x[3]="student"
x[5]="data engineer"

print(x)

x= [34, 89, 24.6, "data",45, 6+9j]
print(x)
y=x
y[3]="student"
y[5]="data engineer"
print(y)

# Nested list

z=[[12,"engineer", 84.6], [45, 78, 90], [26,58.2,"shubrati"]]

print(len(z))

print(z[2][2])

print(z[0][1][-4:].upper())

# list slicing

numbers= [15, 29, 11, 64, 42, 28, 67, 10,81,80,89]

print(numbers[::3])

print(numbers[2:8])
print(numbers[1:9:2])

numbers.append("edukron")
print(numbers)

x=numbers.__len__()
print(x)

x1= print(len(numbers))

print(numbers.count(11))

no1= numbers.copy()
print(no1)

no1.append(89)
print(no1)

print(numbers)

my_list= [11, 64, 42, 28, 67, 10,81,80,89]

my_list.insert(5,500)
print(my_list)

my_list.remove(67)
print(my_list)

my_list.pop(1)
print(my_list)

my_list.pop()
print(my_list)

my_list.clear()
print(my_list)


my_list= [11, 64, 42, 28, 67, 10,81,80,89]

my_list.insert(5,500)
print(my_list)

my_list.reverse()
print(my_list)

my_list.append([6,8,0,2])
print(my_list)

my_list.extend("data")
print(my_list)

my_list.extend(["data","kanpur"])
print(my_list)

my_list.extend([1,2,3])
print(my_list)