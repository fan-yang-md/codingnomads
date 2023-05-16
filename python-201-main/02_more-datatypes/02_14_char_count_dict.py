# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

user_input = input(f'say something silly or serious: ')
new_dict = {}
#print(user_input)

for char in user_input:
    if char != " ":
        new_dict[char] = user_input.count(char)

print(new_dict)