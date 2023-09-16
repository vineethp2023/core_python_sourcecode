class vehicles:
    def getspecs(self):
        self.type = input('\n Enter the type of vehicle :')
        self.color = input('\n Enter the color of vehicle: ')
        self.price = input('\n Enter the price : ')
        self.mileage = input('\n Enter the mileage : ')
    def displayspecs(self):
        print('Type........: ',self.type)
        print('Color.......: ',self.color)
        print('Price.......: ',self.price)
        print('Mileage.....: ',self.mileage)
class car(vehicles):
    def getspecs(self):
        super().getspecs()
        self.seating = int(input('Enter the seating capacity: '))
        self.sunroof = input('is sunroof available ?')
        self.offroad = input('Offroad support needed ? (yes/no)')
    def displayspecs(self):
        super().displayspecs()
        print('Seating Capacity........: ',self.seating)
        print('Sun roof................: ',self.sunroof)
        print('Off-road availability...: ',self.offroad)
class bike(vehicles):
    def getspecs(self):
        super().getspecs()
        self.weight = int(input('Enter the weight: '))
        self.fuel = int(input('Enter the fuel capacity: '))
        self.torque = int(input('Enter the maximum torque: '))
    def displayspecs(self):
        super().displayspecs()
        print('Weight........:',self.weight)
        print('Fuel Capacity.:',self.fuel)
        print('Max. Torque...:',self.torque)

ob = bike()
print('Enter the details of bike\n')
ob.getspecs()
ob.displayspecs()
print('Enter the details of car\n')
ob = car()
ob.getspecs()
ob.displayspecs()


