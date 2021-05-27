# Sets -  Sets are simply unordered collections of unique objects. It is created with {} curly brackets like Dictionary but it doesn't have key value pairs like dictionary. It has only unique value.

my_set = {1,2,3,4,5,5}
print(my_set)

my_set.add(100)
my_set.add(2) # It doesn't add similer value.
print(my_set)

# We can also make a set from a list.
my_list = [1,2,3,4,5,5]
print(set(my_list))
print(list(my_set))

# Set objecy doesn't support indexing. So we can not access any set object with their index. So print(my_set[0]) will give error.
# But we can search any object with in function.
print(2 in (my_set))
print(len(my_set))

# We can also copy a set.
new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)

# 2
# Sets Methods.

my_set = {1,2,3,4,5,}
your_set = {4,5,6,7,8,9,10}

# .difference
print(my_set.difference(your_set))
print(my_set) # Here my_set is not updated.

# .discard
my_set.discard(5)
print(my_set)

# .difference_update
my_set.difference_update(your_set)
print(my_set) # Here my set is updated.

my_set = {1,2,3,4,5,}
your_set = {4,5,6,7,8,9,10}
# .intersection
print(my_set.intersection(your_set))
# This can also done by
print(my_set & your_set)

# .union
print(my_set.union(your_set))
# This can also done by
print(my_set | your_set)

# .isdisjoint (Is there nothing incommon?)
print(my_set.isdisjoint(your_set))

my_set = {4,5,}
your_set = {4,5,6,7,8,9,10}
# .issubset
print(my_set.issubset(your_set))

# .issuperset
print(your_set.issuperset(my_set))

# ALHUMDULLILLAH BASIC-1 IS DONE #