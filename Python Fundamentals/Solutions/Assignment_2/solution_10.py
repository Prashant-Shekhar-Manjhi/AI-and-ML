'''
Let's create a "Number Guessing Game". Given A secret number, write a program that asks the user to guess it and prints:
    1. "Too high" if the guess is above the number.
    2. "Too low" if the guess is below.
    3. "Correct! if the guess matches

'''

def guess_the_number(secret):
    attempt = 1
    while(attempt <= 3):
        x = int(input("Guess the Nuumber: "))
        if(x>secret):
            print("Too high")
        elif(x<secret):
            print("Too low")
        else:
            print("Correct!")
            return
        attempt += 1
        
guess_the_number(10)