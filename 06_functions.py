#write a pyhtin function to remove a given word from a list ad strip it at the same time
def remove(l, word):
    n = []
    for item in l:
        if word not in item:  # Skip items containing the word
            n.append(item.strip())  # Strip whitespace around the item
        else:
            n.append(item.replace(word, "").strip())  # Remove the word and strip whitespace
    return n
l = ["harry", "anshu", "rohan", "saransh"]
print(remove(l, "an"))
