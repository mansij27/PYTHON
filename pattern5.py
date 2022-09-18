"""
ALPHABETS PATTERN RIGHT PYRAMID
"""

n= int(input("Enter number of rows"))
num = 65 # initializing value corresponding to 'A' ASCII value

for i in range(0, n):
    for j in range(0, i + 1):
        ch = chr(num) # explicitly converting to char

        print(ch, end=" ")
        num = num + 1
    print("\r")