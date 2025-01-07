f=open("poem.txt")
poem=f.read()
if("twinkle" in poem):
    print("twinkle is present in the poem")
else:
    print("twinkle isnot present in the content")
f.close()
