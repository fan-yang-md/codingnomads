# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

starter_list = [[1, 2, 3, 4], [5, [5, 5]], [7, 8, 9]]
flattened_list = []
for item in starter_list:
    flattened_list += item

print(flattened_list)

def flatten_list(starter_list):
    flattened_list = []
    for item in starter_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

flattened_list = flatten_list(starter_list)
print(flattened_list)