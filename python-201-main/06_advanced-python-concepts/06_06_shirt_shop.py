# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

shop_inventory = []

for color_ in colors:
    for size_ in sizes:
        tuple_ = (color_,size_)
        shop_inventory.append(tuple_)

print(f'Come check out our inventory and find something you like! \n{shop_inventory}')