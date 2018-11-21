# # fname = input("Enter filename: ")
# fname = './myfile.txt'
# try :
#     f = open(fname)
#     myLine = f.readline()
#     while (len(myLine)>0) :
#     # print generates a newline so we do not
#         #      the newline from the string
#         print(myLine[:-1])
#         # print(myLine)
#         myLine = f.readline()
#     f.close()
# except IOError as e :
#     print("Problem opening file")

# myString= "Test"
f2 = open("myfile2.txt", 'w')
f3 = open("file2.txt", 'a')
# f2.write("Hello")
# f3.write(myString)

# myList=[20,30,40]
# # myList=[f2,f3]
# print("Age:", file = f2)
# for i in myList : print(i, file = f3)




















f2 = open("myfile2.txt", 'w')
f3 = open("file2.txt", 'a')
print("Age:", file = f2)
myList=[1,2,3,4,5]
for i in myList:
    print(i, file=f3)