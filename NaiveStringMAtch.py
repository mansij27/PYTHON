def search(pat,txt):
    m=len(pat)
    n=len(txt)

    for i in range(n-m+1):
        j=0
        while (j<m):
            if (txt[i+j] != pat[j]):
                break
            j+=1
            if(j==m):
                print("Pattern found at index", i)

if __name__ == '__main__':
    txt=input("Enter a string")
    pat=input("Enter pattern to search in string")

    search(pat,txt)
