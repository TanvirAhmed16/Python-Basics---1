# Here we will talk about some common list patterns.

basket = ['a','x','z','d','e','d']
basket.sort()
basket.reverse()
print(len(basket))
print(basket)
# We can also reverse the list using list slicing like string slicing with the help of their index.

basket1 = ['i','x','z','d','f','d']
basket1.sort()
basket1.reverse()
print(basket1[::-1])
print(basket1)

# Range- range is for generating a list very quickly.
print(list(range(1,100)))
print(list(range(100)))

# .Join - Join is actually something that works with string. It is iterable, that means it will join with every string.
sentence = '!'
new_sentence = sentence.join(['Hey ', 'there', 'my', 'name', 'is', 'Tanvir.'])
print(new_sentence)

# We can also do the same like...
new_sentence = ' '.join(['Hey ', 'there', 'my', 'name', 'is', 'Tanvir.'])
print(new_sentence)