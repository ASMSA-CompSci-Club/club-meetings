##this will be able to be downloaded by score board
import random

random.seed(5)

Fins=100
survive = True

def load(spin):
    bullet_position=0
    bullet_position+=spin
    bullet_position=bullet_position%6
    print('the gun is loaded')
    return bullet_position


def ask():
    response=input('y for shoot at you. \nn for shoot at the sky\n')
    if response == 'y' or response == 'yes':
        return True
    elif response =='n' or response == 'no':
        return False
    else:
        print('\ninvalid input\n')
        ask()


def shoot(response, bullet_position):
    global Fins
    if response:
        if bullet_position == 0:
            print('Wrong guess, you die')
            global survive
            survive=False
        else:
            print('Luckily, you survive and get 50 Fins')
            Fins+=50
    else:
        if bullet_position == 0:
            print('Good guess! That was a close one!')
            Fins+=50
        else:
            print('Wrong guess, you lose 100 Fins')
            Fins-=100

while Fins >=0 and survive:
    print(f"your current balance is {Fins}")
    bullet_position=load(random.randint(1,6))
    response=ask()
    shoot(response, bullet_position)
