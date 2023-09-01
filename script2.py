user_input = input("Enter a string: ")

lowercase_letters = ''.join([char for char in user_input if char.islower()])
uppercase_letters = ''.join([char for char in user_input if char.isupper()])
print(lowercase_letters + uppercase_letters)
