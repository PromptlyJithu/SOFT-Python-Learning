# Day 04 - Strings

message = "Hello World"

print("Message:", message)
print("Length:", len(message))
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("First word:", message.split()[0])
print("First letter capitalized:", message.capitalize())
print("Contains 'World':", "World" in message)
multiline_string = """This is a multiline string
It can span multiple lines."""
print( multiline_string)

# String Concatenation
first_name = 'Jithu'
last_name = 'Jomon'
space = ' '
full_name = first_name + space + last_name
print(full_name)
print(len(first_name)) 
print(len(last_name))   
print(len(first_name) > len(last_name))
print(len(full_name))

language = 'Python'
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter)  # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n


language = 'Python'
# starts at zero index and up to 3 but not include 3
first_three = language[0:3]
last_three = language[3:6]
print(last_three)  # hon

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2]
print(pto)  # pto

# find(): Returns the index of first occurrence of substring

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

# format()	formats string into nicer output


radius = 10
pi = 3.14
area = pi  # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result)  # The area of circle with 10 is 314.0

# isalnum(): Checks alphanumeric character

challenge = 'ThirtyDaysPython'
print(challenge.isalnum())  # True

challenge = '30DaysPython'
print(challenge.isalnum())  # True

challenge = 'thirty days of python'
print(challenge.isalnum())  # False

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result)  # 'HTML# CSS# JavaScript# React'\

# title(): Returns a Title Cased String

challenge = 'thirty days of python'
print(challenge.title())  # Thirty Days Of Python

# swapcase(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
