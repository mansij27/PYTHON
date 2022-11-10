"""LONGEST WORD IN A STRING"""
def long_String(string):
    str_list = string.split()
    list = sorted(str_list, key=len)
    print(list[-1])
string = input("Enter your string: ")

long_String(string)

# return string with length
def long_String(string):
    long_word=""
    s=string.split()
    for word in s:
        if len(word) > len(long_word):
            long_word =word

    print("The word is '{}' and the length of longest string is {}".format(long_word, len(long_word)))
long_String(string)

# with position
def long_String(string):
    pos=0
    long_word=""
    s=string.split()
    for i,word in enumerate(s):
        if len(word) > len(long_word):
            long_word =word
            pos=i

    print("The word '{}' is at the position {}".format(long_word,pos))
long_String(string)

