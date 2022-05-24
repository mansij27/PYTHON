print('List of numbers')

def divisible(lst):
    for num in lst:
        if num % 5 == 0:
            print(num)

lst = [2, 45, 7, 5, 20, 49, 55]

divisible(lst)
