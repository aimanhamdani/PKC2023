import random
l=['Rock','Paper','Scissor']
print('''
Rock vs paper->Paper win
Rock vs Scissor->Rock win
Scissor vs Paper->Scissor win
''')
while True:
    #userinput,uchoice,ccount,ucount,Cchoice
    ccount=0
    ucount=0
    uc=int(input('''
    Game Start.....
    1 Yes
    2 No/Exit
    Invalid Choice
    '''))

    if uc==1:
        for a in range(1,6):
            uchoice='' #initialize uchoice with a empty string before using it.
            userinput=int(input('''
            Choose the following
            1 Rock
            2 Scissor
            3 Paper
            '''))
            if userinput==1:
                uchoice='Rock'
            elif userinput==2:
                uchoice='Scissor'
            elif userinput==3:
                uchoice='Paper'
            else:
                print('choose the correct option')

            cchoice=random.choice(l)
            if cchoice==uchoice:
                print('Game Draw...')
                print('Computer Value=',cchoice)
                print('User Value=',uchoice)
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=='Rock' and cchoice=='Scissor')or(uchoice=='Paper' and cchoice=='Rock')or(uchoice=='Scissor' and cchoice=='Paper'):

                print('Computer Value=',cchoice)
                print('User Value=',uchoice)
                print('You Win')
                ucount=ucount+1
            else:
                print('Computer Value=', cchoice)
                print('User Value=', uchoice)
                print('Computer Win')
                ccount=ccount+1

        if ucount==ccount:
            print('Game Draw...')
            print('Total User Score=', ucount)
            print('Total Computer Score=', ccount)
        elif ucount>ccount:
            print('Congratulations! You win the game')
            print('Total User Score=', ucount)
            print('Total Computer Score=', ccount)
        else:
            print('Final Computer win the Game...')
            print('Total User Score=', ucount)
            print('Total Computer Score=', ccount)
    elif uc==2:
        break
    else:
        print('Invalid choice. Please choose 1 or 2')











