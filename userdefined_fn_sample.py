def calc_price(x,y):
    return x/y**2
x = float(eval(input('Enter the price x: \n')))
y = float(eval(input("Enter the price y:\n")))
print("x: ",x,"y: ",y)
print('Final price is: ',calc_price(x,y))
