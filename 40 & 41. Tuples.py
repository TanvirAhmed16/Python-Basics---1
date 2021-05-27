# Tuples - Tuples are simply lists that are immutable. As a good programmer, we can use tuples where value of something need not to change.
my_tuple = (1,2,3,4,5,5)
print(my_tuple)

# We can perform many operations on tuple like lists. Like...
new_tuple = my_tuple[1:4]
print(new_tuple)

# We can also asign multiple Value.
x, y, z, *other = (1,2,3,4,5,5)
print(x)
print(y)
print(z)
print(other)

# Tuple Methods ( Count & Index)
print(my_tuple.count(5))
print(my_tuple.index(5))

# Tuple Functions
print(len(my_tuple))