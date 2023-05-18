# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(list):  # add your arguments
      # add your code implementation
      for index, item in enumerate(list, start=1): #start index at '1' instead of the default '0'
            return(index, item)


