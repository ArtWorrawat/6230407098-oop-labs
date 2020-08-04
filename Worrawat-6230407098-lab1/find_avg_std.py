import random
import math
First_Num = random.randint(1,10)
Second_Num = random.randint(1,10)
Avg = (First_Num + Second_Num) / 2
Std = math.sqrt(((First_Num - Avg)**2)+((First_Num - Avg)**2) / 2)
print("The first number is :",First_Num)
print("The second number is :",Second_Num)
print("Average : ",Avg)
print("Standard deviation :",Std)