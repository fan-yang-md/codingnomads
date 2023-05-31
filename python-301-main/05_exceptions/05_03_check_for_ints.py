# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

while True:
    try:
        input_ = int(input('enter an integer: '))
    except ValueError:
        print('not a valid integer')
    else:
        print('good job.')
        break

    