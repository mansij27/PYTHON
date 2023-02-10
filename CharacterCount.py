"""Returns the frequency of each character in string"""
from collections import Counter
str="hello world"

def CharCount(str):
    count = {}
    # print(type(count))

    for i in str:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    print(count)

    # METHOD 2
    res= Counter(str)
    print(res)

    # METHOD 3
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    print(dict)

CharCount(str)