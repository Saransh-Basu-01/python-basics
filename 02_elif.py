eng=int(input("enter marks"))
math=int(input("enter marks"))
phy=int(input("enter marks"))
total_percentage=((eng+math+phy)*100)/300
if(total_percentage>=40 and eng>=33 and math>=33 and phy>=33):
    print("yor are pass",total_percentage)
else:
    print("you are fail",total_percentage)