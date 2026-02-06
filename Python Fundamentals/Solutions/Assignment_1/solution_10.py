'''
Take a decimal number as input and output its: 
    1. integer part
    2. fractional part
'''

dec_num = float(input("Enter a decimal number: "))
int_part = int(dec_num)
frac_part = dec_num - int_part
print("Integer part: ", int_part)

# The built-in round() function allows you to round a number to a specified number of decimals. 
# This returns a number (either int or float), not a string. 
print("Fractional part: ", round(frac_part, 2))