def getInt(prompt) :
  """
gets integer from keyboard
argument: prompt message: str
returns: input value: int
"""
  gotOne = False
  while not gotOne :
    try :
      num = int(input(prompt + ": "))
      gotOne = True
    except ValueError as e :
      prompt = "Invalid input – try again"
  return num
# sample call: age = getInt("Enter your age")

getInt("Enter your age: ")