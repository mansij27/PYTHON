n=int(input("Enter number"))

factorial=1

if n<0:
    print("Error! Not possible for Negative number")

elif n == 0:
    print(1)

else:
    for i in range(1, n+1):
        factorial= factorial*i
    print("Factorial of the number", n, "is", factorial)