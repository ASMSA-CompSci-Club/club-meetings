from time import sleep     
import Dealer1
import Game1
title = '''         
___________.__               ________              ___.   .__             ________                       
\__    ___/|  |__   ____    /  _____/_____    _____\_ |__ |  |   ____    /  _____/_____    _____   ____  
  |    |   |  |  \_/ __ \  /   \  ___\__  \  /     \| __ \|  | _/ __ \  /   \  ___\__  \  /     \_/ __ \ 
  |    |   |   Y  \  ___/  \    \_\  \/ __ \|  Y Y  \ \_\ \  |_\  ___/  \    \_\  \/ __ \|  Y Y  \  ___/ 
  |____|   |___|  /\___  >  \______  (____  /__|_|  /___  /____/\___  >  \______  (____  /__|_|  /\___  >
              n  \/     \/          \/     \/      \/    \/          \/          \/     \/      \/     \/ 
'''
title=title.splitlines()
intro='''
In year 2270, the world is composed of of a handful of extremely wealthy elites who rule the world. While the rest of people 
struggle in poverty. For the poor majority, the only way to escape poverty and jump into the higher class is to attend the Gamble Game 
where they stake their lives to gamble with other participants. It is broadcasted all over the world to entertain
 the higher class. At the age of 15 the gambling draft is started. It doesn't end until the particapant has graduated
 high school, and you are unluckily in this year's gambling game -- there are only two results waiting for you:
 to amass a fortune big enough to by your soul back, or to die. 
 '''
intro=intro.splitlines()
opening='''
Greetings Participants! (｡･ω･)ﾉﾞ
The game is composed of four levels.
In each, each participant gets 100 Fins to start, and get assigned to a chamber with a dealer for that level.
The participant loses when he loses all his or her Fins and leaves the game, and the participant can only leave 
by earning more than 1000 Fins. 
The game to play entirely depends on the dealer, but difficulty increases as level increases.
Are your ready for the first level? ٩(ˊᗜˋ*)و
'''
opening=opening.splitlines()



for line in title:
    print(line)
    sleep(0.3)
for line in intro:
    print(line)
    sleep(1)

response=input('\n do you want to proceed to the opening\n answer yes to proceed or no to not (I highly recommend you not to skip for this is important)\n')
if response =='yes':
    for line in opening:
        print(line)
        sleep(1)
    input('\n type in anything when you are ready')
response=input('skip the talking? \n y for yes n for no')
if response=='n':
    Dealer1.talking()
Game1.game()