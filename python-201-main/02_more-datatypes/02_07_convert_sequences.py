# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"
tuple1 = tuple(string)
print(tuple1)
list1 = list(tuple1)
print(list1)
list1 = ['k' if item == 'c' else item for item in list1]
print(list1)
tuple1 = tuple(list1)
print(tuple1)