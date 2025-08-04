# Question 1: Calculate the product of first 10 natural numbers


Natural_no = [1,2,3,4,5,6,7,8,9,10]
print("Natural Numbers are:", Natural_no)

product=1

for i in Natural_no:
    if i< len(Natural_no):
        product= product* Natural_no[i]
    i=i+1
print(" Question 2:  product of first 10 natural numbers is:", product)    





# Question 2: Find the remainder when 156 is divided by 7

print("my numerator is : 156")
print("my denominator is : 7")

output= 156 % 7

print(" Question 2:  Remainder is:", output)



# Question 3: Calculate the square of 25

x= 25

square= x*x

print("Question 3:  square of a number is :", square)



# Question 4: Find the cube root of 125

x= 125

cube_root= x**(1/3)

print("Question 4:  Cube root of 125 is: ", cube_root)


# Question 5: Calculate the sum of digits in number 12345

print("my number is : 12345")

sum= 1+2+3+4+5

print("Question 5:  sum of a number is :",sum)


# Question 6: Check if 97 is a prime number

n= 97

number_is_prime= n>1 and all(n%i !=0 for i in range (2,n))

print("Question 6:  Number is prime:", number_is_prime)



# Question 7: Find the factorial of 8


num=4
fact= 1

for i in range(1, num+1):
     fact= fact*i

print("Question 7:  factorial is:", fact)


# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56


num= [15,23,31,42,56]
sum= 0
for i in num:
    sum= sum+ i

average= sum/ len(num)

print("Question 8: Average is :", average)


# Question 9: Find the greatest common divisor (GCD) of 48 and 36

import math

gcd= math.gcd(48,36)

print("Question 9: GCD is :",gcd)


# Question 10: Calculate the sum of first 20 odd numbers

odd_sum=0
n=1
count=1

while count<=20:

    odd_sum= odd_sum+n
    n=n+2
    count=count+1


print("Question 10: Sum of first 20 odd numbers is:", odd_sum)