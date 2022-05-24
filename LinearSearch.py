pos = -1

def search(list, n):
    i = 0

    while i<len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i+1

    return False

list = [13,7,9,4,23]
n = 13

if search(list, n):
    print('Value Found', pos+1)
else:
    print('Value not found')