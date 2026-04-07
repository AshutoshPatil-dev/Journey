class vehicle:
    def base(self):
        self.brand = input("Enter the name of the brand: ")
        self.tyres = int(input("Enter the number of tyres: "))
        self.colour = input("Enter the colour of the vehicle: " )

class car(vehicle):
    def display(self):
        print(self.tyres)
        print(self.colour)
        

v1 = car()
v1.base()
v1.display()