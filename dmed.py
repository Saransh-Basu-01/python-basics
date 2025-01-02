marks={
    "harry":100,
    "subham":56,
    "rohan":23,
    0:"harry"
}
# print(marks.items())#it gives the list of all the items
# print(marks.keys())#it give keys
# print(marks.values())#it gives values
# marks.update({"harry":99})#it is mutable so original dictionary is changed,it updates the value of dictionary
# print(marks.values())
print(marks.get("harry2"))#returns none
print(marks["harry2"])#returns error
