from ingredients import Ingredient, Spice

class Soup:
    def __init__(self, items, spices) -> None:
            self.items = items
            self.spices = spices


    def cook(self):
        print('for this soup, we are adding:\n')
        mixture = ""
            # import pdb
            # breakpoint()

        for item in self.items:
             mixture = mixture + f'{item.name}, portion: {item.amount}\n'
        for spice in self.spices:
             mixture = mixture + f'{spice.name}, portion: {spice.amount}, making the soup {spice.flavor}\n'
        return mixture

def main():
    tofu = Ingredient('tofu', 10)
    bokchoy = Ingredient('bok choy', 5)
    green_onion = Ingredient('green onion', 1)

    salt = Spice('salt', 1, 'salty')
    pepper = Spice('pepper', 1, 'spicy')

    delicious_soup = Soup([tofu, bokchoy, green_onion], [salt, pepper])

    print(delicious_soup.cook())

main()