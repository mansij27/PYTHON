class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('the config is :', self.cpu, self.ram)

c1 = Computer('i5', '8gb')
c2 = Computer('ryzen 3', '16gb')

c1.config()
c2.config()