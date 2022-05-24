from array import *

n=int(input('Enter index length of array'))

arr= array('i', [] )

for i in range(n):
    x=int(input('Enter value of array'))
    arr.append(x)

print(arr)
val= int(input('Enter value to search'))

k=0
for e in arr:
    if e==val:
        print(k)
    else:
        break

    k+=1

    print(arr.index(val))