# Practicing In-bulit functions that is system defined functions

# upper, lower, swapcase, title , capitalize

x1= "ABCDFR"
output= x1.lower()
print(output)

x2= "abcfgh"
op= print(x2.upper())

x3= "awdPFG"
op= print(x3.swapcase())

x4= "data science"
op= print(x4.title())

x5= "DATA SCIENCE"
op= print(x5.capitalize())


# alpha, digit, alnum, split, startswith, endswith

name= "Shubratitripathi"

age= "29"
city= "bangalore"

op= age.isdigit()

print("output is:", op) 


name= "Shubrati tripathi"
output= name.isalpha()
print(output)


val= "data"
op= val.isalpha()
print(op)

x= "data123"
output=x.isalnum()
print("ans is:",output)

name= "Shubrati&tripathi"
output= name.isalpha()
print(output)

variable1= "shubh123"
print(variable1.isalnum())

var2= "74&89"
print(var2.isdigit())

var3= "dataEngineering"
print(var3.isalpha())

print(var3.startswith("d"))
print(var3.endswith("t"))

print(var3.split("a"))
print(var3.split("e"))