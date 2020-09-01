def robust_calculator(first, second, operator, forma):
    first = float(first)
    second = float(second)
    if operator == "+" or operator =="":
        ans = first + second
    elif operator == "-":
        ans = first - second
    elif operator == "*":
        ans = first * second
    elif operator == "/":
        ans = first / second
    if forma == "int":
        return round(ans)
    elif forma == "float" or forma == "":
        return float(ans)


def check_quit(value):
    if value == "q" or value == "Q":
        quit()

while True:
    while True:
        first = input("Please enter the first operand ('q' to quit):")
        check_quit(first)
        try:
            first = float(first)
            break
        except ValueError:
            print("Please enter a number")
    while True:
        second = input("Please enter the second operand :")
        check_quit(second)
        try:
            second = float(second)
            break
        except ValueError:
            print("Please enter a number")
    check_quit(second)
    operator = input("Enter an operation ('+', '-', '*', '/'):")
    if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "" :
        if operator == "":
            operator = "+"
        form =str(input("Enter output format (float int):"))
        try:
          print(f"{first} {operator} {second} = {robust_calculator(first, second, operator, form)}")
        except ZeroDivisionError:
          print("Cannot divide by zero")
          print("We cannot perform your requested calculation")

    else:
        print("Operation must be ADD, SUB, MUL, DIV")