'''
Write a program that takes salary as input. Calculate the final tax rate based on below rules:
    1. if salary<30000 -> 5%
    2. if salary is 30000-70000 --> 15%
    3. if salary > 70000 --> 25%

'''

salary = int(input("Enter Salary amount: "))

rate = 0
if salary < 30000:
    rate = 5
elif (salary >= 30000 and salary < 70000):
    rate = 15
else:
    rate = 25

print("Final tax rate:", rate,"%")