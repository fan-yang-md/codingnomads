# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car:
    def __init__(self, model, year, max_speed) -> None:
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def increase_max_speed(self):
        self.max_speed += 5

    def __str__(self) -> str:
        return f' model: {self.model}\n year: {self.year}\n max speed: {self.max_speed} mph'
    
mustang = Car('Ford Mustang', 1972, 120)

print(f'OG:\n{mustang}')

mustang.increase_max_speed()
mustang.increase_max_speed()

print(f'Boosted:\n{mustang}')
