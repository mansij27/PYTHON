"""Return array of quaternity such that nums[a]+nums[b]+nums[c]+nums[d]=target"""

def fourSum(nums,target):
    nums.sort()
    result=[]
    print(nums)

    # for i in range(len(nums)):
    #     if nums[i]>=target/4:
    #         break
    #
    #
    # print(result)

    for i in range(len(nums)-3):
        if nums[i]>target/4.0:
            break
        if i>0 and nums[i]==nums[i-1]:
            continue
        target2 = target - nums[i]
        for j in range(i+1,len(nums)-2):
            if nums[j]>target2/3.0:
                break
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            k=j+1
            l=len(nums)-1
            target3=target2-nums[j]

            if nums[k]>target3/2.0:
                continue
            while k>l:
                sum_value=nums[k]+nums[l]
                if sum_value==target3:
                    result.append([nums[i], nums[j], nums[k], nums[l]])
                    kk=nums[k]
                    k+=1
                    while k<l and nums[k]==kk:
                        k+=1
                    ll=nums[l]
                    l-=1
                    while k<l and nums[l]==ll:
                        l-=1
                elif sum_value <target3:
                    k+=1
                else:
                    l-=1
    print(result)

# TEST CASES
# nums = [1, 0, -1, 0, -2, 2]
# target = 0
nums=[2,2,2,2,2]
target=8

fourSum(nums, target)


