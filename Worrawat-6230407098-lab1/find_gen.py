from datetime import date
import  math

Today = date.today()
Date = int(Today.strftime("%d"))
Month = int(Today.strftime("%m"))
Year = int(Today.strftime("%Y"))
Name = input("Enter your name :")
B_Day, B_Month, B_Year = input("please input your birthday :").split()
B_Day = int(B_Day)
B_Month = int(B_Month)
B_Year = int(B_Year)
Live_Day = math.sqrt((Date-B_Day)**2)+math.sqrt(((Month-B_Month)*30)**2)+((Year-B_Year)*365)
Live_Year = int(Live_Day/365)

print("Your name is ",Name)
print("You lived %d years"%Live_Year)
if Live_Year >= 73 :
    print("You are generation Builder")
elif Live_Year >= 55 :
    print("You are generation Baby Boomer")
elif Live_Year >= 40 :
    print("You are generation X")
elif Live_Year >= 25 :
    print("You are generation Y")
elif Live_Year >= 10 :
    print("You are generation Z")
else:
    print("You are generation Alpha")
