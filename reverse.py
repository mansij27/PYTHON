print('Enter your number')
number=int(input())

while number>0:
    digit = number % 10
    number=number//10

    print('Reverse of number is', digit)