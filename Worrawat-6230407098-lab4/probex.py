numbers = input("Enter the list of numbers (delimited by a comma):").split(",")
print(numbers)
try:
    point = int(input("Enter an index:"))
    print(numbers[point])
except IndexError:
    print("The list has no element at index",point)