from array import *

n=int(input('Enter size of of array'))

arr= array('i', [] )

for i in range(n):
    x=int(input('Enter value of array'))
    arr.append(x)
print(arr)

val= int(input('Enter value to search'))

i=0
for i in arr:
    if i==val:
        print("Value found at", arr.index(val))
        i += 1
        break
else:
    print("Not found")




