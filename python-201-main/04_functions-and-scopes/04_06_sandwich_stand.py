# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich():
    bread = input('What kind of bread? ')
    toppings = input('Now choose your toppings: ')
    topping_list = toppings.split()
    sandwich = bread + '\n' + '\n'.join(topping_list) + '\n' + bread
    return sandwich

print(f'Here is your sandwich: \n{make_sandwich()}')
