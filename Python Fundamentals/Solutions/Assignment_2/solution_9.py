'''
Write a function is_prime(n) that return True if n is prime number and False otherwhise, using a loop.
'''

def is_prime(n):
    for it in range(2, n):
        if (n%it == 0):
            return False
    return True

print(is_prime(5)) #True
print(is_prime(2)) #True
print(is_prime(23)) #True
print(is_prime(45)) #False
print(is_prime(7)) #True