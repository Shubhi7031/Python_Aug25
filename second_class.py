name= "shubrati tripathi"
output= all(word.isalpha() for word in name.split())

print(output)


# count, replace, index

x1= "data_data"
out1= print(x1.count("a"))

print(x1.replace("a","g"))

print(x1.replace("_", "$"))

print(x1.index("_"))

x2= "I am a human being and I am working on python programming"
out=x2[0:5]
print(out)

print(x2[5:])

print(x2[-20:-10])

x= " "
print(x.isspace())

x= "engineer \tat \twork"
print(x.isspace())

print(x.expandtabs(5))


print(x.find("g"))

print(x.find("e", 5))

print(x.find("w",6,17))

y= "India"

print(y.center(11,"*"))
print(y.zfill(9))

z= "               Indian     "

print(z.lstrip())
print(z.rstrip())
print(z.strip())


x= " Good Evening"

print(x.ljust(101, "*"))
print(x.rjust(50,"*"))