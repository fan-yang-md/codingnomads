# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(list):  # add your arguments
      # add your code implementation
      element_index_list = []
      for item in list:
            tuple_ = (item, list.index(item)+1)
            element_index_list.append(tuple_)
      return element_index_list
print(my_enumerate([1, 2, 3, 4, 5, 6]))



