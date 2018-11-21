
marks=[10,20,30,40]
total = maximum = 0.0

size = len(marks)


if size == 0 :
  print("The list is empty")
else :
  for mark in marks:
    total = total + mark
    if mark > maximum : maximum = mark
  print("The average is", round(total / size,1))
  print("The highest mark is", maximum)