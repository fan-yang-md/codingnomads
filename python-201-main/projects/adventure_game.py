# Build a CLI RPG game following the instructions from the course.

alive = True
find_sword = None
# Ask the player for their name.
player = input('What is your name, brave solider? ')

# Display a message that greets them and introduces them to the game world.
print (f"Greetings {player}! Stay diligent, stay alive!")

# Present them with a choice between two doors.
while alive:
    door_choice = input('Choose a door. Enter 1 for left, 2 for right:')

# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.

    if door_choice == '1':
        print('This room is empty.')
        next_choice = input('Enter 1 to look around, any other key to exit: ')
        if next_choice == '1':
            find_sword = True
            print("Wow you found a sword! Let's go back!")
        else:
            find_sword = False

    elif door_choice == '2':
        print('There is a dragon in here.')
        next_choice = input('Enter 1 to fight, any other key to exit: ')
        if next_choice == '1':
            if find_sword == True:
                print('Congrats! You have beaten the game!')
                break
            else:
                try_again = input('Sorry! You were eaten by the dragon! Enter "Y" to try again or any other key to quit: ')
                if try_again.lower() != 'y':
                    print('Game Over!')
                    alive = False

    else:
        print("You only got two choices solider, and that ain't one of them!")