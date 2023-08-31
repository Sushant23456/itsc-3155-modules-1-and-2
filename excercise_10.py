user_string = input("Enter a string: ")

char_list = list(user_string)

grouped_lists = [char_list[i:i+3] for i in range(0, len(char_list), 3)]

print(grouped_lists)