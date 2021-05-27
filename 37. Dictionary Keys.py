# Dictionary Keys - It is better to use string as a dictionary keys as dictionary keys needs to be unique and strings are immutable.

dictionary = {
  123 : [1,2,3],
  123 : 'Hello',
  'Greet' : 'Hi'
}
print(dictionary[123])
print(dictionary['Greet'])