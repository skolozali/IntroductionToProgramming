from sys import stdout
fname = input("Enter filename: ")
try :
    f = open(fname, 'w')

except IOError as e :
    print("Problem opening file")
    print("Using standard output instead")
    f = stdout

myList=[1,2,3,4,5, 8,9]
for i in myList :
    print(i, file = f)
if f!=stdout :
    f.close()