# The following function definition has a whole lot of bugs in it!
# Run the script and follow Python's error hints to fix them all.
# After your fixes, the function should allow you to take a name as an input
# and return a greeting message that you can save to a variable.

def say_hello(name):
        return str(f'Hello {name}!')

greeting = say_hello(input('what is your name? '))

print(greeting)

""" 
def greet(greeting="Hi", name="User"):  # Adding defaults
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

print(greet())
print(greet(name="Fievel", greeting="Hello"))
 """