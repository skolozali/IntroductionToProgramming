
f2 = open("myfile2.txt", 'w')
f3 = open("file2.txt", 'a')

myAge=12
myList=[20,30,40]
print("Age:", myAge, file=f2)
for i in myList : print(i, file = f3)
