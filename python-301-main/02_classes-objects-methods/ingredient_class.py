class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f'{self.name} ({self.amount})'

    def __repr__(self):
        return f'Ingredient(name={self.name}, amount={self.amount})'
    
carrots = Ingredient('carrot', 10)
broccoli = Ingredient('broccoli', 8)


