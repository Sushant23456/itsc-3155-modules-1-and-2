numbers = []

while True:
    value = input("Enter a number(or type 'QUIT' to quit): ")
    if value == "QUIT":
        break
    numbers.append(int(value))

evens = [num for num in numbers if num % 2 == 0]

print("All NUMS:", numbers)
print("Even NUMS:", evens)