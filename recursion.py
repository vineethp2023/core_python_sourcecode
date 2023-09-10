def fact(x):
    if x == 1:
        return 1
    else:
        return x*fact(x-1)
print('Enter a number: ')
n = eval(input())
print('Factorial of number ',n, 'is: ',fact(n))