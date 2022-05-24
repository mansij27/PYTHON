nums= int(input('Enter no. of rows'))

for i in range(nums):
    for j in range(i+1):
        print(1, end="")

    print()

for i in range(nums):
    for j in range(nums-i):
        print(1, end="")

    print()