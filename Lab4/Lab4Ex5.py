# fname = input("Enter filename: ")
fname = './myfile.txt'
try :
    f = open(fname)
    myLine = f.readline()
    while (len(myLine)>0) :
    # print generates a newline so we do not
        #      the newline from the string
        print(myLine[:-1])
        # print(myLine)
        myLine = f.readline()
    f.close()
except IOError as e :
    print("Problem opening file")