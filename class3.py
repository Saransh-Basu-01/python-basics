class demo:
    a=4
o=demo()
print(o.a)#prints the class attribute because instnace attribute is not present
o.a=0#instance attributes is set
print(o.a)#prints the instnace attribute because instnace attribute is present
print(demo.a)#prints the call attribute
