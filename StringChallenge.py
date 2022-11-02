"""Replace every letter in the string with its following alphabet and capitalize the vowels in the new string"""

def LetterChanges(str):
    result=""
    for x in str:
        if x=="z":
            newChar="a"
        elif x=="Z":
            newChar="A"
        elif x.isalpha():
            newChar=chr(ord(x)+1)
        else:
            newChar=x

        if newChar in "aeiou":
            newChar=newChar.upper()
        result+=newChar
    return result

str=input("Enter string")
print(LetterChanges(str))

# TEST CASES INPUT
# fun times!
# hello*3