# Day 07 - Sets

completed_topics = {"variables", "strings", "lists", "strings"}
new_topics = {"tuples", "sets"}

print("Completed topics:", completed_topics)
print("Unique topic count:", len(completed_topics))
print("All topics:", completed_topics | new_topics)

#checking if an item exists in a set

st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True

#adding items to a set
st.add('item5')

#adding multiple items to a set
st.update(['item5','item6','item7'])

#remove
st.remove('item1')

#pop removes a random item from the set
st.pop()

#clear removes all items from the set
st.clear()
#del 
del st

# joining sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) #st3 = st1 | st2

#intersection

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}

#checking if subset or superset

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True

#disjoint sets
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

