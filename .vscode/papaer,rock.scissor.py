import sys
import random
global additional
additional = 3
a = 0
b = 0
user_choice = 0


def func():
    a = 0
    b = 0
    sd = int(round)
    print('paper=1 rock=2 scissors=3')
    for i in range(sd):
        user_choice = input('what do you choose 1 2 or 3 or EXIT to exit ')
        computer_choice = ['1', '2', '3']
        if user_choice in computer_choice:
            num = random.choice(computer_choice)
            if (num == '3' and user_choice == '2') or (num == '1' and user_choice == '3') or (num == '2' and user_choice == '1'):
                a += 1
                print("Computer chose " + num+'\n'+name +
                      ':'+str(a)+'\ncomputer:'+str(b))
            elif (user_choice == '3' and num == '2') or (user_choice == '1' and num == '3') or (user_choice == '2' and num == '1'):
                b += 1
                print("Computer chose " + num+'\n'+name +
                      ':'+str(a)+'\ncomputer:'+str(b))
            else:
                print("Computer chose " + num+'\n'+name +
                      ':'+str(a)+'\ncomputer:'+str(b))
        elif user_choice == 'EXIT':
            if a < b:
                c = b-a
                print('you 👎LOST👎 BY:'+str(c)+' points')
                sys.exit()
            elif b < a:
                c = a-b
                print('''  YOU---WON-- BY'''+str(c)+' point')
                sys.exit()
            else:
                print('''YOU TIED''')
                sys.exit()
        else:
            func()


print("Welcome to Paper Rock Scissor Game")
name = input('what is your name? ')
round = input('How many rounds do you want to play? ')
if round.isdigit() == False:
    for i in range(3):
        if round.isdigit() == True:
            break
        print("you entered wrong")
        round = input('How many rounds do you want to play? ')
    else:
        print('sorry invalid answer')
        sys.exit()

func()