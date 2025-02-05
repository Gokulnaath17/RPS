def Guess():
    import argparse
    import random
    parse=argparse.ArgumentParser(description='Enter your name ')
    parse.add_argument('-n','--name',metavar='Name',dest='username',required=False,help='Enter your name with the flag -n or --name')
    name=parse.parse_args()
    def outer(playern):
        n=0
        pl=0
        sy=0
        def guesser():
                while True:
                    b=(input(f'\n {playern}, guess which number I am thinking of 1,2,3,4: '))
                    if b not in ('1','2','3','4'):
                        continue
                    nonlocal n,pl,sy
                    l=('1','2','3','4')
                    system=random.choice(l)
                    print(f'\n {playern} choose: {b} \n System choose: {system}')
                    if system==b:
                        print(f' {playern} wins')
                        pl+=1
                    else:
                        print(f" {playern} lose")
                        sy+=1
                    n+=1
                    # if pl!=0:
                    print(f'\n {playern}\'s winning percentage : {pl/n:.1%}')
                    print(f'\n Game count {n}')
                    c=input(f'\n Do you want to continue {playern} Y or N ? ').strip().lower()
                    if c=='y':
                            continue
                    else:
                        print(f'\n Bye {playern}')
                        break
        return guesser()
    if name.username ==None:   
        outer('Player')
    else:
         outer(name.username)
    
if __name__=='__main__':
      Guess()
        
  


