# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(name):
    return f'Hello {name}!'

def write_letter(name, text):
    letter = f'{greet(name.capitalize())} \n {text.capitalize()}. \n Goodbye, {name}'
    return(letter)

print(write_letter('jon', 'hope you are well'))