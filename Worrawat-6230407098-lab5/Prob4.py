def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        number = (number*(factorial(number - 1)))
        return number

try:
  number = int(input("Enter an integer:"))
  print(f"factorial({number}) is {factorial(number)}")
  if number < 0:
      raise Exception("Factorial cannot be less than 0")
except ValueError:
    print("Please enter a positive integer. Invalid literal for int() with base 10: \'a\'")
except Exception as err:
        print(err)