# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4
string = input("give me a sentence: ")
letter = input('now give me the letter you want me to find the first occurence of: ')

for n in range(len(string)):
    if string[n] == letter:
        position = n
        break
print(f'the letter {letter} is at position: {position}')
