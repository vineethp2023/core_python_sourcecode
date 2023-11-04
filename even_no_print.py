n = 100
x = lambda n: n if n%2 == 0 else ''

for i in range(1,101):
    if i%2 == 0:
        print(x(i))
