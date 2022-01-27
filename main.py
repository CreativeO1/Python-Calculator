def factorial(x):
  if x >= 0:
    result = 1

    for y in range(1, x+1):
      result = result * y
    
    return result
  else:
    return "X must be a natural number for this operation!"

def power(x, y):
  result = 1

  if y >= 0:
    for z in range(1, y+1):
      result = result * x
  elif y < 0:
    for z in range(1, y+1):
      result = result / x
  
  return result

print("Possible Operations:\nAdd (X + Y)\nSubtract (X - Y)\nMultiply (X * Y)\nDivide (X / Y)\nFactorial (X !)\nExponent (X ^ Y)")

while True:
  take = input("Calculate: ")

  if take != "":
    splits = take.split(" ")

    if len(splits) >= 3:
      number1 = int(splits[0])
      number2 = int(splits[2])

      if splits[1] == "+":
        print(number1 + number2)
      elif splits[1] == "-":
        print(number1 - number2)
      elif splits[1] == "*":
        print(number1 * number2)
      elif splits[1] == "/":
        print(number1 / number2)
      elif splits[1] == "^":
        print(power(number1, number2))
      else:
        print("Invalid operation!")
    elif len(splits) >= 2:
      if splits[0].isdecimal():
        if splits[1] == "!":
          print(factorial(int(splits[0])))
    else:
      print("Invalid input!")
  else:
    print("-_-")
