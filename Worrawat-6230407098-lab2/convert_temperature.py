while True:
    t_f = input("Enter a temperature in Fahrenheit: ")
    try:
        t_f = float(t_f)
        break
    except:
        print("Please enter a valid floating point for the temperature")
t_c = (5 * (t_f - 32)) / 9
print("Temperature %.2f in Fahrenheit is" %t_f, "%.2f in Celcius"%t_c)
