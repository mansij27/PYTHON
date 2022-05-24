print('Enter two numbers')

num1=20
num2=30

def Multi_Sum(num1, num2):
    product=num1*num2
    if product <=1000:
        return num1*num2
    else:
        return num1+num2

result= Multi_Sum(num1,num2)
print('The result is:', result)