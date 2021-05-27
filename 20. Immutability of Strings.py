'''
Immutable means something that is created can not be changed. In Python we can't change an element of a
string once it is created. The only way we can change it is to create a new string.
'''

numbers = "01234567"
print(numbers + "\n")

# numbers[4] = 6 -- We can't do this as we can't change the value.
numbers = numbers + "8" # We can do that.
print(numbers + "\n")

# Or we can creat a new string.
new_numbers = "987654321"
print(new_numbers + "\n")
