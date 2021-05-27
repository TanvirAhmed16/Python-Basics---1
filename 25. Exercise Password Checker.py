user_name = input("Enter user name: ")
password = input("Enter password: ")

password_length = len(password)
hidden_password = '*' * password_length

print(f"Hey {user_name}, your password {hidden_password} is {password_length} letters long.") 