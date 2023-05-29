from ingredients import Ingredient, Spice

class Soup:
    def __init__(self, *ingredients) -> None:
            self.ingredients = ingredients
            self.spices = ingredients

    def cook(self):
        print('for this soup, we are adding:\n')
        mixture = ""
        for ingredient in self.ingredients:
            mixture = mixture + f'{ingredient.name}: {ingredient.amount} \n'
        
        for spice in self.spices:
             mixture = mixture + f'{spice.name}: {spice.amount}, {spice.flavor}\n'

        return mixture

tofu = Ingredient('tofu', 10)
bokchoy = Ingredient('bok choy', 5)
green_onion = Ingredient('green onion', 1)

salt = Spice('salt', 1, 'salty')
pepper = Spice('pepper', 1, 'spicy')

delicious_soup = Soup(tofu, bokchoy, green_onion, salt, pepper)
print(delicious_soup.cook())
