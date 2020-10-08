from load_deck_copy import *
seed=random.randint(0,10000)
print(f'seed is {seed}')
random.seed(seed)
create_deck()
initial_deck=list(cards.deck)
shuffle_deck(100)
result=list(cards.deck)
output=[]
for i in range(10001):
    cards.deck=list(initial_deck)
    random.seed(i)
    shuffle_deck(100)
    output.append(cards.deck)
candidiates=[]
counter=0
for deck in output:
    tem=[]
    for i in range(0,2):
        tem.append(deck[i]==result[i])
    if all(tem):
        candidiates.append(counter)
    counter+=1
print(len(candidiates))
print(candidiates)