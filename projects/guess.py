import random
random_digit = random.randint(1, 10)
guess = None
tries = 0

while guess != random_digit and tries < 5:
    guess = int(input("Guess a number between 1 and 10: "))
    tries += 1
    if guess == random_digit:
        print("congrats!")

    elif tries == 5:
        print("Time's up!")

    else: 
        print("Try again!")
