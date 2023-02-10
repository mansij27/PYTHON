class Student():

    def __init__(self, name, roll_no):
        self.name= name
        self.roll_no= roll_no
        self.lap= self.Laptop()

    def show(self):
        print(self.name, self.roll_no)

    class Laptop():
        def __init__(self):
            self.brand= 'HP'
            self.cpu= 'i5'
            self.ram= 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1= Student('Mansi', 20)
s1.show()
lap1 = Student.Laptop()
lap1.show()
