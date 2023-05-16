# Use the `csv` module to read in and count the different file types.
#import csv
import json
from pathlib import Path

filepath = Path('/Users/13392/documents/codingnomads/python-201-main/03_file-input-output/file-counter')


with open(filepath.joinpath('filecounts.json'),'r') as file_count:
    data = file_count.read()

jdata = json.loads(data)
#print(type(jdata['']))

print(f"There are: \n {jdata['']} folders \n {jdata['.csv']} .csv files \n {jdata['.md']} .md files \n {jdata['.png']} .png files")