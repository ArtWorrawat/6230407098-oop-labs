import sys
import pdb

pdb.set_trace()
def divide(dividend, divisor):
    return dividend / divisor

while True:
    dividend = int(input("Please enter the dividend:"))
    divisor = int(input("Please enter the divisor:"))
    if dividend < 0 or divisor < 0:
        break
    answer = divide(dividend, divisor)
    print('The answer is: {}'.format(answer))