""" Each employee is given a random number and game is played in batches so not all employees are playing in the selected
batch. The selection of employees in a batch are totally random and buddy is selected from a batch if there are two
employees whose employeee code matches the number called.
if buddy found, return employee code in an array, otherwise (no buddy found) """

def twoSum(nums,target):
    map={}

    for i,val in enumerate(nums):
        tg=target-val
        if tg in map:
            return [nums[map[tg]], nums[i]]
        map[val]=i
    return -1

#passing nums and target values
nums=[25,65,63,20,70]
target=90

res=twoSum(nums,target)

if res==-1:
    print("No buddy")
else:
    print(res)