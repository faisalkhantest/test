import sys
library=['a','b','c','d','e','f','g','h','i','j']
while True:
 user_name=input('Hello what is your name? ')
 user_book=input('What book would you like to borrow? ')
 if user_book in library:
    print('Hi '+user_name+' the book you want to borrowed is available')
    def rent(rental):
     if rental=='borrow':
      library.remove(user_book)
     elif rental=='EXIT':
       sys.exit()
     else:
       print('sorry you did not provide a valid answer')
    rent(input('would you like to borrow the book:'+user_book+' if you do then enter borrow or EXIT to exit '))
 else:
   print('sorry we do not have that book')

 

    

