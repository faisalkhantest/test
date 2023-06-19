import sys
Lawn_tennis_players=['Fedrer','Nadal','Djokovic','Carlos','Andy','Andrey','Stefanos ','Pete']
tennis_rackets=['speed','gravity','power','extreme','radical','stream']
user_choice=input('Hi what would you like to choose rackets or players ')
rackets2=[]
players1=[]
rackets1=[]
players2=[]
try:
 if user_choice=='rackets':
    a=len(tennis_rackets)
    a//=2
    for i in range(a):
       print('Here are your  options')
       print(tennis_rackets)
       racket1=input('which one do you choose p1? ')
       print('Here are your  options')
       rackets1.append(racket1)
       tennis_rackets.remove(racket1)
       print(tennis_rackets)
       racket2=input('which one do you choose p2? ') 
       rackets2.append(racket2)
       tennis_rackets.remove(racket2)
    print('p1\'s selections')
    print(rackets1)
    print('p2\'s selections')
    print(rackets2)
 elif user_choice=='players':
    b=len(Lawn_tennis_players)
    b//=2
    for i in range(b):
      print('here are your options')
      print(Lawn_tennis_players)
      player1=input('Who do you choose p1 ')
      players1.append(player1)
      Lawn_tennis_players.remove(player1) 
      print('here are your options')
      print(Lawn_tennis_players)
      player2=input('Who do you choose p2 ')
      players2.append(player2)
      Lawn_tennis_players.remove(player2)
      print('p1\'s selections')
      print(players1)
      print('p2\'s selections')
      print(players2)
 else:
   print('your fired')
   sys.exit()
except:
  print('sorry_sonething_strange_happened..........reloading........reloding..........reloading............reloading_complete!!!')
  if user_choice=='rackets':
    a=len(tennis_rackets)
    a//=2
    for i in range(a):
       print('Here are your  options')
       print(tennis_rackets)
       racket1=input('which one do you choose p1? ')
       print('Here are your  options')
       rackets1.append(racket1)
       tennis_rackets.remove(racket1)
       print(tennis_rackets)
       racket2=input('which one do you choose p2? ') 
       rackets2.append(racket2)
       tennis_rackets.remove(racket2)
    print('p1\'s selections')
    print(rackets1)
    print('p2\'s selections')
    print(rackets2)
  elif user_choice=='players':
    b=len(Lawn_tennis_players)
    b//=2
    for i in range(b):
      print('here are your options')
      print(Lawn_tennis_players)
      player1=input('Who do you choose p1 ')
      players1.append(player1)
      Lawn_tennis_players.remove(player1) 
      print('here are your options')
      print(Lawn_tennis_players)
      player2=input('Who do you choose p2 ')
      players2.append(player2)
      Lawn_tennis_players.remove(player2)
      print('p1\'s selections')
      print(players1)
      print('p2\'s selections')
      print(players2)
  else:
   print('your fired')
   sys.exit()