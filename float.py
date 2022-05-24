FloatNumbers=[]
n=int(input('Enter list size'))
print('Enter float values')

for i in range(0,n):
    item=float(input())
    FloatNumbers.append(item)
    print('%.2f' %item)

print('User list is:', FloatNumbers)