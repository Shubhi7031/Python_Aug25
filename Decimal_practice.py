# Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577

x= [3.14, 2.718, 1.618, 0.577]

average= sum(x)/len(x)

print("Question 1: Average is:", average)


# Question 2: Convert 98.6 Fahrenheit to Celsius (F = C * 9/5 + 32)

f= 98.6

c= (f-32)*5/9

print("Question 2:Convert 98.6 Fahrenheit to Celsius :",c)


# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years

p= 1000
r= 5.5
t=3

ci= p * (1 + r/100)**t

print("Question 3: coumpound interest is :",ci)


# Question 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2

p= 4.2
b= 3.5
h= (p**2 + b**2)**(1/2)

print("Question 4: The hypotenuse is:", h)


# Question 5: Calculate the volume of a sphere with radius 7.8

import math
r = 7.8

volume= (4/3)* math.pi* (r**3)

print("Question 5: volumne of a sphere is:", volume)

# Question 6: Round 3.14159 to 3 decimal places

num= 3.14159
rounded_num= round(num,3)

print("Question 5: Rounded number is", rounded_num)


# Question 7: Calculate the percentage: 45 out of 67

a=45
b=67
percent= round((a/b)*100,3)


print("Question 7: The percentage is:",percent)

# Question 8: Find the square root of 23.456

num= 23.456

Sq_root = num**(1/2)

print("Question 7: the square root is:", Sq_root)


# Question 9: Calculate the simple interest: Principal=2500, Rate=6.5%, Time=2.5 years


p= 2500
r= 6.5
t= 2.5
SI= (p*r*t)/100

print("Question 9: SI is", SI)


# Question 10: Convert 45.7 degrees to radians

degree= 45.7
import math
R= (math.pi/180)*degree
rounded_no = round(R,3)

print("Question 10: converted into raidans is:", rounded_no)


