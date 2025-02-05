import rps
import test1
import sys
p=(input('\n Welcome to the arcade \n Games \n Press 1 for ROCK PAPER SCISSOR \n Press 2 for GUESS THE NUMBER \n Q to quit \n '))
if (p.strip().lower())=='q':
    sys.exit()
p=int(p)
if p==1:
    rps.ROCK() 
elif p==2:
    test1.Guess()
else:
    print('Please enter a valid number')