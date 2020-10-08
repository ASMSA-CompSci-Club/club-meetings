deck0='(spade.Ace), (spade.2), (spade.3), (spade.4), (spade.5), (spade.6), (spade.7), (spade.8), (spade.9), (spade.10), (spade.Jack), (spade.Queeen), (spade.King), (heart.Ace), (heart.2), (heart.3), (heart.4), (heart.5), (heart.6), (heart.7), (heart.8), (heart.9), (heart.10), (heart.Jack), (heart.Queeen), (heart.King), (diamond.Ace), (diamond.2), (diamond.3), (diamond.4), (diamond.5), (diamond.6), (diamond.7), (diamond.8), (diamond.9), (diamond.10), (diamond.Jack), (diamond.Queeen), (diamond.King), (club.Ace), (club.2), (club.3), (club.4), (club.5), (club.6), (club.7), (club.8), (club.9), (club.10), (club.Jack), (club.Queeen), (club.King)'
deck0=deck0.split(', ')
deck=[]
for card in deck0:
    card = card[1:-1].split('.')
    suit, number=card
    deck.append((suit,number))
#Above code is just setting up the deck that the dealer is using, don't worry about it.
#Here is the actual good stuffs
import random
seed=random.randint(0,100)
random.seed(seed)
def shuffle():
    shift=random.randint(0,len(deck)-1)
    choosen_card=deck.pop(shift)
    shift=shift+random.randint(0,100)
    shift=shift%51
    deck.insert(shift,choosen_card)
#The way the dealer 2 shuffles the deck is to repeat shuffle 100 times namely:
for i in range(100):
    shuffle()
#Now you know how do the dealer shuffle the deck. 
# Also remember that the cart at top of the deck is deck[0], and each the time a card get removed the card after it
#becomes the cart on top of the deck
