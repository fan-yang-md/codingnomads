unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6), ('fourth_element', 1)]
sorted_list = [unsorted_list[0]]

temp_list = []

for tuple_ in unsorted_list:
    if tuple_[1] > sorted_list[0][1]:
        sorted_list.append(tuple_)
    elif tuple_[1] < sorted_list[0][1]:
        temp_list.append(tuple_)

#print(sorted_list)
#print(temp_list)

for item in temp_list:
    if item[1] < sorted_list[0][1]:
        sorted_list.insert(0, item)

print(sorted_list)