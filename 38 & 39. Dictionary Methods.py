# Let's see some dictionary methods.

user = {
  'basket' : [1,2,3],
  'greet': 'Hello',
}
print(user['basket'])

# If we want to check whether a property is present in a dictionary or not, we should use .get method to avoid errors in code. Like
#print(user['age']) If we run this we will get an error as age is not present, so insted of doing that we should do this

print(user.get('age'))

# We can also set a default value for absent properties.
print(user.get('age', 'Not present in Dictionary.')) #  But if the property is present then it won't show the default value.

user1 = {
  'basket' : [1,2,3],
  'greet': 'Hello',
  'age' : 55
}
print(user1.get('age', 'Not present in Dictionary.'))

# 2
# Dictionary Methods cont...

user = {
  'basket' : [1,2,3],
  'greet': 'Hello',
  'age' : 55
}
# Same as string, we can check whether an item is present in the dictionary or not.
print('basket' in (user))

# We can also check with keys or values.
print('basket' in user.keys())
print('Hi' in user.values())
print(user.items())

user2 = user.copy()
print(user)
print(user2)

user.pop('age')
print(user)
user2.popitem()
print(user2)

user.update({'greet' : 'Hey'})
print(user)
user.update({'sports': 'Cricket'})
print(user)

user.clear()
print(user)