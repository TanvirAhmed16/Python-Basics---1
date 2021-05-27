name = 'Tanvir'
age = 25
print("Hi " + name + "You are " + str(age) + " years Old.\n")

# We can easily do the same thing by using the option called Formatted String where we don't need to convert data types of other variables. It is a feature of Python 3.

name = 'Ahmed'
age = 25
print(f"Hi {name}. You are {age} years Old.\n")

# In Python 2 the same feature was implemented using .format

print("Hi {}. You are {} years Old.\n" .format('Niloy', 22))

name = 'Tan'
age = 28
print("Hi {}. You are {} years Old.\n" .format(name, age))

print("Hi {}. You are {} years Old.\n" .format(age, name))

print("Hi {1}. You are {0} years Old.\n" .format(name, age))

print("Hi {new_name}. You are {age} years Old.\n" .format(new_name= "Jonny", age= 50))