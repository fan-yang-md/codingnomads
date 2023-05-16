# Convert a string to a tuple and print out the result.
# What do you see?
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

string = "codingnomads"
tuple1 = tuple(string)
#print(tuple1)

for x in tuple1:
    print(x)

for y in string:
    print(y)