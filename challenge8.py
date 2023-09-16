def firstdiscount(num):
    num = num-(num*(10/100))
    return num
def seconddiscount(num):
    num = num-(num*(5/100))
    return num

print('Enter the price of your product: \n')
price = int(input())
print('\nAfter calculating discount, final price is: ',seconddiscount(firstdiscount(price)))

