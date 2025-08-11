# Question 1: Reverse the string "Python Programming"

Str= "Python Programming"
Rev= Str[::-1]
print("Question 1: Reversed string is :",Rev)

print("-"*100)

# Question 2: Check if "racecar" is a palindrome

str1= "racecar"
str2= str1[::-1]

if str1 == str2:
    print("RaceCar is palindrome")

else:
    print("not palindrome")

print("-"*100)

# Question 3: Count the number of words in "Python is a great programming language"

str= "Python is a great programming language"
count= len( str.split())

print(" Question 3: Total letters in a string are:",count)
print("-"*100)

# Question 4: Convert "hello world" to title case


text= "hello world"

new_text= text.title()

print("Question 4: title case is:", new_text)
print("-"*100)

# Question 5: Find the length of string "Data Science"

str= "Data Science"

print("Question 5: The length of a string is:", len(str))

print("-"*100)

# Question 6: Replace all spaces with underscores in "Machine Learning"

text= "Machine Learning"

Final_Text= text.replace(" ", "_")

print("Question 6: updated text is:", Final_Text)

print("-"*100)

# Question 7: Check if "python" is in "Python Programming Language"

str= "Python Programming Language"
sub_str= "Python"
result= str.find("Python")

if result!= -1 :
    print("Question 7: string is found at position:",result)
    print(str[result: result+ len(sub_str)])

else:
    print("string not found")

print("-"*100)

# Question 8: Extract the first 5 characters from "Artificial Intelligence"

text= "Artificial Intelligence"

print("Question 8: the first five characters are:", text[0:5])

print("-"*100)

# Question 9: Convert "UPPERCASE" to lowercase

text= "UPPERCASE"

print("Question 9: The lowercase would be:", text.lower())

print("-"*100)

# Question 10: Remove all vowels from "Computer Science"

text= "Computer Science"
vowels= "aeiouAEIOU"
str= ""

for char in text:
    if char not in  vowels:
        str=str+char

print("Question 10: result is: ",str)

print("-"*100)


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

print("-"*100)

# Question 13: Capitalize first letter of each word in "python programming language"

str= "python programming language"

print("Question 13: The string would be:  ",str.title())

print("-"*100)

# Question 14: Count consonants in "Hello World"

str1= "Hello World"
vowels= "AEIOUaeiou"
count= 0

for char in str1:
    if char.isalpha() and char not in vowels:
        count=count+1
        print(char)

print("Question 14: Total consonants are:", count)

print("-"*100)

# Question 15: Find the longest word in "Python is a programming language"

str1= "Python is a programming language"
 
x= str1.split()

longest= max(x)

print("Question 15: Longest word is :", longest)
print(" the length is:",len(longest))

print("-"*100)

# Question 16: Remove all punctuation from "Hello, World! How are you?"



import string
str1= "Hello, World! How are you?"

result= " "

for char in str1:
    if char not in string.punctuation:
        result= result + char
print("Question 16: My string without punctuation is:",result)

print("-"*100)

# Question 17: Check if string starts with "Python"

text= "Python is the most useful language"

if text.startswith('Python'):
    print("Question 17: yes, string starts with python")
else:
    print("Question 17: No, string does not start with python")


print("-"*100)

# Question 18: Find the index of first occurrence of 'o' in "Hello World"

x= "Hello World"
index= x.find("o")
print("Question 18: The index of first o is:",index)

print("-"*100)

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

print("-"*100)

# Question 19: Split string "apple,banana,orange" by comma  


x= "apple,banana,orange"

result= x.split(",")

print("Question 19: Ans is :", result)

print("-"*100)


# Question 20: Join list ['Python', 'is', 'awesome'] with spaces

x = ['Python', 'is', 'awesome']

for values in x:
    print(values, end= " ")

print("-"*100)

# Question 21: Check if string contains only digits: "12345"
print("\nQuestion 21: Check if string contains only digits: '12345'")
# Your code here

str1= "12345"

if str1.isdigit():
    print("string has only digits")
else:
    print("No")

print("-"*100)

# Question 22: Check if string contains only letters: "HelloWorld"
print("\nQuestion 22: Check if string contains only letters: 'HelloWorld'")
# Your code here

str1= "HelloWorld"

if str1.isnumeric:
    print("string has only letters")
else:
    print(" string does not only have letters")

print("-"*100)

# Question 23: Convert "hello world" to "hElLo WoRlD" (alternating case)
print("\nQuestion 23: Convert 'hello world' to 'hElLo WoRlD' (alternating case)")
# Your code here

str1= "hello world"
result= " "
for i in range(len(str1)):
    if i%2 == 0:
        result+= str1[i].lower()
    else:
        result+= str1[i].upper()
print(result)

print("-"*100)

# Question 24: Find all positions of 'a' in "banana"
print("\nQuestion 24: Find all positions of 'a' in 'banana'")
# Your code here

str1= "banana"
for i in range(len(str1)):
    if str1[i]== "a":
        print(i)

print("-"*100)

# Question 25: Remove leading and trailing whitespace from "  Hello World  "
print("\nQuestion 25: Remove leading and trailing whitespace from '  Hello World  '")
# Your code here

str1= "  Hello World  "
result= str1.strip()
print(result)

print("-"*100)

# Question 26: Check if string ends with "ing": "programming"
print("\nQuestion 26: Check if string ends with 'ing': 'programming'")
# Your code here

str1= "programming"
result= str1.endswith("ing")
print(result)

print("-"*100)


# Question 27: Replace first occurrence of 'o' with '0' in "Hello World"
print("\nQuestion 27: Replace first occurrence of 'o' with '0' in 'Hello World'")
# Your code here

str1= "Hello World"
result= str1.replace("o","0",1)
print(result)
print("-"*100)


# Question 28: Find the shortest word in "Python is a programming language"
print("\nQuestion 28: Find the shortest word in 'Python is a programming language'")
# Your code here

str1= "Python is a programming language"
result= str1.split()

shortest_word= min(result, key=len)
print(shortest_word)
print("-"*100)


# Question 29: Count words that start with 'p' in "Python programming is powerful"
print("\nQuestion 29: Count words that start with 'p' in 'Python programming is powerful'")
# Your code here

str1= "Python programming is powerful"
result= str1.split()
count=0
for items in result:
    if items.lower().startswith("p"):
        count=count+1

print(count)

print("-"*100)


# Question 30: Reverse words in "Hello World Python"
print("\nQuestion 30: Reverse words in 'Hello World Python'")
# Your code here
# Question 30: Reverse words in "Hello World Python"

str1= "Hello World Python"
result= str1.split()

for word in result:
    reversed_word= word[::-1]
    print(reversed_word)


print("-"*100)


# Question 31: Check if string is a valid email format: "user@example.com"
print("\nQuestion 31: Check if string is a valid email format: 'user@example.com'")
# Your code here
import re

email= "user@example.com"
pattern= r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match (pattern, email):
    print("valid email format")
else:
    print("not a valid email format")


print("-"*100)


# Question 32: Extract domain from "https://www.example.com/path"
print("\nQuestion 32: Extract domain from 'https://www.example.com/path'")
# Your code here

from urllib import urlparsed

url= "https://www.example.com/path"
parsed_url= urlparsed(url)
domain= parsed_url.netloc
print(domain)
print("-"*100)

# Question 33: Count lines in multi-line string
print("\nQuestion 33: Count lines in multi-line string")
# Your code here

multi_line_string= """first line
                    second line
                    third line"""

line_count= len(multi_line_string.splitlines())
print(line_count)
print("-"*100)

# Question 34: Find common characters between "hello" and "world"
print("\nQuestion 34: Find common characters between 'hello' and 'world'")
# Your code here

str1= "hello"
str2= "world"

common_char = set (str1) & set (str2)
print(common_char)
print("-"*100)

# Question 35: Check if string is a valid phone number: "+1-555-123-4567"
print("\nQuestion 35: Check if string is a valid phone number: '+1-555-123-4567'")
# Your code here

import re
phone= "+1-555-123-4567"
pattern= r"^\+\d{1,3}-\d{3}-\d{3}-\d{4}$"

if re.match(pattern, phone):
    print("valid number")
else:
    print("invalid pattern")

print("-"*100)


# Question 36: Extract numbers from "abc123def456ghi789"
print("\nQuestion 36: Extract numbers from 'abc123def456ghi789'")
# Your code here

import re
text= "abc123def456ghi789"

numbers= re.findall(r"\d+",text)
print(numbers)
print("-"*100)


# Question 37: Convert "snake_case" to "camelCase"
print("\nQuestion 37: Convert 'snake_case' to 'camelCase'")
# Your code here


snake_case= "snake_case"
parts= snake_case.split("_")

camel_case= parts[0]+ "".join(word.capitalize()for word in parts[1:])

print(camel_case)
print("-"*100)


# Question 38: Check if string is a valid palindrome ignoring case: "A man a plan a canal Panama"
print("\nQuestion 38: Check if string is a valid palindrome ignoring case: 'A man a plan a canal Panama'")
# Your code here

str1= "A man a plan a canal Panama"

cleaned= "".join(char.lower() for char in str1 if char.isalnum())

is_palindrome= cleaned == cleaned[::-1]
print(is_palindrome)
print("-"*100)


# Question 39: Find the most common word in "the quick brown fox jumps over the lazy dog"
print("\nQuestion 39: Find the most common word in 'the quick brown fox jumps over the lazy dog'")
# Your code here

from collections import Counter

str1= "the quick brown fox jumps over the lazy dog"
word= str1.split()

word_counter= Counter(word)
most_common= word_counter.most_common(1)[0]

print(most_common)
print("-"*100)


# Question 40: Generate acronym from "National Aeronautics and Space Administration"
print("\nQuestion 40: Generate acronym from 'National Aeronautics and Space Administration'")
# Your code here
str1= "National Aeronautics and Space Administration"

word= str1.split()
ignore_words= {"and", "of", "the"}

acronym = "".join(w[0].upper() for w in word if w.lower() not in ignore_words)

print(acronym)
print("-"*100)

# Question 41: Check if string contains balanced parentheses: "((()))"
print("\nQuestion 41: Check if string contains balanced parentheses: '((()))'")
# Your code here


def bal_paranthesis(s):
    count= 0
    for char in s:
        if char == "(":
            count= count+1
        elif char == ")":
            count= count-1
        if count<0:
            return False 
    return count == 0  


string = "((()))"
print("Balanced:" if bal_paranthesis(string) else "Not balanced.")

print("-"*100)

# Question 42: Convert "hello world" to Morse code
print("\nQuestion 42: Convert 'hello world' to Morse code")
# Your code here

morse_code_dict = {
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',
    'e': '.',     'f': '..-.',  'g': '--.',   'h': '....',
    'i': '..',    'j': '.---',  'k': '-.-',   'l': '.-..',
    'm': '--',    'n': '-.',    'o': '---',   'p': '.--.',
    'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
    'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',
    'y': '-.--',  'z': '--..',  '0': '-----', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'  
}

text = "hello world"
morse = ' '.join(morse_code_dict[char] for char in text.lower())

print("Morse code:", morse)
print("-"*100)


# Question 43: Find the longest common substring between "programming" and "grammar"
print("\nQuestion 43: Find the longest common substring between 'programming' and 'grammar'")
# Your code here


# Question 44: Check if string is a valid URL: "https://www.google.com"
print("\nQuestion 44: Check if string is a valid URL: 'https://www.google.com'")
# Your code here

# Question 45: Extract all words with length > 5 from "Python programming is amazing and powerful"
print("\nQuestion 45: Extract all words with length > 5 from 'Python programming is amazing and powerful'")
# Your code here

# Question 46: Convert "hello world" to Pig Latin
print("\nQuestion 46: Convert 'hello world' to Pig Latin")
# Your code here

# Question 47: Check if string is a valid IPv4 address: "192.168.1.1"
print("\nQuestion 47: Check if string is a valid IPv4 address: '192.168.1.1'")
# Your code here

# Question 48: Find all substrings of "abc"
print("\nQuestion 48: Find all substrings of 'abc'")
# Your code here

# Question 49: Convert "hello world" to ROT13 encoding
print("\nQuestion 49: Convert 'hello world' to ROT13 encoding")
# Your code here

# Question 50: Check if string is a valid credit card number: "4532015112830366"
print("\nQuestion 50: Check if string is a valid credit card number: '4532015112830366'")
# Your code here 


