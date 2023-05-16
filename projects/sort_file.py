# Import pathlib
import pathlib

# Find the path to my Desktop
desktop = pathlib.Path('/Users/13392/Desktop')

# List all the files on there
# Filter for screenshots only
#for each_file in desktop.iterdir():
#    if each_file.suffix in ['.mp4', '.mkv', '.avi']:
#        print(each_file.name)

# Create a new folder
#new_path = pathlib.Path('/Users/13392/Desktop/Movies')
#new_path.mkdir(exist_ok=True)
new_path = desktop.joinpath("Movies")
new_path.mkdir(exist_ok=True)

# Move the screenshots in there
for each_file in desktop.iterdir():
    if each_file.suffix in ['.mp4', '.mkv', '.avi', '.m4v']:
        new_file_path = new_path.joinpath(each_file.name)
        each_file.replace(new_file_path)
        #print(each_file)