#wap to find the greatest of four numbers entered by the user
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
d=int(input("enter a number"))
if(a>b and a>c and a>d):
    print("a is greater",a)
elif(b>b and b>c and b>d):
    print("b is greater",b)
elif(c>b and c>a and c>d):
    print("c is greater",c)
else:
    print("d is greater",d)
