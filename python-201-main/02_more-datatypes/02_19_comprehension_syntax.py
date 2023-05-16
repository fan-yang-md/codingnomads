# Use a list comprehension to create a list that contains the individual
# letters of the word "codingnomads":
# ['c', 'o', 'd', 'i', 'n', 'g', 'n', 'o', 'm', 'a', 'd', 's']
#
# Note: You can solve this more quickly with a call to `list()`
# but try to do it using a list comprehension.

word = "codingnomads"
new_list = []
for alphab in word:
    new_list.append(alphab)

print(new_list)
