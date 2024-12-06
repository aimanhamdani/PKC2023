

# n=input('Enter the Value:-')
# print(n)
# l=n.split()  #split the words single
# print(l)
# # multiple inputs whether number or alpha
# l=[]
# for a in range(1,4):
#     n=input('Enter The Value'+str(a)+':-')
#     print(n)       #string and number never concenate,so, we use str.
#     l.append(n)
#     print(l)
# #
# l=[]
# while True:
#     c=input('''
#     1 Push Elements
#     2 Pop Elements
#     3 Peek Element(show last value)
#     4 Display Stack (Show complete list)
#     5.Exit
#     else is invalid opr
#     ''')
#     if c==1:
#         n=input('Enter The Value')
#         l.append(n)
#         print(l)
#     elif c==2:
#         if len(l)==0:
#             print('Empty Stack')
#         else:
#             p=l.pop()
#             print(p)
#             print(l)
#     elif c==3:
#         if len(l)==0:
#             print('Empty Stack')
#         else:
#             print('Last Stack Value',l[-1])
#     elif c==4:
#         print('Display Stack',l)
#     elif c==5:
#         break
#     else:
#         print('invalid operator')

#         print('Invalid Opr')
# #Queue: it works on fifo.
l=[]
while True:
    c=int(input('''
    1 Enqueue Elements >>>>>>>>>>>>>>>>>>>>>>>>>>>>append
    2 Dequeue (delete/pop First Elements) >>>>>>>>>delete index 0 or first element
    3 Front / First queue Element >>>>>>>>>>>>>>>>>show index 0 or first element
    4 Peak/Rear/last Element >>>>>>>>>>>>>>>>>>>>>>show index -1 or last element
    5 Display Stack >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>show entire list
    6.Exit >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>out from program <break>
    Invalid operations
    '''))
    if c==1:
        n=input('Enter The Value:- ')
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print('Queue is Empty')
        else:
            print(l[0])
            del l[0]
            print(l)
    elif c==3:
        if len(l)==0:
            print('Queue is Empty')
        else:
            print('Front queue Value',l[0])
    elif c==4:
        if len(l)==0:
            print('Queue is Empty')
        else:
            print('Rear/Last queue Element Value',l[-1])
    elif c==5:
        if len(l)==0:
            print('Stack is Empty')
        else:
            print('Display Queue List :-',l)
    elif c==6:
        break
    else:
        print('Invalid Opr, Plesae enter the correct number')




