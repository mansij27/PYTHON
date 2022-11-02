x= int(input("Enter size of list: "))
list=[]
print("Enter Elements in ascending order")


for i in range(x):
    ele = int(input("Enter element: "))
    list.append(ele)
print(list)

n= int(input("Enter element to search: "))
pos= -1

def search(list,n):
   l=0
   u=len(list)-1

   while l<=u:
       mid=(l+u)//2
       if list[mid]==n:
           globals()['pos'] = mid
           return True
       else:
           if list[mid]<n:
               l=mid
           else:
               u=mid

if search(list,n):
    print("Found at", pos + 1)
else:
    print("Not Found")
# INPUT TESTS
# list=[4,7,8,12,45,99,102,702110987,56666]
# n=102

# USIND RECURSION
def binarySearch(arr, l,r,x):
    if r>=l:
        mid= l +(r-l)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarySearch(arr, l, mid-1,x)
        else:
            return binarySearch(arr, mid+1, r,x)
    else:
        return -1

arr=[2,3,4,10,40]
x=40
result=binarySearch(arr, 0, len(arr)-1,x)
if result != -1:
    print("Element is present at index %d" %result)
else:
    print("Element is not present in array")