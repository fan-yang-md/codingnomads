# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    def __init__(self, name, mass, density, planetary_system) -> None:
        self.name = name
        self.mass = mass
        self.density = density
        self.planetary_system = planetary_system
    def __str__(self) -> str:
        return f'Planet name: {self.name}\n\
mass: {self.mass} 10^24 kg\n\
density: {self.density} kg/m^3\n\
solar system: {self.planetary_system}'
    
earth = Planet('Earth', 5.97, 5514, 'the Solar System')

print(earth)
