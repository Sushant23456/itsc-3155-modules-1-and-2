list1 = [int(input("Enter number for list 1: ")) for _ in range(5)]
list2 = [int(input("Enter number for list 2: ")) for _ in range(5)]

common = list(set(list1) & set(list2))

print("List 1:", list1)
print("List 2:", list2)
print("Common values:", common)
