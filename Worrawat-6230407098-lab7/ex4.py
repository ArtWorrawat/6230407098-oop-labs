class Number:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def display_factors(cls, number):
        if number % 2 == 0:
            divided = number / 2
            return f"Factors of {number} is {float(divided)} and {float(divided)}"
        else:
            divided = int(number / 2)
            return f"Factors of {number} is {float(divided)} and {float(divided + 1)}"

    @staticmethod
    def is_valid_divisor(number):
        if number == 0:
            return f"{number} is not a valid divisor"
        else:
            return f"{number} is a valid divisor"


if __name__ == '__main__':
    print(f"3 + 5 is {Number(3, 5).add()}")
    print(Number.display_factors(6))
    print(Number.display_factors(8))
    print(Number.is_valid_divisor(2))
    print(Number.is_valid_divisor(0))
