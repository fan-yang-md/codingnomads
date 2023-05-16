# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
from pathlib import Path

nomad_folder = Path('/Users/13392/Documents/codingnomads')

for each_item in nomad_folder.iterdir():
    if each_item.is_file():
        if ".py" in each_item.name:
            print(str(nomad_folder) + ": " + str(each_item.name))
    elif each_item.is_dir():
        for sub_item in each_item.iterdir():
            if sub_item.is_file():
                if ".py" in sub_item.name:
                    sub_item_path = nomad_folder.joinpath(each_item)
                    print(str(sub_item_path) + ": " + str(sub_item.name))