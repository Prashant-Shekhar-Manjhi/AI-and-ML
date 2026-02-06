'''
    write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.
'''

for it in range(1, 100+1):
    if(it%3==0 and it%5==0):
        print(it)
