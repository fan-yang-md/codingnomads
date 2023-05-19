# Using a listcomp, create a list from the following tuple that includes
# only words ending with -fish. Tip: Use an `if` statement in the listcomp.

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')
fish_list = []
for tuple_ in fish_tuple:
    if tuple_[-4:] == 'fish':
        fish_list.append(tuple_)

print(fish_list)
