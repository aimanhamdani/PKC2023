#if you want a value in string then u can set it.
#when we want to format a data and to show in comand.
#any value can use in string
#define with{} curly bracket

#how to format string
a="The error you're encountering {a:^20} is likely due to Python not finding the my_functions {c} module. To resolve " \
  "this," \
  "\ ensure that the my_functions.py {b} file is in the same directory {d} as your 1practice.py file, and {e} then " \
  "follow ," \
  "the steps outlined below:"
print(a.format(a="-1",e=5,c=3,d=4,b=2))
b=a.format(a="-1",e=5,c=3,d=4,b=2)
print(b)
print('-----------------------------------------1')
w='Welcome {} to {} Wscubetech'.format('hello',20);
print(w)
print('-------------------------------2')
w='Welcome {1} to {0} Wscubetech'.format('hello',20);
print(w)
w='Welcome {a} to {b} Wscubetech'.format(b=30,a=40);
print(w)
#if we want to give space in characters
#>10=give space in right side
#<10=give space in left side
#^10=both sides equal spacing 5left side and 5right side.
w='Welcome{a:^10} to {b:<10}Wscubetech'.format(a=20,b=40);
print(w)

k='It {a:^20} is {b:<20} very {c:>20} shiny {d} day'.format(a='USA',b=20,c=22,d='qatar')
print(k)

z='It {:^20} is {:<20} very {:>20} shiny {} day'.format('USA',30,22,'qatar')
print(z)
l= 'a {h:^10}quick {g:^10}brown {f:^10}fox {e:^10}jumps {d:^10}over {c:^10}the {b:^10}lazy {a:^10}dog'.format(a='1',b=2,
                                                                                                           c="three",
                                                                                                    d='iv',e=5,f='six',\
  g='saat',h=8)
print(l)