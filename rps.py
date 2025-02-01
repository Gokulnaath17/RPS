import random
import argparse
import sys
def c(name,lang):
    gamecount=0
    play=0
    python=0
    ti=0
    print(f"\n {lang},{name} welcome to rps game, hope you have a great time")
    def rps():
     while True:
        nonlocal play,python,ti
        list=['3','1','2']
        player=input(f'\n {name},enter 1 for Rock:  \n Enter 2 for Paper: \n Enter 3 for Scissor:\n ')
        system=random.choice(list)
        if player not in list:
            print(f"\n {name},please enter a valid input")
            return rps()
        print(f'\n {name} chose: {player}\n System chose: {system}')
        if (player=='1' and system=='3') or (player=='2' and system=='1') or (player=='3' and system=='2'):
            print(f'\n {name} wins')
            play+=1
        elif player==system:
            print('\n Tie game')
            ti+=1
        else:
            print('\n System wins')
            python+=1
        nonlocal gamecount
        gamecount+=1
        print(f'\n Game count: {gamecount}')
        print(f'\n Player wins: {play}')
        print(f'\n Python wins: {python}')
        print(f'\n Tie games: {ti}')
        exi=input('\n\n Do you wish to continue Y/N  \n ').strip().lower()
        return rps() if exi=='y' else print(f'\n Bye {name}');break
    return rps()
if __name__=="__main__":
    
    gr={'English':'Hello','Tamil':'Vanakam','German':'Halo'}
    parse=argparse.ArgumentParser(description='Provides a pesonalized greeting to the player')
    parse.add_argument('-n',metavar='   Name',dest='user_name',required=True,help='Enter your name using the -n flag')
    parse.add_argument('-l',metavar='Language',dest='lang',required=True,choices=('English','Tamil','German'),help='For selecting the language with -l flag')
    arg=parse.parse_args()
    c(arg.user_name,gr[arg.lang])