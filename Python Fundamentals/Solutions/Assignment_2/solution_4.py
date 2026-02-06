'''
write a function to return count the number of digits in a number n.
'''

def digits_count(n):
    count = 0
    while(n>0):
        count += 1
        n = int(n/10)
    return count

print(digits_count(4628364))