a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
def greatest(a,b,c):
    if(a>b and a>c):
        print("a is greater",a)
    elif(b>a and b>c):
        print("b is greater",b)
    else:
        print("c is greater",c)
greatest(a,b,c)
