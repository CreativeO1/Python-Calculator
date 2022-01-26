def factorial(x):
  if x >= 0:
    result = 1

    for y in range(1, x+1):
      result = result * y
    
    return result
  else:
    return "X must be a natural number for this operation!"

print("Possible Operations:\nAdd (X + Y)\nSubtract (X - Y)\nMultiply (X * Y)\nDivide (X / Y)\nFactorial (X !)")

while True:
  take = input("Calculate: ")

  if take != "":
    splits = take.split(" ")

    if len(splits) >= 3:
      if splits[0].isdecimal() and splits[2].isdecimal():
        if splits[1] == "+":
          print(int(splits[0]) + int(splits[2]))
        elif splits[1] == "-":
          print(int(splits[0]) - int(splits[2]))
        elif splits[1] == "*":
          print(int(splits[0]) * int(splits[2]))
        elif splits[1] == "/":
          print(int(splits[0]) / int(splits[2]))
        else:
          print("Invalid operation!")
      else:
        print("Invalid number!")
    elif len(splits) >= 2:
      if splits[0].isdecimal():
        if splits[1] == "!":
          print(factorial(int(splits[0])))
    else:
      print("Invalid input!")
  else:
    print("-_-")
