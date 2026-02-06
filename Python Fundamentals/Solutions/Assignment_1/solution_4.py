'''
The user enters a string containing a number. Convert it to
    1. an integer
    2. a float
    3. a string again
print all values with their type
'''

string = input("Enter a number: ")
integer = int(string)
float_value = float(integer)
string_value = str(float_value)

print(integer, type(integer))
print(float_value, type(float_value))
print(string_value, type(string_value))