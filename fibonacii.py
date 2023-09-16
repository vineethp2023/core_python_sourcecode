def fib(num):
    f = 0
    s = 1
    t = f+s
    while t <= num:
        t = f + s
        f = s
        s = t
        print(t,"\t")

print('\n Enter the number of terms: ')
n = int(input())
while n < 0:
    print('Please enter a non-zero number')
    n = int(input())
print('\n Fibonacii series upto ',n,' is:\n')
if n == 1:
     print(0,'\t',1)
if n == 0:
     print(0)
else:
    fib(n)


