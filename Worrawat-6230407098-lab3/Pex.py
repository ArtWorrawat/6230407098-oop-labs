def check_quit(word):
    if word == "quit":
        exit()

def calculator(first, second, op):
    first = float(first)
    second = float(second)
    if op == "+":
        print(f"{first} + {second} = ",first + second)
    if op == "-":
        print(f"{first} - {second} = ",first - second)
    if op == "*":
        print(f"{first} * {second} = ",first * second)
    if op == "/":
        if second == 0:
            print("Cannot divide a number by 0")
        else:
            print(f"{first} / {second} = ", first / second)
while True:
    first_num = input("Enter the first number:")
    check_quit(first_num)
    second_num = input("Enter the second number:")
    check_quit(second_num)
    while True:
        operator = str(input("Enter operator:"))
        check_quit(operator)
        if operator == "+" or operator == "-" or operator == "*" or operator == "/":
            calculator(first_num, second_num, operator)
            break
        else:
            print("Unknown operator")
            break
