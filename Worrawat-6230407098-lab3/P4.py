number = int(input("Enter anumber to find the factorial:"))
summary = 1

for i in range(number):
    summary *= i+1
print(f"Factorial of {number} is {summary}")
