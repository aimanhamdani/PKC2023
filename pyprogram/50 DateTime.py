# import datetime
# x=datetime.datetime.now()
# print(x)
# print('')
# # date and time fixed symbols
# x=datetime.datetime.now()
# m=x.strftime('%B') #%b,B,m,y,Y,H,I,p,M
# print(x)
# print(m)


import datetime
x=datetime.datetime.now()
print(x.strftime('%B'))

from datetime import datetime

date_string = "2023-01-01"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print(date_string)
print(parsed_date)
print('****************')

print(datetime.now().strftime('%H:%M , %Y-%m-%d'))





