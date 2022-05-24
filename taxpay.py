print('Enter your income')
income=int(input())
taxpayable=0
print('Given Income is:', income)

if income<=10000:
    taxpayable=0
elif income<=20000:
    taxpayable=(income-10000)*10 /100
else:
    taxpayable=0
    taxpayable=10000*10 / 100
    taxpayable+=(income-20000)*20/ 100

print('Total tax to be paid', taxpayable)
