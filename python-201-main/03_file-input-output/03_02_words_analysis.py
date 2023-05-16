# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.
import time

from pathlib import Path

filepath = Path('/Users/13392/documents/codingnomads/python-201-main/03_file-input-output')

with open(filepath.joinpath('words.txt'), 'r') as file_out:
    new_list = list(file_out.read().split())

#print(new_list[0:10])

#option 1 for printing shortest words
start = time.time()
shortest_words = []
shortest_words.append(new_list[0])

for word in new_list:
    if len(word) < len(shortest_words[0]):
        shortest_words = []
        shortest_words.append(word)
        print(word)
    elif len(word) == len(shortest_words[0]):
        shortest_words.append(word)
        print(word)

end = time.time()
print((end-start)*10**3)

#option 2 for printing shorest words

start = time.time()
shortest_word_len = len(min(new_list, key=len))

for item in new_list:
    if len(item) <= shortest_word_len:
        print(item)

#printing longest words
longest_word_len = len(max(new_list, key=len))

for item in new_list:
    if len(item) >= longest_word_len:
        print(item)

end = time.time()
print((end-start)*10**3)

#word count
word_count = len(new_list)
print(f'this file contains {word_count} words')