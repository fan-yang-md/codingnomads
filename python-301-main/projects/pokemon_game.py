# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `earth`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > earth > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`

class Pokemon: 
    def __init__(self, name, primary_type, max_hp, hp) -> None:
        self.name = name

        if primary_type in ('water', 'fire', 'earth'):
            self.primary_type = primary_type
        else:
            print('Invalid Primary Type.')
        
        self.max_hp = max_hp
        self.hp = hp
    
    def battle(self, enemy):
        if self.primary_type == enemy.primary_type:
            return 'It is a draw.'
        
        elif self.primary_type == 'water':
            if enemy.primary_type == 'fire':
                enemy.hp -= 10
                return f'{enemy.name} loses 10 hp and has {enemy.hp} hp left.'
            elif enemy.primary_type == 'earth':
                self.hp -= 10
                return f'{self.name} loses 10 hp and have {self.hp} hp left.'

        elif self.primary_type == 'fire':
            if enemy.primary_type == 'earth':
                enemy.hp -= 10
                return f'{enemy.name} loses 10 hp and has {enemy.hp} hp left.'
            elif enemy.primary_type == 'water':
                self.hp -= 10
                return f'{self.name} loses 10 hp and have {self.hp} hp left.'
        
        elif self.primary_type == 'earth':
            if enemy.primary_type == 'water':
                enemy.hp -= 10
                return f'{enemy.name} loses 10 hp and has {enemy.hp} hp left.'
            elif enemy.primary_type == 'fire':
                self.hp -= 10
                return f'{self.name} loses 10 hp and have {self.hp} hp left.'
    
    def feed(self):
        self.hp += 20
        return f"{self.name}'s hp is now recovered to {self.hp}."
    
    def __str__(self) -> str:
        return f'Name: {self.name}\nType: {self.primary_type}\nMax HP: {self.max_hp}\nCurrent HP:{self.hp}'
