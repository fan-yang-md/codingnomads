# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

string = input('give me a sentece: ')
a = 0
e = 0
i = 0
o = 0
u = 0
for char in string:
    if char == 'a':
        a+=1
    elif char == 'e':
        e+=1
    elif char == 'i':
        i+=1
    elif char == 'o':
        o+=1
    elif char == 'u':
        u+=1

print(f'a: {a}, e: {e}, i: {i}, o: {o}, u: {u}')

