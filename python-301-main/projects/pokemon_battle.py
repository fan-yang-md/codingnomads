from pokemon_game import Pokemon

charizard = Pokemon('Charizard', 'fire', 100, 100)
squirtle = Pokemon('Squirtle', 'water', 100, 100)

battle1 = charizard.battle(squirtle)
print(battle1)
print()
print(charizard)
print()
print(squirtle)