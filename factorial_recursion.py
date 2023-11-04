def fact(n):
    x=1
    while(n!=0):
        x=n*fact(n-1);
    return x;

print("enter a number: ")
y=input()
if(y==0 or y==1):
    print("factorial of ",y," is 1")
else:
    print("factorial of ",y," is ",fact(y))
    
    
