# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

from pathlib import Path

filepath = Path('/Users/13392/documents/codingnomads/python-201-main/03_file-input-output')

with open(filepath.joinpath('words.txt'),'r') as file_out:
    new_list = list(file_out.read().split())
    new_list.reverse()

#print(new_list[0:10])

with open(filepath.joinpath('words in reverse.txt'), 'w') as file_reverse:
    for word in new_list:
        file_reverse.write(word + '\n')