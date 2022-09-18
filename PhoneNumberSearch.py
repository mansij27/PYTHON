
numbers = [1234, 2356, 4642, 3456, 1239, 3572, 7859]  # key
names = ['mansi', 'anshika', 'mani', 'zy', 'mom', 'dad', 'sachin']  # value

result = dict(zip(numbers, names))
print(result)

def Phonebook(result):
    numToFind = int(input("Enter number to search:"))
    check = -1
    list = []

    for i in range(len(result)):
        if numToFind in result.keys():
            check=i
            list.append(result[numToFind])

        if check == -1:
            # query did not exist in the directory
            print("Number Doesn't exist")
            break

        else:
            print(list)
            break

Phonebook(result)