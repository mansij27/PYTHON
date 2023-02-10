"""Repeated word in a sentence"""
str=input("Enter a sentence: ")

def RepeatedWord(str):
    s=str.split()

    for i in s:
        count=1
        for j in s:
            if i==j:
                count+=1

    if(count>1):
        print(i)

RepeatedWord(str)