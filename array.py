if __name__ == '__main__':

 n = int(input('Enter your number'))
 factorail= 1

 if n<0:
    print('Error, negative is not possible')

 elif n == 0:
    print(1)

 else:
    for i in range(1, n+1):
        factorail= factorail* i
    print('Factorial of',  n, 'is' , factorail)
