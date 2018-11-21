
# marks=[10,20,30,40]
# total = maximum = 0.0
# size = len(marks)
#
#
# if size == 0 :
#   print("The list is empty")
# else :
#   for mark in marks:
#     total = total + mark
#     if mark > maximum : maximum = mark
#   print("The average is", round(total / size,
# 1))
#   print("The highest mark is", maximum)


# vowels = 0
# for c in myStr:
#   if c in "aeiouAEIOU": vowels = vowels + 1

#
# def minmax(l):
#   """
#   find smallest and largest values in l
#   argument: l: list of int
#   returns: (smallest, largest): tuple of 2 ints
#   """
#   if len(l) == 0: return None
#   smallest = largest = l[0]
#   for n in l:  # could use n in l[1:]
#       if n < smallest:
#           smallest = n
#       elif n > largest:
#           largest = n
#   return (smallest, largest)
#
# l=[10,20,30,40]
# myTuple=minmax(l)
# smallest, largest=myTuple
# print("smallest: ",smallest, " largest: ", largest)


# gotOne = False
# while not gotOne :
#   try :
#     age = int(input("Enter your age:"))
#     gotOne = True
#   except ValueError as e :
#     print("Invalid input – try again")

# def getInt(prompt) :
#   """
# gets integer from keyboard
# argument: prompt message: str
# returns: input value: int
# """
#   gotOne = False
#   while not gotOne :
#     try :
#       num = int(input(prompt + ": "))
#       gotOne = True
#     except ValueError as e :
#       prompt = "Invalid input – try again"
#   return num
# # sample call: age = getInt("Enter your age")
#
# getInt("Enter your age ")