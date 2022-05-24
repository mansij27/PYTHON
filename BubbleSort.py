def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

        print(nums)
        
nums=[2,5,9,4,0,1,8]

sort(nums)

print(nums)
