def get_unique_list(input_list):
    return list(dict.fromkeys(input_list))

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)
