row = int(input('Enter no of rows: '))

for i in range(1, row + 1):
    # for space
    for j in range(1, row + 1 - i):
        print(' ', end='')

    # for increasing pattern
    for j in range(1, i + 1):
        print(j, end='')

    # for decreasing pattern
    for j in range(i - 1, 0, -1):
        print(j, end='')

    print()
