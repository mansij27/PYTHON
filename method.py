class student:
    school= 'Universal'

    def __init__(self, m1, m2, m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print('This is student class')

    def get_m1(self):
        return self.m1

    def set_m2(self,value):
        self.m2= 35

s1=student(26,54,65)
s2=student(34,64,48)

print(student.get_school())
student.info()
print(s1.avg())
print(s2.avg())
print(s1.get_m1())
print(s1.set_m2)