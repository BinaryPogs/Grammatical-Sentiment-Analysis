import re

s = dict()
s_map = dict()
amod = dict()
first_word = ''
second_word = ''
amodlist = []
para = []
target = []
lexxe = open('000140.ant').read()
paragraphs = re.sub(r'(\n\d\)*)', r'|\1', lexxe).split('|')
source = [[l.rstrip() for l in p.split('\n') if re.search(r's\d$', l.rstrip())]
          for p in paragraphs]  # creates a list that holds each inidividual list of the lines with s# in each distinct paragraph.
source = [x for x in source if x != []]  # Remove empty lists

paragraph_lines = [p.split('\n') for p in paragraphs]
paragraph_lines = paragraph_lines[1:]
for lines in paragraph_lines:
    # lines = list(filter(lambda i: i != 'Neutral.', lines))
    if not 'Neutral.' in lines:  # gets rid of the paragraphs with Neutral. marked
        para.append(lines)

for i, item in enumerate(source):
    s[i] = str(item)  # map the paragraphs and their source lines
# print(s)


# for i, item in enumerate(para):
# for k, v in s.items():
# if i == k:
# print(str(v))
# for words in v:
# if re.search('^amod', words):
# print(words)

# x = re.findall('\((.*?)\-', str(v))
# print(x)

for k, v in s.items():
    for w, words in enumerate(v):
        if re.search('^amod', words):
            x = re.findall('\((.*?)\-', words)
            amodlist.append(x)  # changes to a list of amod's first words


for i, item in enumerate(amodlist):
    amod[i] = item  # dictionary to indicate which paragraph the sources are in

for lines in para:
    s_map[lines[1]] = lines[2:]

count = 0
for i in range(len(s_map)):
    for k, v in s_map.items():
        if i == count:
            count += 1
            s_map[i] = s_map.pop(k)

# print(s_map)
# print(s_map)
# print(amodlist)
for k, v in s.items():
    if re.search('^amod', v.lstrip("['")):
        first_word = re.findall('\((.*?)\-', v)
        print('this is the first word(s)', first_word, 'in paragraph', k)
        for k1, v1 in s_map.items():
            for word in v1:
                if re.search("^nmod", word):
                    if k == k1:
                        second_word = re.findall(
                            '\, (.*?)\-', word.lstrip(' '))
                        print('this is the second word in nmod:',
                              second_word, 'in paragraph', k1)
                        if first_word == second_word:
                            target.append(first_word)


# print(target)
# if first_word == second_word:
# target.append(first_word)

# print(s.items())
