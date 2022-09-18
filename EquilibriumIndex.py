class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums) #calculating total sum of nums
        leftsum = 0
        for i, x in enumerate(nums):
            # calculating left sum by subtracting from total and the current index value
            if leftsum == (S - leftsum - x): #if not equal
                return i
            leftsum += x #incrementing left sum value
        return -1

nums = [1, 7, 3, 6, 5, 6]
p= Solution().pivotIndex(nums)
print("Equilibrium index is", p, "Value is",nums[p])