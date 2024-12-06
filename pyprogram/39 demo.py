# import random
#
# l = ['Rock', 'Paper', 'Scissor']
#
# while True:
#     ccount = 0
#     ucount = 0
#
#     uc = int(input('''
#     Game Start.....
#     1 Yes
#     2 No/Exit
#     '''))
#
#     if uc == 1:
#         for a in range(1, 6):
#             userinput = int(input('''
#             Choose the following
#             1 Rock
#             2 Scissor
#             3 Paper
#             '''))
#             if userinput == 1:
#                 uchoice = 'Rock'
#             elif userinput == 2:
#                 uchoice = 'Scissor'
#             elif userinput == 3:
#                 uchoice = 'Paper'
#             else:
#                 print('invalid entry')
#                 continue
#
#             cchoice = random.choice(l)
#
#             if cchoice == uchoice:
#                 print('Game Draw...')
#                 print('Computer Choice', cchoice)
#                 print('User Choice', uchoice)
#                 ucount +=1
#                 ccount +=1
#             elif (uchoice == 'Rock' and cchoice == 'Scissor') or \
#                  (uchoice == 'Paper' and cchoice == 'Rock') or \
#                  (uchoice == 'Scissor' and cchoice == 'Paper'):
#                 print('User Value', uchoice)
#                 print('Computer Value', cchoice)
#                 print('You Win')
#                 ucount += 1
#             else:
#                 print('Computer Value', cchoice)
#                 print('User Value', uchoice)
#                 print('Computer Win')
#                 ccount += 1
#
#         if ucount == ccount:
#             print('Game Draw...')
#             print('User Value', ucount)
#             print('Computer Value', ccount)
#         elif ucount > ccount:
#             print('You Win...')
#             print('User Value', ucount)
#             print('Computer Value', ccount)
#         else:
#             print('Final Computer wins the Game...')
#             print('User Score', ucount)
#             print('Computer Score', ccount)
#     elif uchoice==2:
#         break
#     else:
#         print('invalid entry')

import random

l = ['Rock', 'Paper', 'Scissor']

while True:
    ccount = 0
    ucount = 0

    uc = int(input('''
    Game Start.....
    1 Yes
    2 No/Exit
    '''))

    if uc == 1:
        for a in range(1, 6):
            userinput = int(input('''
            Choose the following
            1 Rock
            2 Scissor
            3 Paper
            '''))
            if userinput == 1:
                uchoice = 'Rock'
            elif userinput == 2:
                uchoice = 'Scissor'
            elif userinput == 3:
                uchoice = 'Paper'
            else:
                print('invalid entry')
                continue

            cchoice = random.choice(l)

            if cchoice == uchoice:
                print('Game Draw...')
                print('Computer Choice', cchoice)
                print('User Choice', uchoice)
                ucount += 1
                ccount += 1
            elif (uchoice == 'Rock' and cchoice == 'Scissor') or \
                 (uchoice == 'Paper' and cchoice == 'Rock') or \
                 (uchoice == 'Scissor' and cchoice == 'Paper'):
                print('User Value', uchoice)
                print('Computer Value', cchoice)
                print('You Win')
                ucount += 1
            else:
                print('Computer Value', cchoice)
                print('User Value', uchoice)
                print('Computer Wins')
                ccount += 1

        if ucount == ccount:
            print('Game Draw...')
            print('User Value', ucount)
            print('Computer Value', ccount)
        elif ucount > ccount:
            print('You Win...')
            print('User Value', ucount)
            print('Computer Value', ccount)
        else:
            print('Final Computer wins the Game...')
            print('User Score', ucount)
            print('Computer Score', ccount)
    elif uc == 2:
        break
    else:
        print('Invalid entry')
