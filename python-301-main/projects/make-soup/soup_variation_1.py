from ingredients import Ingredient, Spice

class Soup:
#I THINK you wanted to do this, but we can't do the following because python 
#(1) you can only give ONE *arg, and (2) python  won't know which list is spices
#  and which list is items! We NEED the **kwargs arg (here it is called soup_stuff)
#  to label our two input lists (items_list for the Ingredients items  and spices_list for the Spices)
    #def __init__(self, *spices, *items) -> None:
	def __init__(self, *ingredients, **spice_stuff) -> None:
		#self.ingredients = soup_stuff['ingredients']
		self.ingredients = ingredients
		self.spices = spice_stuff['spices']
		print(type(spice_stuff))

	def cook(self):
		print('for this soup, we are adding:\n')
		mixture = ""
		#for item in self.items:
        #    if isinstance(item, Spice):
        #        mixture = mixture + f'{item.name}, portion: {item.amount}, making the soup {item.flavor}\n'
        #    else:
        #        mixture = mixture + f'{item.name}, portion: {item.amount}\n'
        #return mixture
    
		for ingredient in self.ingredients:
			mixture = mixture + f'{ingredient.name}, portion: {ingredient.amount}\n'
		for spice in self.spices:
			mixture = mixture + f'{spice.name}, portion: {spice.amount}, making the soup {spice.flavor}\n'
		return mixture

def main():
	tofu = Ingredient('tofu', 10)
	bokchoy = Ingredient('bok choy', 5)
	green_onion = Ingredient('green onion', 1)
	#ingredients_list = [tofu, bokchoy, green_onion]

	salt = Spice('salt', 1, 'salty')
	pepper = Spice('pepper', 1, 'spicy')
	spices_list = [salt, pepper]

	#delicious_soup = Soup(ingredients=ingredients_list, spices=spices_list)
	delicious_soup = Soup(tofu, bokchoy, green_onion, spices = spices_list)
	print(delicious_soup.cook())

main()

