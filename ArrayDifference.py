"""two integer array of distinct items of target value. Return index of both arrays where diff btw elements is target
value. If no element diff equal to target return [-1,-1]"""

def ArrayDiff(numsFirst,numsSecond):
    nums=[]
    i=0
    j=1
    # for i,j in enumerate(numsFirst):
    for i in range(0,len(numsFirst)):
        for j in range(len(numsSecond)):
            if numsFirst[j]-numsSecond[i]==target:
                nums.append(i,j)
            elif numsFirst[j] - numsSecond[i] < target:
                j+=1
            else:
                i+=1
            # else:
            #     print("xx")
                # return [-1,-1]
                # break
    print(nums)

#TEST CASES
numsFirst=[3,4,10]
numsSecond=[1,4,8]
target=5

ArrayDiff(numsFirst,numsSecond)

# numsFirst=[2,4,10]
# numsSecond=[1,4,8]
# target=5

