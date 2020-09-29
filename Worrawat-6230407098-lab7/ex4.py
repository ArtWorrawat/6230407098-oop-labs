class Number:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
    def display(self):
        print(self.x)
        print(self.y)

    @classmethod
    def display_factors(cls, number):
        divided1 = number // 2
        divided2 = number - divided1
        return f"Factors of {number} is {float(divided1)} and {float(divided2)}"

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

