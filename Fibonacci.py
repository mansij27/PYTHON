"""Fibonacci print numbers only in between a range"""
# solution Not found

a=int(input("Enter number"))
b=int(input("Enter number"))
def Fibonacci(a,b):
    # a=0
    # b=1
    # count =0
    sum=0

    while sum<=100:
    # while sum in range(20,100):
        print(sum)
        sum=a+b
        a=b
        b=sum
        # count+=1
        # if sum>=20 or sum<=100:

# n=int(input("Enter number"))
Fibonacci(a,b)