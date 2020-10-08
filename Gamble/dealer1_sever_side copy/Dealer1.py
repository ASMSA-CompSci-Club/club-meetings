from time import sleep
dealer1='''
        _________
     ___|_______|____
       | _    _  |   
       |   /     |   
        \  __   /
         \     /
        /      \ 
       /        \ 
      /          \ 
     /___ /̵͇̿̿/'̿'̿ ̿ ̿̿ ̿̿ ̿̿
    ------|        \ 
   /                \ 
'''
dealer1=dealer1.splitlines()
dealer1_talking='''
        _________
     ___|_______|____
       | _    _  |   
       |   /     |   
        \  口   /
         \     /
        /       \ 
      /          \ 
     /            \ 
    /___ /̵͇̿̿/'̿'̿ ̿ ̿̿ ̿̿ ̿̿
    ------|         \ 
   /                 \ 
'''
dialogue='''Dealer1: Greetings. My name is Jack. You can just call me Dealer 1 (Honestily I don't care what you call me for you will be dead in no time).
Dealer1: The game I am going to play with is Russian Roulette, but it is going to be a little different.
Dealer1: I will start each game by loading one bullet into the top slot for the cylinder and spin the cylinder 'randomly'.
Dealer1: After the cylinder stop spinning, I will let you choose to either let me shoot at you or shoot at the sky
Dealer1: If you choose to let me shoot at you and there is bullet in that slot, appearantly you die and I get all you Fins.
Dealer1: If there is no bullet in that slot, you win 50 Fins.
Dealer1: If you choose let me shoot at the sky there is bullet in that slot, then lucky of you to escape from death.
Dealer1: If you choose to let me shoot at the sky and there is no bullet in that slot, then wrong guess you die.
Dealer1: Are you ready to play?
'''
dialogue=dialogue.splitlines()


def talking():
    for lines in dealer1:
        print(lines)
        sleep(0.2)
    sleep(0.5)
    print('You are escorted by two guards into a small chamber that does not have a roof and there sit a man with a cool hat and a revolver')
    sleep(5)
    print('As the guards recede to the side, the man starts talking')
    sleep(3)
    print(dealer1_talking)
    sleep(1)
    for line in dialogue:
        sleep(3)
        print(line)
    response=input('\npress return to start\n')
    print('\n','\n')


