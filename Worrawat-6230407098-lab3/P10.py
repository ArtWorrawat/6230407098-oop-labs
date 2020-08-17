sum_list = []
all_num = 0
while True:
    number = float(input("Enter an integer:"))
    if number >= 0:
        sum_list.append(number)
    else:
        break
if sum_list == []:
    print("You haven't entered a positive number")
else:
    all_num += sum(sum_list)
    print("Average is ",all_num / len(sum_list))