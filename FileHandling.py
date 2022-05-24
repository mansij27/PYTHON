f = open('MyData.py', "r")

print(f.read())

f = open('MyData.py', "a")
f.write('Mansi is 20 years old')

for data in f:
    f.read(data)
