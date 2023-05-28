# Write a script that prints a star pyramid of flexible size
# If the `stars` variable is `5`, your code will output:
#
# *
# * *
# * * * 
# * * * *
# * * * * * 
#
# There should be five rows in total:
# 1. the 1st row will have 1 star,
# 2. the 2nd row will have 2 stars,
# 3. the 3rd row will have 3 stars,
# 4. the 4th row will have 4 stars,
# 5. the 5th row will have 5 stars
#
# Another example: if you set the `stars` variable tp `3`, 
# your code will output:
#
# *
# * *
# * * *
#
# HINT: Think of nested for loops!

n = input('gimme a number between 0 and 10: ')
m = 1
star = '*'
if n.isnumeric():
    n = int(n)
    while m <= n :
        print(star*m)
        m+=1
    
else:
    print(' :( you do not follow directions well.')