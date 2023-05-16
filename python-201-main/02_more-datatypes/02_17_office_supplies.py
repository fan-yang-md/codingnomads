# Using f-strings, print out the name, last name, and favorite
# office supply item of each person in the given dictionary,
# formatted like so:
#
# LASTNAME, Name           Office supply item
# LONGERLASTNAME, Name     Office supply item

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]
'''
i = 0
office_tuple = tuple(office)
print(office_tuple)

while i in range(len(office_tuple)):
    i+=1
    full_name = office_tuple[i]
'''
'''
for each_dict in office:
    full_name = each_dict["full_name"].split()
    last_name = full_name[-1]
    first_name = full_name[0]
    length_last_name = len(last_name)
    length_first_name = len(first_name)

    print(f"{last_name}, {first_name} {each_dict['item']}")
'''

#Ange version
final_list = []
for i, each_dict in enumerate(office):
    full_name_length = len(each_dict['full_name'])
    full_name = each_dict["full_name"].split()
    last_name = full_name[-1]
    first_name = full_name[0]    
    last_name_length = len(last_name)
    each_dict["last_name_length"] = last_name_length
    each_dict['full_name_length'] = full_name_length
    each_dict['last_name'] = last_name
    each_dict['first_name'] = first_name
    del each_dict['full_name']
        
sorted_office = sorted(office, key = lambda dict:dict["last_name_length"])

column_length = sorted_office[-1]['full_name_length'] + 10

for i, each_dict in enumerate(sorted_office):
    num_spaces = column_length - each_dict['full_name_length'] - 2
    print(f"{each_dict['last_name'].upper()}, {each_dict['first_name']}" + " "*num_spaces + each_dict['item'])

#print(sorted_office)
