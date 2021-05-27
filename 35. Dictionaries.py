# Dictionaries - Dictionary is a data structure with a unordered key value pairs and keys needs to be unique.

dictionary = {
  'a' : 1,
  'b' : 2
  }

print(dictionary['b'])
print(dictionary)

# We can store different kind of data in a dictionary. Like
dictionary1 = {
  'a' : [1,2,3],
  'b' : 'Hello',
  'x' : True
  }
# We can access an element of the list inside dictionary like
print(dictionary1['a'][1])

# We can also have a dictionary inside a list.
my_list = [
  {
  'a' : [1,2,3],
  'b' : 'Hello',
  'x' : True
  },
  {
  'd' : [4,5,6],
  'e' : 'Hey',
  'f' : False
  }
]
print(my_list[1]['e'])