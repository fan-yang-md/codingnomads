lowercase_letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = int(input("choose your cipher index: "))
deciphered = ""

for char in secret:
    if char.isalpha():
        x = lowercase_letters.find(char.lower())
        new_char = lowercase_letters[x+cipher]
        deciphered += new_char
    else:
        deciphered += char

print(deciphered)
print(deciphered[::-1])