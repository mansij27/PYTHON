def replace(lst, target, swap_value):
    for idx in range(len(lst)):
        element = lst[idx]

        if element == target:
            lst[idx] = swap_value

lst= ["Mansi" ,"is" , "good", "girl"]
print(lst)
replace(lst, 'good', 'bad')
print('","'.join(lst))