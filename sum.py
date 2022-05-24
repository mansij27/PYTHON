def NumSum(num):
    previosnumber=0
    for i in range(num):
        sum=previosnumber+i
        print('Previous Number', previosnumber, 'Current number', i, 'Sum', sum)
        previosnumber=i

NumSum(10)