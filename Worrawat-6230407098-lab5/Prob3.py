import math
def hypothenus(first, second):
    try:
        sum_squares = math.sqrt((first**2)+(second**2))
        return sum_squares
    except TypeError:
        return None

print("Hypothenus({}, {}) is {}".format(3.0, 4.0, hypothenus(3.0, 4.0)))
print("Hypothenus({}, {}) is {}".format("3", "4", hypothenus("4", "5")))
print("Hypothenus({}, {}) is {}".format(3, "4.0", hypothenus(3, "4.0")))