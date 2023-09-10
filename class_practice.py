class vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def get_details():
        name = input('Enter the name of the vehicle: ')
        price = int(input('Enter the price: '))
    def put_details(self):
        print('NAME: ',self.name)
        print('PRICE: ',self.price)
obj = vehicle('',890)
print('Details of the vehicle are\n')
obj.put_details()
obj1 = vehicle()
obj1.put_details()
