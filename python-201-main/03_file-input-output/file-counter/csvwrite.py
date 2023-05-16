# Write the file counts to a `.csv` file.
import csv

count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

""" 
with open('filecounts.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    data = [count[''], count['.csv'], count['.md'], count['.png']]
    csvwriter.writerow(data)
"""

with open('filecounts.csv', 'a') as csvfile:
    data = [count[''], count['.csv'], count['.md'], count['.png']]
    #print(data)
    data_string = ''
    for data_point in data:
        data_string += (str(data_point) + ",")
    csvfile.write('\n'+data_string)