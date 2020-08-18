number = int(input("Enter a number to find the factorial:"))
summary = 1

if number == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(number):
        summary *= i+1
    print(f"Factorial of {number} is {summary}")

