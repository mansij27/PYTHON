# REMOVE DUPLICATE FROM STRING
from collections import Counter
string="mansi is mansi good girl school school"
s=Counter(string.split())
print(s)
x=[]
for i in s:
    if s[i]>1:
        x.append(i)
print(' '.join(x))