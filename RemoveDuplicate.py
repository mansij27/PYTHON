# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element
# appears only once. The relative order of the elements should be kept the same.
class Solution:
    def removeDuplicates(self, nums) -> int:
        a=len(nums)
        prev = 0

        for curr in range(a):
            if nums[curr]!=nums[prev]:
                prev+=1
                nums[prev]=nums[curr]
        return prev+1

nums = [0,0,1,1,1,2,2,3,3,4]
ob=Solution().removeDuplicates(nums)
print(ob)