"""
list1.py
simple list manipulation
created by sands 7/11/10
"""

myList = [1,2,3,4,5,6,7,8,9,10]

# print the list using print
print(myList)

# print the items one at a time using a while loop
i = 0
while i<len(myList) :
    print("myList["+str(i)+"] is", myList[i])
    i = i+1

print("The last two items in the list are", myList[8], "and", myList[9])

# examine some slices
print("myList[:4] is ", myList[:4])
print("myList[0:5] is ", myList[0:5])
print("myList[5:8] is ", myList[5:8])
print("myList[8:] is ", myList[8:])
myList[7] = 77
print("myList[7] = 77 is ",myList)
myList.append(23)
print("myList.append(23) is ",myList)
