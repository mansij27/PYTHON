""" Return count of ranges array"""

def CountRange(nums):
    result = []
    op=0
    n=len(nums)
    for i in range(1,n+1):
        # if only 1 element or difference 1 nhi hai
        if (i == n or nums[i] -nums[i - 1] != 1):
            op+=1
        else:
            result.append(nums[i])
    print(op)

#TEST CASES
nums=[0,1,2,6,9,10]
# nums=[0,2,3,4,6,8,9]
# nums=[1,2,4,6,7,9,12]

CountRange(nums)


