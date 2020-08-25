while True:
    try:
        first = int(input("Please enter the first operand:"))
        break
    except ValueError:
        print("Please enter a number")
while True:
    try:
        second = int(input("Please enter the second operand:"))
        break
    except ValueError:
        print("Please enter a number")
while True:
    operator = input("Please enter an operator")
    if operator == "+":
        ans = first + second
        break
    elif operator == "-":
        ans = first - second
        break
    elif operator == "*":
        ans = first * second
        break
    elif operator == "/":
        try:
            ans = first / second
            break
        except ZeroDivisionError:
            print("Cannot divide by zero")
    else:
        print("Unknown operator")

print(f"Result of {first} {operator} {second} is {ans}")
