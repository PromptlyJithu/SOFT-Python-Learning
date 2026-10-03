# Day 03 - Operators

first_number = 10
second_number = 3

print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)
print("Division:", first_number / second_number)
print("Floor division:", first_number // second_number)
print("Remainder:", first_number % second_number)
print("Exponentiation:", first_number**second_number)

print("Is first number greater", first_number > second_number)
print("Are the numbers equal", first_number == second_number)

# Calculating area of a circle \ (**) is pow()
radius = 10
area_of_circle = 3.14 * radius ** 2
print('Area of a circle:', area_of_circle)

# Calculating a weight of an object
mass = 65
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('J in Jithu', 'J' in 'Jithu')  # True - J found in the string
print('i in Jithu', 'i' in 'Jithu')  # False -there is no uppercase I

print(not False)     # True
print(not not True)  # True
print(not not False)  # False