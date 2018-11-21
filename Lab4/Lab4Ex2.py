
def minmax(l):
  """
  find smallest and largest values in l
  argument: l: list of int
  returns: (smallest, largest): tuple of 2 ints
  """
  if len(l) == 0: return None
  smallest = largest = l[0]
  for n in l:  # could use n in l[1:]
      if n < smallest:
          smallest = n
      elif n > largest:
          largest = n
  return (smallest, largest)


l=[10,20,30,40]
myTuple=minmax(l)
smallest, largest=myTuple
print("smallest: ",smallest, " largest: ", largest)
