class Solution:
    def maxSubArray(self, nums) -> int:
        answer, temp_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            temp_sum = max(temp_sum + nums[i], nums[i])
            if temp_sum > answer:
                answer = temp_sum
        return answer

nums = [1,-2,4,-4,8,3]
m=Solution().maxSubArray(nums)
print(m)