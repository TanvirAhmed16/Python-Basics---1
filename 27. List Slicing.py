# List Slicing -  List Slicing is simillar to string slicing. We can slice list items by their index number. But most importantly unlike string Lists are immutable, that means we can modify list items.

amazon_cart = [
 'Notebooks',
 'Sunglasses',
 'Toys',
 'Bike']
print(amazon_cart)
print(amazon_cart[0:2])
print(amazon_cart[0::2])

amazon_cart[0]='Laptop'
print(amazon_cart)

# List Slicing is generally used to copy the values of an old list to a new one. So if we don't use list slicing to copy the values then that will reffer to the memory address of the old list. Like suppose...
new_cart = amazon_cart # Here new_cart will reffer to the memory address of amazon_cart and thats why amazon_cart will change also.
new_cart[0] = 'Phone'
print(new_cart)
print(amazon_cart)

# But if we use list slicing then new_cart will copy the values of amazon_cart which will not affect amazon_cart. Like...

new_cart = amazon_cart[0:3]
new_cart[0] = 'Football'
print(new_cart)
print(amazon_cart)