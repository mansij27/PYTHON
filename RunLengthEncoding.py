"""Return the count of each alphabet in string, aa=2a"""
# NOT COMPLETE
from collections import Counter
strParam = input("Enter string: ")

def Encoding(strParam):
    # count=0
    list=[]
    a=Counter(strParam)
    print(Counter(strParam))
    for i in a:
        if a[i] == 1:
            list.append(i)
        else:
            list.append(a[i])
            list.append(i)
    print(list)

    ch=str(list)
    print(''.join(ch))
    print(type(ch))

    # encoded_str=""
    # i=0
    # # token=['f', 'q', 'z', 'j', 'a', 5,2,6,9]
    # token='fqzja5269'
    # final=[]
    # while(i<=len(strParam)-1):
    #     count=1
    #     ch=strParam[i]
    #     j=i
    #     while(j<len(strParam)-1):
    #         if (strParam[j]==strParam[j+1]):
    #             count+=1
    #             j+=1
    #         else:
    #             break
    #     encoded_str+=str(count)+ch
    #     i=j+1
    # # return encoded_str
    #
    # for x in encoded_str:
    #     if str(token) in str(encoded_str):
    #         final.append(x)
    # # print(final)
    # return final

print(Encoding(strParam))