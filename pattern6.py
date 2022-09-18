"""
1
2 3
4 5 6
7 8 9 10
n numbers sequence in pyramid
"""

n= int(input("Enter no. of rows"))
num=1

for i in range (0,n):
    for j in range(0,i+1):
        print(num, end=" ")

        num +=1

    print()
