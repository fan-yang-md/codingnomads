# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

from pathlib import Path

filepath = Path('/Users/13392/documents/codingnomads/python-201-main/03_file-input-output')

with open(filepath.joinpath('words.txt'),'r') as file_out:
    for word in file_out.read().split(): #QUESTION: why is split() needed here?!
        print(word)
        if len(word) > 20:
            print(word)