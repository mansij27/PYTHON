class cars:
    wheels=4

    def __init__(self):
        self.com='BMW'
        self.mil= 10

c1=cars()
c2=cars()

c1.mil=20

c1.wheels=6

print("Company is:", c1.com, " Wheels:",c1.wheels, " Mileage: ", c1.mil)
print("Company is:", c2.com, " Wheels:",c2.wheels, " Mileage: ", c2.mil)