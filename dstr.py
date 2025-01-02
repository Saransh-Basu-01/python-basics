#check double space in the string
name="saransh is a  good boy"
print(name)
print(name.find("  "))
print(name.replace("  "," "))#new string ,string is immutable which means that you cannot change them ny running functioin on them
print(name.find("  "))