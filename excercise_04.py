n = int(input("Enter a number, n: "))
floats = [float(input(f"Enter number {i+1}: ")) for i in range(n)]
mean = sum(floats) / n
print("List:", floats)
print("Average:", mean)