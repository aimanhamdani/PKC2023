#Number guessing game python project
#by using random module
#Senorio: User input compare with computer by using comparision opr..
#=,>,<
import random
while True:
    ccount = 0
    ucount = 0
    print('''
    press 1 to start the game
    press 2 to exit game
    ''')
    user_choice=int(input('enter the value= '))
    if user_choice==1:
        for a in range(1,3):
            UserInput=int(input('Enter the guess number= '+str(a)+'='))
            Cnumber = random.randrange(1, 101)
            if Cnumber>UserInput:
                print('Computer Number:- ',Cnumber)
                print('Your guess is low & Computer Win')
                ccount=ccount+1
            elif Cnumber<UserInput:
                print('Computer Number:- ',Cnumber)
                print('Your guess is High & You Win')
                ucount=ucount+1
            else:
                print('Draw')
                ccount=ccount+1
                ucount=ucount+1
        if ccount==ucount:
            print('Final Computer score=',ccount)
            print('Final User score=',ucount)
            print('Finally Game Draw')
        elif ccount<ucount:
            print('Final User score=',ucount)
            print('Final Computer score=',ccount)
            print('Finally You win')
        else:
            print('Finally computer win')
            print('Final Computer score=',ccount)
            print('Final User score=',ucount)
    elif user_choice==2:
        break
    else:
        print('invalid entry')

#Incomplete.


