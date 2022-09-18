"""Remove the triplet from last. The relative order of the elemets should be kept same"""

from collections import Counter

def RemoveTriplet(nums):
    count=Counter(nums)
    print(count)
    rev=nums[::-1]
    print("Reverse", rev)
    list=[]

    for num in rev:
        if count[num]>=3:
            # a= list(filter((count[num]).__ne__, num))

            # res = [i for i in rev if i != ]



            # rev.remove(num)
            # rev.remove(num)
    print(rev[::-1])

# TEST CASES
nums=[2,4,2,2,7,5,6,7,8,6,6,2,6,7,6]
# nums=[2,2,3,2,3,2]
# output1=[2,4,5,6,8,6]
RemoveTriplet(nums)