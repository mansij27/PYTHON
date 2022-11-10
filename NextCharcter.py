"""Change every character with its next character of the given input"""

def NextCharacter(word):
    new_word=''
    for c in word:
        asci= ord(c)
        if asci ==ord('z'):
            new_word= new_word+'a'
        elif asci==ord('Z'):
            new_word=new_word+'A'
        else:
            new_word= new_word +chr(asci+1)
    print(new_word)
    
word = input("Enter a string")
NextCharacter(word)