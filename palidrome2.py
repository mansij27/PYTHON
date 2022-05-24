def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word(len(word)-1-i)
    return x

word = input('Give me a word')
x = reverse(word)

if x == word:
    print('Word is palidrome')
else:
    print('Word is not palidrome')