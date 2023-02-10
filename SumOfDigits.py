nums=int(input("Enter the digit: "))
sum=0

while(nums>0):
    sum+=nums%10
    nums=nums//10

print(sum)

