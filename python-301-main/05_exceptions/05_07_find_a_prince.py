# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

from pathlib import Path

class PrinceException(Exception):
    pass

def prince_check(book_list):
    for book in book_list:
        with open(folder_path.joinpath(book), 'r', errors='ignore') as book_:
            book_string = book_.read()
            #print(book_string[:100])
            if 'prince' in book_string[:100]:
                raise PrinceException(f'found an exceptional prince in {book}')
            else:
                print(f'no exceptional prince to be found in {book}')

folder_path = Path('C:/Users/13392/Documents/codingnomads/python-301-main/05_exceptions/books')

war_ = 'war_and_peace.txt'
crime_ = 'crime_and_punishment.txt'
pride_ = 'pride_and_prejudice.txt'

book_list = [war_, crime_, pride_]

prince_check(book_list)
