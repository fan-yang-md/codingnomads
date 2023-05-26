# CLASSES AND INHERITANCE
# =======================
# 1) Define an empty `Movie()` class.
class Movie: 

# 2) Add a dunder init method that takes two arguments `year` and `title`
    def __init__(self, year, title, director, star) -> None:
        self.year = year
        self.title = title
        self.director = director
        self.star = star

    def __str__(self) -> str:
        return f' Movie title: {self.title}\n Year: {self.year}\n Director: {self.director}\n Starring: {self.star}\n'

# 3) Create a sub-class called `RomCom()` that inherits from the `Movie()` class

class RomCom(Movie):
    pass

# 4) Create another sub-class of the `Movie()` class called `ActionMovie()`
#     that overwrites the dunder init method of `Movie()` and adds another
#     instance variable called `pg` that is set by default to the number `13`.

class ActionMovie(Movie):
    def __init__(self, year, title, director, star) -> None:
        super().__init__(year, title, director, star)
        self.pg = 'PG 13'

    def __str__(self) -> str:
        return super().__str__() + f' Rating: {self.pg}'

# 5) Practice planning out and flushing out these classes even more.
#     Take notes in your notebook. What other attributes could a `Movie()` class
#     contain? What methods? What should the child classes inherit as-is or overwrite?

rambo = ActionMovie(1982, 'Rambo: First Blood', "Ted Kotcheff", "Sylvester Stallone")
print(rambo)