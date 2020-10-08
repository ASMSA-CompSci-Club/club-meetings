import random
class cards:
    deck=[]
    @staticmethod
    def decide(asuit, anumber):
            suit=['spade','heart','diamond','club']
            number=['Ace']
            number.extend(range(2,11))
            number.extend(['Jack','Queen','King'])
            asuit=suit[asuit]
            anumber=number[anumber-1]
            return (asuit,anumber)
    #suit is a number in range[0,3] spade-heart-diamond-club
    def __init__(self, suit, number):
        self.suit, self.number = self.decide(asuit=suit,anumber=number)
        self.deck.append(self)
    @classmethod
    def shuffle(self):
        shift=random.randint(0,len(self.deck)-1)
        choosen_card=self.deck.pop(shift)
        shift=shift+random.randint(0,100)
        shift=shift%51
        self.deck.insert(shift,choosen_card)

    def __repr__(self):
        return f'({self.suit}.{self.number})'
def create_deck():
    for i in range(4):
        for j in range(1,14):
            cards(i,j)
def shuffle_deck(times):   
    for k in range(times):
        cards.shuffle()
