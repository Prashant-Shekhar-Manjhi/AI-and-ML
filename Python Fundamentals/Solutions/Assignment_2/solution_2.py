'''
Write a function that takes 2 integers and prints all even numbers between them(inclusive).
'''

def even_numbers(a, b):
    for it in range(a, b+1):
        if it%2==0:
            print(it)

even_numbers(3, 21)