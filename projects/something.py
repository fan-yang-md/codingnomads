winning_words = "something"
input = input("write something to win: ").lower()

if winning_words in input:
    print("congrats!")
        
else:
    print ("nope!")