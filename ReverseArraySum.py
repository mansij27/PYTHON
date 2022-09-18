"""Increment array by its reverse and return result in array of digits"""

# TEST CASES
numsFirst=[2,4,7,2]
# numsFirst=[1,2,3]

s="".join(map(str,numsFirst)) #joining as string
sum=str(int(s)+int(s[::-1])) #adding array with its reverse
list=[x for x in sum] #returning them as digits
print(list)