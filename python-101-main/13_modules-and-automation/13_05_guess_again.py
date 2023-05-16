# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
import random
number = random.randint(0, 5)
maxguess = 3
counter = 1

# while counter < maxguess: 
#     guess = int(input("Guess a number between 0 and 10: "))
#     counter += 1
#     if guess != number:
#         print("try again.")
#     else:
#         print("wow!")
#         break
# if guess == maxguess:
#     print("max numbers of tries reached!")
guess = int(input("guess a number between 0 and 5: "))
while counter<maxguess and guess != number:
    guess = int(input("try again: "))
    counter += 1
if counter < maxguess and guess == number:
    print(f"WOW! You got it in {guess} try/tries!")
if counter == maxguess:
    print("game over!")



