def rotateWord(str,k):
    #splitting the string
    strRotate = str.split()
    #loop for number of rotation
    for i in range(0,k):
     #loop for number of words
     for j in range(0, len(strRotate)):
        #shifting 1 character from left to right
        strRotate[j] = strRotate[j][1:] + strRotate[j][0]
    #initializing counter
    count = 0
    #loop for getting rotating words
    for k in range(0, len(strRotate)):
        #checking rotating words in original string
        if strRotate[k] in str:
            #incrementing counter
            count+=1
    print(count)

rotateWord("Hello Friend", 3)
rotateWord("Hello dFrien", 5)

