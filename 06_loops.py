n=int(input("enter a number"))
for i in range(1,11):
    print(f"the multiplication table of {n}*{i} is ",n*i)
for i in range(1,11):
    print(f"the multiplication table of {n}*{11-i} is ",n*(11-i))