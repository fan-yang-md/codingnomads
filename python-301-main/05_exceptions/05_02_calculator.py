# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.
while True:
    coms = input('enter q to quit or any other key to continue: ')
    if coms == "q":
        break
    else:
        try:
            divider = int(input('what is the divider: '))
            divisor = int(input('what is the divisor: '))
            print(divider/divisor)

        except ValueError:
            print('Input numbers onlys.')

        except ZeroDivisionError:
            print('not divisible by zero.')




