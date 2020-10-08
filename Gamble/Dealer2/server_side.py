from load_deck import *
from time import sleep
import random
Fins=100
seed = random.randint(0,100)
random.seed(seed)

##########
def compare(aguess,astake):
    global cards
    card = str(cards.deck[0])
    card = card[1:-1].split('.')
    suit, rank=card
    suit=suit.lower()
    rank=rank.lower()
    card=(suit,rank)
    if aguess==card:
        global Fins
        print('\n__________\n')
        print('\ncorrect!!!\n')
        print(f'\n the card was {suit} {rank}\n')
        Fins+=astake
    else: 
        print('\n__________\n')
        print('\nWronggggg!!!!!\n')
        print(f'\n the card was {suit} {rank}\n')
        Fins-=astake
    cards.deck.pop(0)
#############
dealer2='''
    ____________
    |           |
    |           |
    |           |
    |           |
____|___________|_____
    ┃　　　　　　 ┃ 　 
    ┃　　　━　　　┃  
    ┃　┳┛　   ┗┳　┃ 
    ┃　　　　　　 ┃  
    ┃　 ______  　┃  
    ┃　　　　　　 ┃   
    ┗━┓　　　  ┏━┛  
'''
dealer2=dealer2.splitlines()
description='''After defeating Dealer 1, the guards take all the Fins you earned back except 100 Fins and escort you to another room. This room is relatively confined and, of course, have a roof. 
A tall man with a cool tall hat sitting behind the table in the middle of the room with a deck of cards in his hands.
 (Rule is still the same you start with 100 Fins and the goal is to get 1000 Fins)
'''
description=description.splitlines()
dialogue='''Dealer2: Greetings, I am dealer2.
Dealer2: The game we are going to play is easy. 
Dealer2: Here is a new deck of 52 playing cards (no jokers).
Dealer2: I am going to shuffle a new deck "randomly", and you are going to guess what the card on top of the deck is.
Dealer2: You can put at least 30 Fins(no maximum) as stake before I reveal the card.
Dealer2: If you get it wrong, you lose all the Fins and I will reveal the card and you .
Dealer2: If you get it right, you get your stake back and win an extra Fins of the number you put in.
Dealer2: No matter you get it right or wrong, the card get removed and the next card becomes the card on the top
Dealer2: Then you guess that card, and the process is repeated.
Dealer2: If you have less than 30 Fins, you will lose the game.
Dealer2: If you get more than 1000 Fins, you win and move to next level.
Dealer2: Are you ready?
'''
dialogue=dialogue.splitlines()
for line in description:
    print(line)
    #sleep(2)


for line in dealer2:
    print(line)
    #sleep(0.2)
for line in dialogue:
    print(line)
    #sleep(2)
input('type in anything when you are ready')
###############


print('\ndealer 2 is shuffling\n')
create_deck()
shuffle_deck(100)
#sleep(5)
print('\nthe deck is ready\n')
while Fins>0:
    print('\n_________________\n')
    print(f'you current balance is {Fins}')
    print('\n_________________\n')
    print('input your stake:\n')
    stake=int(input(''))
    if stake < 30:
        print('\nThe stake must be at least 30 Fins, put a valid input\n')
        continue
    print('\n ________________\n')
    print('\nYour guess for suit\n')
    print('\ntype in your answer in either spade, heart, diamond, club\n')
    guess_suit=input('').lower()
    print('\n ________________\n')
    print('\nYour guess for the rank\n')
    print('\ntype in your answer as an integer between 2-10 inclusive, Ace, Jack, Queen, or King')
    guess_rank=input('').lower()
    guess=(guess_suit,guess_rank)
    print(f'your guess is {guess_suit} {guess_rank}')
    compare(guess,stake)
    print(f'you current balance is {Fins}')
    if Fins >= 1000:
        print('\n ________________\n')
        print('you win!!!!!!!')
        print('\nflag{i_know_the_game_is_bad_but_suck_it}\n')
        break

    print('\n ________________\n')
    print('\nReady for next round? If you are type in anything.\n')
    input('')
    if Fins <=30:
        print('you lose')   
