"""Convert uppercase to lowercase and vice versa. Also keep count of all the cases in the string"""

string=input("Enter string: ")
count_lower = 0
count_upper = 0
newstr = ""

for i in string:
    if i.isupper():
        newstr += i.lower()
        count_lower += 1
    elif i.islower():
        newstr += i.upper()
        count_upper +=1
    else:
        newstr += " "

print("Count of upper is {} and lower is {} and new string is {}".format(count_upper, count_lower, newstr))

# ALTERNATIVE FUNCTION
print(string.swapcase())