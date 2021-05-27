# Type Conversion -  This means convorting anythings data type like str--->int, int--->str, int--->float etc.

print(type(str(100)))
print("\n")

print(type(int(str(100))))
print("\n")

# The above thing can also be done like...
a = str(100)
b = int(a)
c = type(b)
print(c)
