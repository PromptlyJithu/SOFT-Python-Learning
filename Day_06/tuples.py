# Day 06 - Tuples

coordinates = (10, 20)

print("Coordinates:", coordinates)
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])
print("Number of coordinates:", len(coordinates))

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]

all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]

# chnging tuple to list
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

#checking if an item exists in a tuple
'item2' in tpl # True

#joining tuples
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

#del
del tpl1