print('hello future dragon riders')
print("hello")
print('I hope you have fun','To have fun you MUST FOLLOW the rules')
print('by the way i\'m Rayd')
_get_ready='get ready'
print(_get_ready)
print(0o45+0x39)
print('think'*3,'what dragon will you choose')
user_dragon=input('so what dragon have you chosen ')
#&out puts the smaller number if 2 and 2 are given then it outputs 2
#| outputs the larger no. if 2 and 2 are given then it outputs 2
# ^out puts 0 if the same numbers are provided and outputs 1 if 2 different no. are gien
#  ~ outputs the negative opposite of the positive numbers starting from 0=-1 and vice versa 
# 12<<1 outputs 12*2 wich is 24 12<<2=48 12<<3=96 and so on
# 12>>1 out puts 12%2 wich is six 12>>2=3 and so on 
if user_dragon=='Skrill'or user_dragon=='night fury'or user_dragon=='Lightfury'or user_dragon=='Bewilderbeast'or user_dragon=='Red death'or user_dragon=='Screaming death'or user_dragon=='Night light'or user_dragon=='Typhoomerang'or user_dragon=='Whispering death'or user_dragon=='Shell fire'or user_dragon=='Sea shocker'or user_dragon=='Submaripper'or user_dragon=='Scauldron'or user_dragon=='Buffalord':
    print('sorry the dragon you chose is either too rare or cannot be trained by beginners or is too dangerous for beginners or cannot be rided ')
else:
    print('g','o','o','d',sep='🐉',end='!!!')
my_dragon=input('What dragon do you think I own, it is black and yellow and breaths fire')
while my_dragon !='Triple stryke':
    print('Try again')
    if my_dragon=='Skrill'or my_dragon=='Singetail'or my_dragon== 'Night fury':
        print('It can rival that dragon')
    my_dragon=input('What dragon do you think I own, it is black and yellow and breaths fire ')
else:
    print('Great job')    
a=0
dangerous_dragon=['Skrill','Singetail','Screaming death','Whispering death','Submaripper','Shellfire','Scauldron','Sea shocker','Tryple stryke','Furies and Night lights']
for B in dangerous_dragon:
    a+=1
    print('Dangerous dragon no.',a,B,sep=' ')  
user_safety=input('Now tell me what dragon have you chosen and I will tell you if it is a starter dragon') 
starters={'Gronckle':'Starter','Monstrous nightmare':'Starter','Hideous zippleback':'Starter','Deadly nadder':'Starter'}     
if user_safety in starters:
    print(starters[user_safety])
Triple_stryke_info=('Color:Black and yellow stripes','Eye color:Red','Size:Moderate','Inteligence:High','no.'[2])
for inform in Triple_stryke_info:
    print(inform)


def situation(hunter=input('Drago captered your friends and there dragons and would kill your friends and thier dragons if you attacked what will you do')):
    if hunter =='Send a terror mail to Berserker Island to lend some gold and Berk to lend meta to exchange with Drago 'or hunter=='launch a stealth mission':
        print('You are a worthy dragon rider')
    else:
        print('Try again')
        hunter=input('Drago captered your friends and there dragons and would kill your friends and thier dragons if you attacked what will you do')
        if hunter =='Send a terror mail to Berserker Island to lend some gold and Berk to lend meta to exchange with Drago 'or hunter=='launch a stealth mission':
            print('You need more practice')    
        else:
            print('your fired!!')  

situation()   
def favnum():
    for i in range(0,123,2):
        yield(i)
favnum()    
gen=favnum
print(next(gen))
print(next(gen))
print(next(gen))
