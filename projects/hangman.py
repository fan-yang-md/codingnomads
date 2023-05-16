# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
word = "sassy"
word_empty = "_____"
word_length = len(word)
attempts = word_length
total_correct = 0

#print("here is your word: " + "_ "*word_length)
print(f"here is your word: {word_empty}")
guess = input("you have: " + str(attempts) + " tries. Take your best shot and gimme a letter: ")

while attempts > 0: 
    if len(guess)>1 or guess == "":
        input("Invalid guess. Try again!")

    elif guess in word:
        position = word.find(guess)
        word_empty = word_empty[:position]+guess+word_empty[position+1:]
        attempts -= 1
        total_correct += 1
        if word_empty == word:
            print("Congrats!")
        else:
            guess = input(f"Good job! {word_empty} You have {attempts} attempts left.")
    else:
        attempts -= 1
        if attempts == 0:
            print("No attempts left. Game over.")
        else:
            input(f"Try again. {attempts} attempts left.")

# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it

