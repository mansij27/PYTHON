n = int(input("Enter the number of rows and columns :"))
matrix= []
# Entering values in matrix
for i in range(n):
    a = []
    for j in range(n):  # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)

# matrix print
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()

def find(n,k):
    if (n + 1 >= k):
        return (k - 1)
    else:
        return (2 * n + 1 - k)

k = int(input(" enter Frequency"))
freq = find(n,k)

if (freq == 3 ):
    print(" Frequency of ", k, " is ", freq)
else:
    print(" element not exist, -1")


