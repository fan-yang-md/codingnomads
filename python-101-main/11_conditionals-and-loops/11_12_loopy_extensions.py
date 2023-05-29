# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"
is_pdf = False
for n in range(len(filename)):
    if filename[n] == 'p' and filename[n+1]=='d' and filename[n+2]=='f':
        is_pdf = True

print(f'is it a pdf? {is_pdf}')