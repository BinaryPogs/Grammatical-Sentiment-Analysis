import re
import itertools

first_word = ''
second_word = ''
source = list()
words = list()
lexxe = open('000140.ant')
for line in lexxe:
    line = line.rstrip()
    if re.search('s[0-9]$', line):
        source.append(line)
print(source)
for line in lexxe:
    line = line.rstrip()
    if not re.search('s[0-9]$', line):
        words.append(line)
print(words)
# for a, b in itertools.combinations(source, 2):
# if re.search('^amod', a) and re.search('^nmod', b):
#first_word = re.findall('\((.*?)\-', a)
# print(first_word)
#second_word = re.findall('\, (.*?)\-', b)
# print(second_word)
#print(a, b)
