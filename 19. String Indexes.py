#--> In string every character is stored in memory with an index number. So we can easily access every character of a string with their indexes.
numbers = "01234567"
#indexes = 01234567
print(numbers + "\n")
print(numbers [2] + "\n")

# String Manipulation-- We can manupulate a string in many ways with their indexes.
# string[start:stop]
print(numbers[2:4] + "\n")

# string[start:stop:stepover]
print(numbers[0:8:3] + "\n")

# string[start:] --gap indicates to last element or from first element.
print(numbers[2:] + "\n")
print(numbers[:4] + "\n")
print(numbers[::2] + "\n")

# string[-1] -- -1 indicates last element.
print(numbers[-1] + "\n")

# string[::-1] -- For reverse string.
print(numbers[::-1] + "\n")
print(numbers[::-2] + "\n")
print(numbers[:-2] + "\n")
