'''
    design a program to continuously input a number n from user & 
    print if is positive or negative until the user enters "Quit".
'''

while True:
    x = input("Enter: ")
    if(x=="Quit"):
        break
    
    num = int(x)
    print("Positive" if num>=0 else "Negative")