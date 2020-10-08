import random

random.seed(0)

flag = "FLAG{this is the flag}"
_flagChecker = False
money = 100
while 0<money<1000:
print("Your current balance is " + str(money) + " Fins \n" )
x =int(input("how much do you want to gamble?"))
money-=x
if random.randrange(2)==0:
money += x*5
if(money <= 0):
_flagChecker = False
if(money >= 1000):
_flagChecker = True

if _flagChecker == True:
print("\nCongratulations you've won the jackpot!\n")
print(flag)
else:
print("You lost, try again.")