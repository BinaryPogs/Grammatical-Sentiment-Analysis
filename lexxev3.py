import re

s = dict()
para_map = dict()
amod = dict()
first_word = ''
second_word = ''
amodlist = []
para = []
target = []

filename = input('Enter Filename:')
lexxe = open(filename).read()


paragraphs = re.sub(r'(\n\d\)*)', r'|\1', lexxe).split('|')


def createPara(path_or_file):
    paragraph_lines = [p.split('\n') for p in paragraphs]
    paragraph_lines = paragraph_lines[1:]
    for lines in paragraph_lines:
        if not 'Neutral.' in lines:  # gets rid of the paragraphs with Neutral. marked
            para.append(lines)
    for lines in para:
        para_map[lines[1]] = lines[2:]
    count = 0
    for i in range(len(para_map)):
        for k, v in para_map.items():
            if i == count:
                count += 1
                para_map[i] = para_map.pop(k)
    return para_map


def createSourceMap(list):
    source = [[l.rstrip() for l in p.split('\n') if re.search(r's\d$', l.rstrip())]
              for p in paragraphs]  # creates a list that holds each inidividual list of the lines with s# in each distinct paragraph.
    source = [x for x in source if x != []]  # Remove empty lists
    for i, item in enumerate(source):
        s[i] = str(item)  # map the paragraphs and their source lines
    return s


p = createPara(lexxe)
s = createSourceMap(p)

# The code below checks for the amod rule, if the first and second word of
#  the same paragraph are the same, then the word is the target.
for k, v in s.items():
    if re.search('^amod', v.lstrip("['")):
        first_word = re.findall('\((.*?)\-', v)
        print('this is the first word(s)', first_word, 'in paragraph', k)
        for k1, v1 in p.items():
            for word in v1:
                if re.search("^nmod", word):
                    if k == k1:
                        second_word = re.findall(
                            '\, (.*?)\-', word.lstrip(' '))
                        print('this is the second word in nmod:',
                              second_word, 'in paragraph', k1)
                        # if first_word == second_word:
                        # target.append(first_word)
