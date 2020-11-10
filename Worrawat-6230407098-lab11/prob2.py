from functools import reduce
import sys

if __name__ == '__main__':
    n = int(sys.argv[1])
    factorial = reduce(lambda x, y: x * y, range(1, n + 1))
    print(f"Factorial of ({n}) is {factorial}")