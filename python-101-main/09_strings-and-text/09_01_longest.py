# Which of the following strings is the longest?
# Use the len() function to find out.

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"

def find_longest_word(list):
    longest_word = ''
    for item in list:
        if len(item) > len(longest_word):
            longest_word = item
    return longest_word

list = {longest_finnish_word, longest_hungarian_word, longest_finnish_word, strong_password}

print(f'the longest word in the list is: {find_longest_word(list)}')