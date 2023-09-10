def factorial(num):
    f=1
    for i in range(1,num+1):
        f = f*i
    return f
print('Enter a number:\n')
n = int(input())
print('Factorial of ',n,' is :\t',factorial(n))
