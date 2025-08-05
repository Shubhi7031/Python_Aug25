# Question 1: Reverse the string "Python Programming"

Str= "Python Programming"
Rev= Str[::-1]
print("Question 1: Reversed string is :",Rev)


# Question 2: Check if "racecar" is a palindrome

str1= "racecar"
str2= str1[::-1]

if str1 == str2:
    print("RaceCar is palindrome")

else:
    print("not palindrome")


# Question 3: Count the number of words in "Python is a great programming language"

str= "Python is a great programming language"
count= len( str.split())

print(" Question 3: Total letters in a string are:",count)


# Question 4: Convert "hello world" to title case


text= "hello world"

new_text= text.title()

print("Question 4: title case is:", new_text)

# Question 5: Find the length of string "Data Science"

str= "Data Science"

print("Question 5: The length of a string is:", len(str))


# Question 6: Replace all spaces with underscores in "Machine Learning"

text= "Machine Learning"

Final_Text= text.replace(" ", "_")

print("Question 6: updated text is:", Final_Text)

# Question 7: Check if "python" is in "Python Programming Language"

str= "Python Programming Language"
sub_str= "Python"
result= str.find("Python")

if result!= -1 :
    print("Question 7: string is found at position:",result)
    print(str[result: result+ len(sub_str)])

else:
    print("string not found")


# Question 8: Extract the first 5 characters from "Artificial Intelligence"

text= "Artificial Intelligence"

print("Question 8: the first five characters are:", text[0:5])

# Question 9: Convert "UPPERCASE" to lowercase

text= "UPPERCASE"

print("Question 9: The lowercase would be:", text.lower())


# Question 10: Remove all vowels from "Computer Science"

text= "Computer Science"
vowels= "aeiouAEIOU"
str= ""

for char in text:
    if char not in  vowels:
        str=str+char

print("Question 10: result is: ",str)



# Question 11: Find the most frequent character in "mississippi"

# Question 12: Check if two strings are anagrams: "listen" and "silent"

str1= "listen"
str2= "silent"

str1= str1.replace(" ", "").lower()
str2= str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("Question 12: strings are anagrams")

else:
    print("Not anagrams")



# Question 13: Capitalize first letter of each word in "python programming language"

str= "python programming language"

print("Question 13: The string would be:  ",str.title())


# Question 14: Count consonants in "Hello World"

str1= "Hello World"
vowels= "AEIOUaeiou"
count= 0

for char in str1:
    if char.isalpha() and char not in vowels:
        count=count+1
        print(char)

print("Question 14: Total consonants are:", count)



# Question 15: Find the longest word in "Python is a programming language"

str1= "Python is a programming language"
 
x= str1.split()

longest= max(x)

print("Question 15: Longest word is :", longest)
print(" the length is:",len(longest))


# Question 16: Remove all punctuation from "Hello, World! How are you?"



import string
str1= "Hello, World! How are you?"

result= " "

for char in str1:
    if char not in string.punctuation:
        result= result + char
print("Question 16: My string without punctuation is:",result)



# Question 17: Check if string starts with "Python"

text= "Python is the most useful language"

if text.startswith('Python'):
    print("Question 17: yes, string starts with python")
else:
    print("Question 17: No, string does not start with python")


# Question 18: Find the index of first occurrence of 'o' in "Hello World"

x= "Hello World"
index= x.find("o")
print("Question 18: The index of first o is:",index)

# to find the 2nd index of "o" in "Hello World"

x1= "Hello World"
target= "o"
count=0

for i in range(len(x1)):
    if x[i] == target:
        count+=1
        if count==2:
            print("the index of second o is:",i)
            break



# Question 19: Split string "apple,banana,orange" by comma  


x= "apple,banana,orange"

result= x.split(",")

print("Question 19: Ans is :", result)


# Question 20: Join list ['Python', 'is', 'awesome'] with spaces