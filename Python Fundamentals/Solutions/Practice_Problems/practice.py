# Practice Problem (Set 1)
# For a given number n, print if it's a multiple of 5 or not.
'''
n = int(input("Enter a number: "))

if (n%5 == 0):
    print(n, "is a multiple of 5!")
else:
    print(n, "is not a multiple of 5!")
'''

# For a given number n, print if it's a odd or Even.
'''
n = int(input("Enter a number: "))

if (n%2 == 0):
    print(n, "is a Even number!")
else: 
    print(n, "is an Odd number!")
'''

# Practice Problem (Set 2)
# Print multiplication table for any number n. [using while loop]

'''
n = int(input("Enter a Number: "))

i=1
while (i<=10):
    print(n*i)
    i += 1
'''

# Print odd numbers from 1 to 10, using continue. [use while loop]

'''
i = 1
while(i<=10):
    if(i%2 == 0):
        i+=1
        continue
    print(i)
    i+=1
'''

# Count vowels in a words. [using for]

'''
word = input("Enter a word: ")

count=0
for c in word:
    if (c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
        count += 1

print(count)
'''

# Sum of first n natural numbers. [using for]

'''
n = int(input("Enter a Number: "))

ans = 0
for i in range(1, n+1):
    ans += i

print(ans)
'''

# Practice Problem (Set 2)
# Create a funtion to compute factorial of a number n.

'''
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

n = int(input("Enter a Number: "))
print(factorial(n))
'''

# Create a funtion to return largest of three numbers - a, b, and c.

'''
def max_of_three(a, b, c):
    max = a if a>b else b
    max = max if max>c else c
    return max

print(max_of_three(4, 8, 2))
'''
