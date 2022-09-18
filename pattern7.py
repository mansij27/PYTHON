"""
1
* *
1 2 3
* * * *
1 2 3 4 5
number sequence and star alternating line
"""
n= int(input("Enter no. of rows"))
num=1

for i in range (0,n+1):
    for j in range(1,i+1):
        if i%2==0:
            print("*", end=" ")
        else:
            print(j, end=" ")

    print()