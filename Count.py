def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd

lst = [12,4,5,2,8,7,9,34,65,46]

even, odd = count(lst)
print('Even: {} Odd: {}'.format(even, odd))