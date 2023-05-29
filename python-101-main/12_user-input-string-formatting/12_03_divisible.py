# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.
num = input('give me a number: ')

if num.isnumeric():
    num = int(num)
    if num%3 == 0:
        print('It is divisible by 3.')
    else:
        print('it is not divisible by 3.')

else:
    print('you do not follow rules.')