def First_Last_Same(lst):
    print('Given list is:', lst)
    FirstElement=lst[0]
    LastElement=lst[-1]

    if FirstElement==LastElement:
        return (' same')
    else:
        return ('not same')

lst=[13,64,7,3,13]
val=First_Last_Same(lst)

print('The number are', val)

