# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
#tries = 1
points = 5 
game_set = set()

# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.

while points > 0 and len(game_set) <= 10: 
    user_input = input(f'give a number: ')
    if user_input.isdigit():
#        tries += 1
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
        if user_input in game_set:
            print("you entered this number already, dummy!")
            points -= 1
        else:
            game_set.add(user_input)

    else: 
        print("invalid input")

# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

if points == 0: 
    print("sorry you have the memory of a goldfish!")
elif len(game_set) > 10 and points > 0:
    print("congrats! you have the memory of an elephant!")



