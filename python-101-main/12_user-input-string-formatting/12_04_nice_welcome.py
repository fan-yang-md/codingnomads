# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

name = input('what is your name? ')

if len(name.split()) > 1:
    print(f'Hello {name.split()[0]}!!')

else:
    print(f'hello {name}!!')