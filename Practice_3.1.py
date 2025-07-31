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


my_list= [11, 64, 42, 28, 67, 10,81,80,89]

my_list.insert(4,1000)
print(my_list)
my_list.sort()
print(my_list)

my_list.append({(2+3j),6})
print(my_list)

my_list.extend(["bangalore"])
my_list.extend("system")
my_list.extend({(2+3j),6})
print(my_list)

my_list.pop(2)
my_list.pop(3)
my_list.pop(0)



x= ["abc","klm","bdc","zyc"]
x.sort()
print(x)
x.sort(reverse= True)
print(x)

x=["Delhi", "Mumbai", "Bangalore","Chennai","Uttarakhand"]
x.sort(reverse= True)

print(x)

x= [1,2,8, "course", "object"]

print(x)


x.reverse()
print(x)

# Shallow copy and deep copy

x= [1,2,3,4,5]
y=x
y[3]=100000
print(x)
print(y)

x= [3,8,9,11]
y=x.copy()
y[3]=198
print(x)
print(y)

x= [3,3,8,8,9,10,11,3,3,3,3,4]
a= x.count(3)
print(a)

x.pop(-1)
print(x)
x.pop()
x.pop()
x.pop()
x.pop()
print(x)
