"""Returns the first missing positive number"""

def MissingInt():
    list = []
    res = 1

    for ele in range(n):
        nums = int(input("Enter element"))
        list.append(nums)
    print(list)

    list.sort()
    for a in list:
        if a == res:
            res += 1
    print("Missing positive integer is: ", res)

n = int(input("Enter list size"))
MissingInt()