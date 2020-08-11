def check(round) :
    if round == "1":
        term = "midterm"
    elif round == "2":
        term = "final"
    while True:

name = input("Please enter a student name: ")
for i in  range(2):
    score__ex = check(i)

score /= 2
if score < 50:
    print("%s has total mark as"%name, "%.2f and grade as F"%score)
elif score < 60:
    print("%s has total mark as"%name, "%.2f and grade as D"%score)
elif score < 70:
    print("%s has total mark as"%name, "%.2f and grade as C"%score)
elif score < 80:
    print("%s has total mark as"%name, "%.2f and grade as B"%score)
else:
    print("%s has total mark as"%name, "%.2f and grade as A"%score)