import random

#take in a number and return a string representation of the hand. 
def get_hand(hand):
    if hand == 0:
        return 'scissor'
    elif hand == 1:
        return 'rock'
    elif hand == 2:
        return 'paper'
    
#determine winner
def get_winner(player, computer):
    if (player > computer) or (player < computer and player == 0 and computer == 2):
        return "You win!"
    elif player == computer:
        return "it's a tie!"
    else:
        return "You lose!"



#prompt user to choose a hand.
player_hand = int(input('OK player, choose your hand wisely: \
\n 0 = scissor\
\n 1 = rock \
\n 2 = paper \
\n 3 = quit \n'))

while player_hand != 3: 
    if player_hand > 3:
        player_hand = int(input('Invalid hand. Choose again: '))
    else:
        computer_hand = random.randint(0, 2)
        print(f'You chose: {get_hand(player_hand)}')
        print(f'Computer chose: {get_hand(computer_hand)}')
        print(get_winner(player_hand, computer_hand))
        player_hand = int(input('Play again or enter 3 to quit: \
\n 0 = scissor\
\n 1 = rock \
\n 2 = paper \
\n 3 = quit \n'))
