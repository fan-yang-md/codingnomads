# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Write your code below here

#sort the list
randlist.sort()
print(randlist)

tuple_pair = ()
new_list = []

#add 0 to list if odd-numbered
if len(randlist) % 2 != 0:
    randlist.append(0)
print(randlist)

#pairing the numbers in tuples and saving them in one list
for index in range(len(randlist)-1):
    if index % 2 == 0:
        tuple_pair = (randlist[index], randlist[index+1])
        new_list.append(tuple_pair)
        print(tuple_pair)
        
print(new_list)