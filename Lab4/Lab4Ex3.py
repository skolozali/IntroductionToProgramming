
gotOne = False
while not gotOne :
  try :
    age = int(input("Enter your age:"))
    gotOne = True
  except ValueError as e :
    print("Invalid input – try again")