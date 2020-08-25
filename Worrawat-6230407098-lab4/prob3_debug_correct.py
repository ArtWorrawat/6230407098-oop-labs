import sys
import pdb


def divide(dividend, divisor):
    return dividend / divisor


def check_nega(value):
    if value < 0 :
        quit()
    else:
        return


while True:
    while True:
        try:
            dividend = int(input("Please enter the dividend:"))
            check_nega(dividend)
            break
        except ValueError:
            print("NUMBER!!!")
    while True:
        try:
            divisor = int(input("Please enter the divisor:"))
            check_nega(divisor)
            if divisor == 0:
                print("Cannot perform division by zero")
            else:
                break
        except ValueError:
            print("NUMBER!!!")

    answer = divide(dividend, divisor)
    print('The answer is: {}'.format(answer))
