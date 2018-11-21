def getReg(studTuple):
    return studTuple[2]

def getName(studTuple) :
    fName, sName, reg = studTuple
    return (sName, fName)

def printStudsByName(l) :
    l.sort(key = getName)
    for tup in l : print(tup[0], tup[1], tup[2])

def printStudsByName(l) :
    l = l[:]
    l.sort(key=getName)
    for tup in l : print(tup[0], tup[1], tup[2])

l=[("Sefki","Kolozali",163),("Mark","Test", 133),("Stephen","Test2", 143)]

l.sort(key=getReg)
print(l)
l.sort(key=getName)
print(l)

#
# def custom_sort(t):
#     return t[1]
#
# L = [("Alice","A", 25), ("Bob","B", 20), ("Alex","C", 5)]
# L.sort(key=custom_sort)
# print(L)
