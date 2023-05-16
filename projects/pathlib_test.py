import pathlib

path = pathlib.Path("/Users/13392/Desktop")

for filepath in path.iterdir():
    print(filepath.name)