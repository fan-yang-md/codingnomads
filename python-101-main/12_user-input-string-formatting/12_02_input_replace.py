# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

string = input("give me a sentence: ")
symbol = input("now give me the symbol: ")

list_ = string.split()
new_string = ''

for item in list_:
    new_item = item.replace(item[0], symbol)
    new_string += new_item + " "

new_string.rstrip()

print(new_string)