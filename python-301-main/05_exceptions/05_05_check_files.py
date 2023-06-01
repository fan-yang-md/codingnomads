# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

from pathlib import Path

file_name = 'integers.txt'
filepath = Path('C:/Users/13392/Documents/codingnomads/python-301-main/05_exceptions')

with open(filepath.joinpath(file_name), 'r') as file_:
    integer_list = list(file_.read().split())
    #print(integer_list)

print(f' \nHere is list of numbers in the file: {integer_list}')

print(' \nwe are dividing all the numbers by all the numbers in the list: \n ')

for num in integer_list:
    for divisor in integer_list:
        try: 
            print(f'{num}/{divisor} = {int(num)/int(divisor)}')
        except IOError as i:
            print(i)
        except ZeroDivisionError:
            print(f'{num}/{divisor}: Cannot divide by zero')
        except ValueError:
            print(f'{num}/{divisor}: non-numerical values.')



