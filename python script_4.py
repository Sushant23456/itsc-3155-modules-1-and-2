def get_valid_integer():
    while True:
        try:
            value = int(input("Enter INT: "))
            return value
        except ValueError:
            print("That's not a valid integer. Please try again.")

def main():
    total = 0
    for i in range(5):
        total += get_valid_integer()
    print(f"Your sum is: {total}")

main()
