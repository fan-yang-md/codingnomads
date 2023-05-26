# number guessing game
import random
age = random.randint(1,100)
attempts = 10

guess = input(f"You have {attempts} attempts to guess my age: ")
while True:
    if guess.isnumeric():
        guess = int(guess)
        break
    else:
        guess = input(f'Enter a number: ')

while attempts > 0:
    if guess == age:
        print('GOOD JOB! YOU GOT IT RIGHT!')
        exit()
    else:
        attempts -= 1
        if guess > age: 
            guess = int(input(f'Nope, guess again! Yikes, I am no t as old as you think! You have {attempts} attempts left: '))
        else:
            guess = int(input(f'Nope, guess again! That is flattering but I am not that young anymore...\
You have {attempts} attempts left: ' ))
