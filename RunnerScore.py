if __name__ == '__main__':
    n = int(input("Number"))
    arr = map(int, input("Enter").split())
    a = list(arr)

    lists = []
    maximum = max(a)

    for i in a:
        if maximum == i:
            pass
        else:
            lists.append(i)

    print(max(lists))

