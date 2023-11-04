Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fact(num):
...     if(num==0 or num==1):
...         return 1
...     else:
...         f=1
...         while(num>0):
...             f=f*fact(num-1)
...         return fact
... print("enter a number")
... n=int(input())
... print("factorial of ",n," is: ",fact(n))
SyntaxError: invalid syntax
