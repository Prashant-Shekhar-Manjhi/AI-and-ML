'''
Ask the user to enter two integers and one float. Convert them all to floats 
and print their average.
'''

int_1 = int(input("Integer 1: "))
int_2 = int(input("Integer 2: "))
float_1 = float(input("Float: "))

avg = (float(int_1) + float(int_2) + float_1) / 3
print("Average value:", avg)