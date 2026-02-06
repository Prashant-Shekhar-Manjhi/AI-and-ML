'''
write a function that prints the digits of a number, n.
    ex: n=312, print 3, 1, 2.
'''

def digits(n):
    while(n>0):
        print(n%10)
        n = int(n/10)

digits(1987)

