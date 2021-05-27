# There are many list methods present in python which helps to ease any operation connected with lists. Insted of using function, it is good to use methods in lists.
basket = [1,2,3,4,5]
print(len(basket)) # It is a function.

# Methods in Lists
# For adding (append, insert, extend)
basket.append(100)
new_list = basket
print(basket)
print(new_list)
basket.insert(2, 10)
print(basket)
basket.extend([101])
print(basket)
basket2 = [6,7,8,9]
basket.extend(basket2)
print(basket)

# Different methods works differently.
# For removing (pop, remove, clear)
basket.pop()
print(basket)
basket.pop(0) # pop works with index but it returns the poped value.like
new_list = basket.pop(4)
print(new_list)
print(basket)

basket.remove(4) # remove works with value.
print(basket)

basket.clear()
print(basket)

# 2
# List Methods Cont...

basket = ['a','b','c','d','e','d']
print(basket)
print(basket.index('c'))
print(basket.index('b', 0, 3))

# In some point it is easy to use python keywords.

print('e' in(basket))
print('t' in('My name is Tanvir'))

print(basket.count('d'))

# 3
# List Methods Cont...

basket = [1,2,3,7,9,5,4,10]
basket.sort()
print(basket)

basket2 = ['a','b','c','d','e','d']
basket2.sort() # This does't return any value. We can do the same thing using a build-in function.
print(basket2)

basket3 = ['a','x','z','d','e','d']
print(sorted(basket3)) # Here sorted() produces a new list that works like list slicing.
print(basket3)

new_basket = basket3.copy()
new_basket.sort()
print(new_basket)
print(basket3)

basket3.reverse()
print(basket3) # Though it is reversed, it is not sorted. SOn insted of this we can do this.
basket3.sort()
basket3.reverse()
print(basket3)