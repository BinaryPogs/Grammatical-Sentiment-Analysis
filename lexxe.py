import re
import itertools

first_word = ''
second_word = ''
rules = list()
hand = open('000140.ant')
for line in hand:
    line = line.rstrip()
    if re.search('s[0-9]$', line):
        rules.append(line)

for a, b in itertools.combinations(rules, 2):
    if re.search('^amod', a) and re.search('^nmod', b):
        first_word = re.findall('\((.*?)\-', a)
        # print(first_word)
        second_word = re.findall('\, (.*?)\-', b)
        # print(second_word)
        print(a, b)

        # print(a[5:10])
