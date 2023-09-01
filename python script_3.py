def count_letters(s):
    letter_dict = {}
    for char in s:
        char_lower = char.lower()
        if char_lower.isalpha():
            if char_lower in letter_dict:
                letter_dict[char_lower] += 1
            else:
                letter_dict[char_lower] = 1
    return letter_dict

user_input = input("Please enter a string: ")
result = count_letters(user_input)
print(result)

