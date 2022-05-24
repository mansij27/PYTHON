class computer():

    def __init__(self):
        self.name= 'Mansi'
        self.age= 20

    def update(self):
        self.age=40

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1=computer()
c2= computer()
c1.update()

if c1.compare(c2):
    print('Same')
else:
    print('Not same')

print(c1.name, c1.age)
print(c2.name, c2.age)
