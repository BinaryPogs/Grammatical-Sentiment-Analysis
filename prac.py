import re
x = 5
s = '{} hi'.format(x)

if s in '5 hi':
    print('yes')

l = 't1'
if re.search('t[0-9]$', l):
    print('ok')
    
print(re.search('t[0-9]$',l)[0])