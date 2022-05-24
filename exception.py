a=2
b=0

try:
    print('Resouce open')
    print(a/b)

except ZeroDivisionError as e:
    print('Cannot divide by zero...', e)

try:
    k=int(input('Enter a number'))
    print(k)

except ValueError as e:
    print('k cannot be a character ')

finally:
    print('Resource closed')