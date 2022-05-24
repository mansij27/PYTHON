def pynative(str):
    for i in range(0, len(str)-1,2):
        print('index [',i,']', str[i])

inputStr=str(input('Enter your string'))
print('Original string is:', inputStr)

pynative(inputStr)