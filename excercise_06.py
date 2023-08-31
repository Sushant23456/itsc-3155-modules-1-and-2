row = int(input("Enter row num from 1 - 5: "))
col = int(input("Enter column num from 1 - 5: "))

for r in range(1, 6):
    line = []
    
    for c in range(1, 6):
        if r == row and c == col:
            line.append('1')
        else:
            line.append('0')
    
    print(' '.join(line))