# reversing words in a given string
string = "geeks quiz practice code"
s = string.split()[::-1]
l = []
for i in s:
    l.append(i)
print(' '.join(l))

# EACH LETTER REVERSE
string = "Geeks Quiz pRactice codeE"
s = string[::-1]
print(s)