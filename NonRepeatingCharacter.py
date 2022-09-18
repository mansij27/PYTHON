"""Finding all the non repeating characters ina string"""
"""Finding second non repeating character"""

# METHOD 1
def NonRepeat(str):

    str=input("Enter a string")
    list=[]

    for i in str:
        count = 0
        for j in str:
            if i==j: #repeating condition
                count+=1
            if count>1:
                break
        # if count is 1 means non repeating so append in list
        if (count==1):
            list.append(i)
            # from list fetching index that is 1 means second non repeating character
            if (list.index(i))==1:
                print(i)

    print(list) #all non repeating chars

NonRepeat(str)




# METHOD 2
from collections import Counter

def repeatFunc(myStr):

	freq = Counter(myStr)

	for i in myStr:
	    if(freq[i] == 1):
		    print("method 2 op",i)
		    break

myStr = "mansii"

repeatFunc(myStr)