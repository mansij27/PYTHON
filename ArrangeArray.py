"""Arrange the array with negatives on the left and positive on right. Order of appearance should be same.
Consider 0 as positive"""

def rearrange(nums):
    positive = [val for val in nums if val >= 0]
    negative = [val for val in nums if val < 0]
    result=negative+positive
    print(result)

# TEST CASES
# nums = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
nums=[14 ,13 ,-15 ,-5,6,-7,5,-3,-6]
# nums=[-12, 11, -13, -5, 6, -7, 5, -3, 11]
# nums=[1, 9, -3, 6, 8, 11, 35, -5, -7, 10, -1, -2, -3]

rearrange(nums)


# METHOD 2 WRONG OUTPUT LAST M BAKI SAHI HAI
# j = 0
# for i in range(0, n):
#     if (arr[i] < 0):
#         temp = arr[i]
#         arr[i] = arr[j]
#         arr[j]= temp
#         j = j + 1
#     if (arr[i]>= 0):
#         continue
# print(arr)



