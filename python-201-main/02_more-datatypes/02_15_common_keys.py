# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

new_dict = {}

#dict_1.update(dict_2)
#print(dict_1)

for key in dict_1:
    if key in dict_2:
        new_dict[key] = dict_1[key] + dict_2[key]
    else:
        new_dict[key] = dict_1[key]

for key in dict_2:
    if key not in new_dict:
        new_dict[key] = dict_2[key]
        
print(new_dict)

    

