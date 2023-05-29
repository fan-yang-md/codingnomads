import requests
import webbrowser

class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f'{self.name} ({self.amount})'

    def __repr__(self):
        return f'Ingredient(name={self.name}, amount={self.amount})'
    
    def get_info(self):
        url = f'https://en.wikipedia.org/wiki/{self.name}'
        response = requests.get(url)
        if response.status_code == 200:
            webbrowser.open_new(url)
        else:
            print("Failed to open the web page.")


class Spice(Ingredient):
    def __init__(self, name, amount, flavor):
        super().__init__(name, amount)
        self.flavor = flavor
    def __str__(self):
        return super().__str__() + f'\nFlavor ({self.flavor})'
    