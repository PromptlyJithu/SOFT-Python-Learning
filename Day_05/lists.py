# Day 05 - Lists

skills = ["Python", "C++", "HTML"]

print("Skills:", skills)
print("First skill:", skills[0])
print("Last skill:", skills[-1])

skills.append("JavaScript")
print("After adding a skill:", skills)

skills.remove("HTML")
print("After removing a skill:", skills)

print("Number of skills:", len(skills))


fruits = ['banana', 'orange', 'mango', 'lemon']

# Slicing items
all_fruits = fruits[0:4]  # it returns all the fruits

# checking items
does_exist = 'banana' in fruits
print(does_exist)  # True

#deleting items
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon']

# clear
fruits.clear()
print(fruits)       # []

#literally counting the number of occurrences of an item in a list
print(fruits.count('orange'))   # 1

# index
print(fruits.index('orange'))   # 1

#reverse
fruits.reverse()
print(fruits.reverse())