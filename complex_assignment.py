# Question 1: Create complex number 5 + 3j
print("Question 1: Create complex number 5 + 3j")
# Your code here

num= 5+3j
print(num)

print("-"*100)


# Question 2: Find the real part of complex number 7 - 2j
print("\nQuestion 2: Find the real part of complex number 7 - 2j")
# Your code here

num= 7-2j
print("Real part:", num.real)
print("Imaginary part:", num.imag)

print("-"*100)


# Question 3: Find the imaginary part of complex number 4 + 6j
print("\nQuestion 3: Find the imaginary part of complex number 4 + 6j")
# Your code here

num= 4 + 6j
print("Imaginary part of a number is:", num.imag)

print("-"*100)


# Question 4: Add two complex numbers: (3 + 2j) and (1 + 4j)
print("\nQuestion 4: Add two complex numbers: (3 + 2j) and (1 + 4j)")
# Your code here

a=  (3 + 2j) 
b=  (1 + 4j)

print("addition is:",a+b)

print("-"*100)


# Question 5: Multiply two complex numbers: (2 + 3j) and (1 + 2j)
print("\nQuestion 5: Multiply two complex numbers: (2 + 3j) and (1 + 2j)")
# Your code here

a= (2 + 3j)
b= (1 + 2j)

print("multiplication is :", a*b)

print("-"*100)

# Question 6: Find the magnitude of complex number 6 + 8j
print("\nQuestion 6: Find the magnitude of complex number 6 + 8j")
# Your code here

num= 6 + 8j
result = abs(num)
print("magnitude is :", result)

print("-"*100)

# Question 7: Find the conjugate of complex number 5 - 7j
print("\nQuestion 7: Find the conjugate of complex number 5 - 7j")
# Your code here

num= 5 - 7j
result= num.conjugate()

print(result)

print("-"*100)

# Question 8: Subtract complex numbers: (10 + 5j) - (3 + 2j)
print("\nQuestion 8: Subtract complex numbers: (10 + 5j) - (3 + 2j)")
# Your code here

a= (10 + 5j)
b= (3 + 2j)

result= a-b
print(result)

print("-"*100)

# Question 9: Divide complex numbers: (8 + 6j) / (2 + 1j)
print("\nQuestion 9: Divide complex numbers: (8 + 6j) / (2 + 1j)")
# Your code here

a= (8 + 6j)
b= (2 + 1j)

result= a/b
print(result)

print("-"*100)

# Question 10: Find the phase angle of complex number 1 + 1j
print("\nQuestion 10: Find the phase angle of complex number 1 + 1j")
# Your code here 

import cmath

num= 1+1j

result= cmath.phase(num)
print(result)

print("-"*100)

