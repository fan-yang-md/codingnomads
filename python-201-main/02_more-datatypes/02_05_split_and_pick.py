# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

string1 = input(f'enter a sentence: ')
list1 = string1.split()
list_count_dict = {}

#print(list1)

for word in list1:
    if word in list_count_dict:
        list_count_dict[word] += 1
    else:
        list_count_dict[word] = 1

print(list_count_dict)

highest_count = 1
highest_count_word = ""

for word, count in list_count_dict.items():
    if count > highest_count:
        highest_count = count
        highest_count_word = word

if highest_count == 1:
    print('no word occurs more than once')
else:
    print(highest_count_word)
