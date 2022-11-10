"""Traingle print """

n=int(input("Enter no of rows: "))
for row in range(1,n+1):
    print(" "*(n-row)+ "* " *row)

#     k=n-1
#     for i in range(0,n):
#         for j in range(0,k):
#             print(end="")
#         k=k-1
#         for j in range(0,i+1):
#             print("*", end="")
#         print("\r")

