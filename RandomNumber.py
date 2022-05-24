import random

numList = []
list_length = random.randint(5,15)

while len(numList) < list_length:
    numList.append(random.randint(1,75))

evenlist = [number for number in numList if number % 2 == 0]

print(numList)
print(evenlist)