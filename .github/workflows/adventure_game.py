import time
import random
# Objects
Places = ['Forest', 'Desert', 'House']
Weapons = ['Sword' , 'Knife', 'Gun', 'Rock']
Forest_Monesters = ['Bear', 'Rabbit', 'Lion', 'Wolf', 'Monkey']
Desert_Monesters = ['Alien', 'Giant Monster', 'Snake', 'Dog']
House = ['Eat', 'Drink', 'Sleep', 'Watch Movie']
Game_Result = ['Win', 'Lose']
# End of Objects
print('Welcome to the game of adventures fun game')
time.sleep(1)
print('Takes you to another world of fun and thrill')
time.sleep(1)
print('We will help you during the game choice, but you will think before choosing then you can win.')
time.sleep(1)
name = input('Please give me your name\n')
time.sleep(1)
print('Please choose which place you want to play\n')
time.sleep(1)
for place in Places:
    print(place)
    time.sleep(1)
Choice = ''
while Choice not in Places:
    msg = 'Give me your \n for forest write f or forest or 1\n for desert write d or desert or 2\n for house write h or house or 3\n'
    Choice=input(msg)
    if Choice.lower() == 'Forest'.lower() or Choice.lower() == 'F'.lower() or Choice.lower() == '1'.lower():
        Choice = 'Forest'
    elif Choice.lower() == 'Desert'.lower() or Choice.lower() == 'D'.lower() or Choice.lower() == '2'.lower():
        Choice = 'Desert'
    elif Choice.lower() == 'House'.lower() or Choice.lower() == 'H'.lower() or Choice.lower() == '3'.lower():
        Choice = 'House'
    else:
        Choice = ''
time.sleep(1)
print('You have a weapon')
weaponchoosed = random.choice(Weapons)
print(weaponchoosed)
changerequest = input('would you like to change weapon\n')
if changerequest == 'yes':
    weaponchoosed = random.choice(Weapons)
    print(weaponchoosed)
print('\nNow you are in ' + Choice + ' and you have a weapon ' + weaponchoosed)
time.sleep(1)
print('Now in front of you ')
if Choice == 'Forest':
    print(random.choice(Forest_Monesters))
if Choice == 'Desert':
    print(random.choice(Desert_Monesters))
if Choice == 'House':
    print(random.choice(House)) 
print('Use the weapon to kill monster\n')
time.sleep(1)
print('you ' + random.choice(Game_Result))
time.sleep(1)
print('Game Over')
