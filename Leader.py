"""Return the leader value. An element is leader if it is greatest than all elements to its right side.
Rightmost element is always a leader"""

list=[]
nums=[16,19,4,3,8,3]
a=len(nums)

for i in range(1,a):
    for j in range(i+1, a):
    # nums[::-1]
        if nums[i]>nums[j]:
            list.append(nums[i])

            break
        # if nums[j]==len(nums):
        #     print(nums[j])

print(list)

