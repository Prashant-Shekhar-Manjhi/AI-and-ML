'''
Ask for principal, rate, time. convert them into float and compute simple interest.
    SI = (P*R*T)/100
'''

p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))

SI = (p * r * t)/100
print("Simple Interest:", SI)