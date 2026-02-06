'''
Ask the user for a temperature in Celsius (string input). Convert it to float, then calculate and print temperature in Fahrenheit.
FahrenheitTemp = (CelsiusTemp * (9/5)) + 32
'''

temp_in_cel = float(input("Enter Temp in celsius: "))
temp_in_Fah = (temp_in_cel * (9/5)) + 32

print("Temp in Fahrenheit:", temp_in_Fah)

