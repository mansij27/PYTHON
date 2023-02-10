from collections import Counter

string="geeks for geeks"
x=Counter(string)
y=max(x, key=x.get)
print(str(y))