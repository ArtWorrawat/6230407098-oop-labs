def check(round):
    if round == 0:
        while True:
            value = input("Please enter the student's midterm exam mark (0-100):")
            try:
                value = float(value)
                if 100 >= value >= 0:
                    return value
                else:
                    print("Please enter a valid exam mark (0-100)")
            except:
                print("Please enter a valid exam mark (0-100)")
    elif round == 1:
        while True:
            value = input("Please enter the student's final exam mark (0-100):")
            try:
                value = float(value)
                if 100 >= value >= 0:
                    return value
                else:
                    print("Please enter a valid exam mark (0-100)")
            except:
                print("Please enter a valid exam mark (0-100)")


score = 0
name = input("Please enter a student name: ")
for i in range(2):
    score__ex = check(i)
    score += score__ex
score /= 2
if score < 50:
    print("%s has total mark as" % name, "%.2f and grade as F" % score)
elif score < 60:
    print("%s has total mark as" % name, "%.2f and grade as D" % score)
elif score < 70:
    print("%s has total mark as" % name, "%.2f and grade as C" % score)
elif score < 80:
    print("%s has total mark as" % name, "%.2f and grade as B" % score)
else:
    print("%s has total mark as" % name, "%.2f and grade as A" % score)
