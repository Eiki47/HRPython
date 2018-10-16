def usingList(fname, lname):
    templist = []
    for letter in fname.lower():
        if letter in lname.lower() and letter not in templist:
            templist.append(letter.lower())
    templist.sort()
    return templist

def usingSet(fname, lname):
    first = set(fname.lower())
    last = set(lname.lower())
    return sorted(first & last)

fname, lname  = input("Enter name: ").split(' ')
print(usingList(fname, lname))
print(usingSet(fname, lname))
