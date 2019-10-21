a = {'p1,l1':'a','p2,l1':'b','p2,l2':'c'}
b = {'p1,l1':'a','p3,l1':'b','p2,l2':'c'}

for x,y in zip(a,b):
    print(x,y)