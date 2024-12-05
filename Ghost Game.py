#Ghost Game by Dc117 Corp.
from random import randint
print('Ghost Game V1.02')
feeling_brave=True
score=0
while feeling_brave:
    ghost_door=randint(1, 3)
    print('Three doors ahead...')
    print('A ghost behind one.')
    print('Which door do you open?')
    door=input('1, 2, or 3?')
    door_num=int(door)
    if door_num==ghost_door:
        print('GHOST!')
        feeling_brave=False
    else:
        print('No ghost!')
        print('You enter the next room.')
        score=score+1
print('Run Away!')
print('Game Over! You scored', score)