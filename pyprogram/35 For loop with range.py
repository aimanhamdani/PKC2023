# range(5)
# #start=0
# #condition<5
# #increment 1
# # 0,1,2,3,4
# range(1,6)
# # start=1
# # condition<6
# # increment 1
# # 1,2,3,4,5
# range(1,6,2)
# # start=1
# # condition<5
# # increment 2
# # 1,3,5
# #
# for n in range(5):
#     print('Welcome',end='')
# print()
# for n in range(1,6):
#      print(n,end='')
# # # # # #
# # for n in range(1,6,2):
# #     print(n)
# print('Table of 2')
# for a in range(1,11):
#     print('2 X', a, '=', 2*a)
# # # #2 table to print
# # #
# # for a in range(1,11):
# #     print('2*',a,'=',2*a)
# # # # #
# for r in range(10,0,-1):
#     print(r)
# # #
# for n in range(10,-1,-2):
#     print(n)
# for a in range(1,11):
#     print('19 X',a,'=',19*a)
# for a in range(10,0,-1):
#
#     print('16 X',a,'=',16*a)
#if we want 12345 in sequence and 5times then;
for i in range(1,6):
    for j in range(1,6,1):
        print(j,end='')

    print()
print('--'*20)
# #if we want 1111,2222,3333,4444,5555 then print i;
for i in range(1,6):
    for j in range(1,6,1):
        print(i,end='')
    print()
#
#
print('---------------reverse patern')
# #if we want to print reverse patern values than.
for i in range(1,6):
    for j in range(5,0,-1):
        print(j,end='')
    print()
print('--------------------------increment each line')
#if i want to increment in 5lines from 1 to 5 each line:
for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(j,end='')
    print()
print('------------------decrement each line 54321')
#if i want to decrement each line from 54321 to 1 than;
for i in range(1,6,1):
    for j in range(5,i-1,-1):
        print(j,end='')
    print()
print('----------------------------decrement 11111,2222...')
#if i want decrement of 11111,22222...55555 than;
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(i,end='')
    print()