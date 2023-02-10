FloatNumbers=[]
n = int(input("Enter list size:"))
print('Enter float')

for i in range(0, n):
    item = float(input())
    FloatNumbers.append(item)
    print('%.1f' % item)

print("User List is", FloatNumbers)





