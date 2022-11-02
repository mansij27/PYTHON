n=int(input("Enter no of rows:"))
"""
1 
1 4 
1 4 9 
1 4 9 16 
1 4 9 16 25 """
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j**2,end=" ")

    print()

print(end="\n")
# square series of first column value
"""
1 
2 4 
3 9 27 
4 16 64 256 """
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i**j,end=" ")

    print()
