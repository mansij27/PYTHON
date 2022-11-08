num= int(input("Enter any number: "))
flag=False

if num>1:
    for i in range(2,num):
        if (num % i)==0:
            flag=True
            break

if flag:
    print(num, 'is Not Prime number')
else:
    print(num , "is Prime number")