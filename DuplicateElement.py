"""program to print duplicate numbers in a given list"""
from collections import Counter

# METHOD 1
arr = [3, 4, 1,5,5,3,1]
print("Duplicate elements in given array: ")

# Searches for duplicate element
def Solution(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] == arr[j]):
                print(arr[j])

Solution(arr)

# METHOD 2
nums = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

def findDuplicate(nums):
	result=[]
	x=Counter(nums) #Counter imported
	# k=Counter.values(x)
	print(x)
	# print(k)
	for a in x:
		if x[a]>1:
			result.append(a)
	print(result)

findDuplicate(nums)