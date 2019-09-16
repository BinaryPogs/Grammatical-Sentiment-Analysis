import itertools
mylist = [1, 2, 3, 4, 5, 1]
for a, b in itertools.combinations(mylist, 2):
    print(a, b)
