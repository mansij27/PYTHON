num= int(input("Enter any number"))
i=2
while range(2,num):
    if num % i==0:
        print("Not Prime")
        break
    else:
        print("Prime")
        break
