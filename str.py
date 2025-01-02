# Name=input("enter your name")
# print(f"Good afternoon,{Name}")
letter='''Dear <|name|>,
you are selected!
<|date|>'''
print(letter.replace("<|name|>","Saransh Basu").replace("<|date|>","24th september 2060"))
