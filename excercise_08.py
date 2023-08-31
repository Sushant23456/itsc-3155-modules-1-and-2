numbers = []
for i in range(10):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

unique_numbers = []
for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)

print("Original List:", numbers)
print("Nums that appear once:", unique_numbers)
