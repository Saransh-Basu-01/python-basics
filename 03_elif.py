p1="make a lot of money"
p2="make many money"
p3="click money"
p4="money money"
message=input("enter your comment")
if((p1 in message)or(p2 in message)or(p3 in message)or(p4 in message)):
    print("this is a scam")
else:
    print("this is not a scam")