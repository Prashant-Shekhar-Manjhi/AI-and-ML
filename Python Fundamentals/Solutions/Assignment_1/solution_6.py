# Write a program to swap values of two numbers entered by the user

num_1 = int(input("First number: "))
num_2 = int(input("Second number: "))

print("Before swaping:", "num_1 =", num_1, "num_2 =", num_2)

x = num_1
num_1 = num_2
num_2 = x

print("After swaping:", "num_1 =", num_1, "num_2 =", num_2)