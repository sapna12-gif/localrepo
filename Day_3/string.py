# create string variable
# Example1: these are the four ways we can store stringvalue into variable.
""" s="welcome"
s='welcome'
s=str('welcome')
s=str("welcome") """

# creating empty string variables
""" name=""
name=''
name=str() """

# Example2: ways of creating string variables
# mutable- cann change the value of the variable
# immutable - cannot change the value of variable
# string is immutable
""" str1='welcome'
print(id(str1)) # 2984541559472

str1=str1+"to python"
print(id(str1)) """

# if the value is changed after updation then it is mutable.


# Example 3: + and * with string
""" str="welcome"
print(str+"programming") # concatenation/joining
print(str*2) """

# Example4: Slicing
#starting index 0
#ending index 1
""" str="welcome"
print(str[1:3]) #el
print(str[:6]) # welcom here starting index is 0 by default)
print(str[2:]) #lcome
print(str[1:-1]) #elcom """

# Example5: ord() and chr()
""" print(ord('A')) #65, returns the ASCII code of character
print(chr(65)) #A, returns character represented by a ASCII number.
 """

# Example6: max(), min(), len()
""" print(max("abc"))
print(min('abc'))
print(len('abc')) """

#Example7: in, not in operators
""" s= 'welcome'
print('come' in s) # True
print('lomee' in s) # false

print('come' not in s) #False
print('lone' not in s) # true """

#Example8: String comparision
""" print('tim'=='tie') # False
print('free' !="freedom") # False
print('arrow'>'aron')#True
print('right'>='left') #True
print('teeth'< 'tee')#False
print('yellow' <= 'fellow') #false
print('abc'>"") #True """

# Example9: Testing Strings True/False
""" s="welcome to python"

print("Welcome".isalpha())#True
print(s.isalnum()) #False

print("2012".isdigit()) #True

print("first Number".isidentifier())#False

print(s.islower()) #True
print("WELCOME".isupper()) #True

print("".isspace()) #True """

# Example10: Searching for Substrings
""" s="welcome to python"
print(s.endswith("thon")) # true

print(s.startswith("good")) #false

print(s.find("come")) #3

print(s.find("become")) #-1 not found
print(s.count("t")) # 2 #Returns number of occurrences of substring the string
 """
#Example11: Converting String
s="String in PYTHON"
s1=s.capitalize()
print(s1) #string in python

s2=s.title()
print(s2) #String In Python

s3 = s.lower()
print(s3) #string in python

s4 = s.upper()
print(s4) #STRING IN PYTHON

s5 = s.swapcase()
print(s5) #sTRING IN python

s6 = s.replace("in","on")
print(s6) #String on PYTHON

#Example12: Reverse a string
#Method1
s='welcome'
rev_str=""
for i in s:
    rev_str=1+rev_str #e
print("reversed string is:",rev_str) #emoclew

#Method2
s='welcome'
rev_str=s[::-1] #s[0:7:-1]
print(rev_str)
