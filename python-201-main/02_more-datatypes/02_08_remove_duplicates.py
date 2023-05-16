# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]
set_ = set(list_)
print(set_)

list2 = []
for item in list_:
    if item not in list2:
        list2.append(item)
print(list2)