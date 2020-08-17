months = ("January", "February", "March", "April", "May", "June", "July"
              , "August", "September", "October", "November", "December")
dates = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
dict_items = {}
for i in range(12):
    dict_items[months[i]] = dates[i]
month_select = input("Enter month:")
print(f"Number of days in {month_select} is {dict_items[month_select]}")
