# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]
user_input = input(f'give me a sentence: ')
list1 = user_input.split()

#print(list1)

list1 = [tuple(word) for word in list1]

print(list1)