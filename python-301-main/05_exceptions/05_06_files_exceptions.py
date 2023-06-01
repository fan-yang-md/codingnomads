# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?

from pathlib import Path

folder_path = Path('C:/Users/13392/Documents/codingnomads/python-301-main/05_exceptions/books')

war_ = 'war_and_peace.txt'
crime_ = 'crime_and_punishment.txt'
pride_ = 'pride_and_prejudice.txt'

with open(folder_path.joinpath(pride_), 'r', errors='ignore') as file_:
    try:
        pride_list = file_.read().split()
        print(pride_list[0])
    except Exception as e:
        print(e)

