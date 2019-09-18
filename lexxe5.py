import re

para = []
target = []
para_map = {}
s = {}
amod_nmod_map = {}
amod_root_map = {}
amod_dobj_map = {}
advmod_nmod_map = {}
amod_nmodin_map = {}
amod_aclrel_map = {}
neg_nmodas_map = {}
root_dobj_map = {}
filename = input('Enter Filename:')
lexxe = open(filename).read()


paragraphs = re.sub(r'(\n\d\)*)', r'|\1', lexxe).split('|')


def createParaMap(path_or_file):
    paragraph_lines = [p.split('\n') for p in paragraphs]
    paragraph_lines = paragraph_lines[1:]
    for lines in paragraph_lines:
        if not 'Neutral.' in lines:  # gets rid of the paragraphs with Neutral. marked
            para.append(lines)
    for lines in para:
        # gets rid of the first two lines as they are unnecessary
        para_map[lines[1]] = lines[2:]
    count = 0
    for i in range(len(para_map)):
        for k, v in para_map.items():
            if i == count:
                count += 1  # changes the key values to 0-len(para_map)
                para_map[i] = para_map.pop(k)
    return para_map


def createSourceMap(list):
    source = [[l.rstrip() for l in p.split('\n') if re.search(r"s\d[-/\d]*", l.rstrip())]
              for p in paragraphs]  # creates a list that holds each inidividual list of the lines with s# in each distinct paragraph.
    source = [x for x in source if x != []]  # Remove empty lists
    for i, item in enumerate(source):
        s[i] = str(item)  # map the paragraphs and their source lines
    return s


p = createParaMap(lexxe)
s = createSourceMap(p)


# The code below checks for the amod rule, if the first and second word of
#  the same paragraph are the same, then the word is the target.

for k, v in s.items():
    if re.search('amod', v):
        first_word = re.findall(r'amod\(([^-]*)-', v)
        # print('this is the first word(s)', first_word, 'in paragraph', k)
        for k1, v1 in p.items():
            for word in v1:
                if re.search("^nmod:of", word):
                    second_word = re.findall(
                        '\, (.*?)\-', word.lstrip(' '))
                    # print('this is the second word in nmod:',
                    # second_word, 'in paragraph', k1)
                    if k == k1:
                        for i in first_word:
                            if second_word == [i]:
                                amod_nmod_map[k+1] = second_word

for k, v in s.items():
    if re.search('amod', v):
        first_word = re.findall(r'amod\(([^-]*)-', v)
        # print('this is the first word(s)', first_word, 'in paragraph', k)
        for k1, v1 in p.items():
            for word in v1:
                if re.search("^nmod:in", word):
                    second_word = re.findall(
                        '\, (.*?)\-', word.lstrip(' '))
                    # print('this is the second word in nmod:',
                    # second_word, 'in paragraph', k1)
                    if k == k1:
                        for i in first_word:
                            if second_word == [i]:
                                amod_nmodin_map[k+1] = second_word

for k, v in s.items():
    if re.search('amod', v):
        first_word = re.findall(r'amod\(([^-]*)-', v)
        # print('this is the first word(s)', first_word, 'in paragraph', k)
        for k1, v1 in p.items():
            for word in v1:
                if re.search("^root", word):
                    second_word = re.findall(
                        '\, (.*?)\-', word.lstrip(' '))
                    # print('this is the second word in nmod:',
                    # second_word, 'in paragraph', k1)
                    if k == k1:
                        for i in first_word:
                            if second_word == [i]:
                                amod_root_map[k+1] = second_word

for k, v in s.items():
    if re.search('amod', v):
        first_word = re.findall(r'amod\(([^-]*)-', v)
        # print('this is the first word(s)', first_word, 'in paragraph', k)
        for k1, v1 in p.items():
            for word in v1:
                if re.search("^dobj", word):
                    second_word = re.findall(
                        '\, (.*?)\-', word.lstrip(' '))
                    # print('this is the second word in nmod:',
                    # second_word, 'in paragraph', k1)
                    if k == k1:
                        for i in first_word:
                            if second_word == [i]:
                                amod_dobj_map[k+1] = second_word

for k, v in s.items():
    if re.search('amod', v):
        first_word = re.findall(r'amod\(([^-]*)-', v)
        # print('this is the first word(s)', first_word, 'in paragraph', k)
        for k1, v1 in p.items():
            for word in v1:
                if re.search("^acl:relcl", word):
                    second_word = re.findall(
                        r'acl:relcl\(([^-]*)-', word.lstrip(' '))
                    # print('this is the second word in acl:relcl',
                    # second_word, 'in paragraph', k1)
                    if k == k1:
                        for i in first_word:
                            if second_word == [i]:
                                amod_aclrel_map[k+1] = second_word

for k, v in s.items():
    if re.search('advmod', v):
        v = str(re.findall("(?<=advmod\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v)
        # print('this is the first word(s)', first_word, 'in paragraph', k)
        for k1, v1 in p.items():
            for word in v1:
                if re.search("^nmod:to", word):
                    second_word = re.findall(r'nmod:to\(([^-]*)-',
                                             word.lstrip(' '))
                    # print('this is the second word in nmod:',
                    # second_word, 'in paragraph', k1)
                    if k == k1:
                        for i in first_word:
                            if second_word == [i]:
                                advmod_nmod_map[k+1] = second_word


for k, v in s.items():
    if re.search("neg", v):
        first_word = re.findall(r'neg\(([^-]*)-', v)
       # print('this is the first word(s)', first_word, 'in paragraph', k)
        for k1, v1 in p.items():
            for word in v1:
                if re.search('nmod:as', word):
                    second_word = re.findall(
                        r'nmod:as\(([^-]*)-', word.lstrip(' '))
                   # print('this is the second word in nmod:as',
                    # second_word, 'in paragraph', k1)
                    if k == k1:
                        for i in first_word:
                            if second_word == [i]:
                                neg_nmodas_map[k+1] = second_word

for k, v in s.items():
    if re.search("root", v):
        v = str(re.findall("(?<=root\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v)
        #print('this is the first word(s)', first_word, 'in paragraph', k)
        for k1, v1 in p.items():
            for word in v1:
                if re.search("dobj", word):
                    second_word = re.findall(r'dobj\(([^-]*)-',
                                             word.lstrip(' '))
                    # print('this is the second word in nmod:',
                    # second_word, 'in paragraph', k1)
                    if k == k1:
                        for i in first_word:
                            if second_word == [i]:
                                root_dobj_map[k+1] = second_word

print('='*100)
for k, v in amod_nmod_map.items():
    print('The target', v, 'was found in paragraph',
          k, 'using the amod-nmod:of relationship')
print('='*100)  # separator for tidiness

for k, v in amod_root_map.items():
    print('The target', v, 'was found in paragraph',
          k, 'using the amod-root relationship')
print('='*100)

for k, v in amod_dobj_map.items():
    print('The target', v, 'was found in paragraph',
          k, 'using the amod-dobj relationship')
print('='*100)

for k, v in advmod_nmod_map.items():
    print('The target', v, 'was found in paragraph',
          k, 'using the advmod-nmod:to relationship')
print('='*100)

for k, v in amod_nmodin_map.items():
    print('The target', v, 'was found in paragraph',
          k, 'using the advmod-nmod:in relationship')
print('='*100)

for k, v in amod_aclrel_map.items():
    print('The target', v, 'was found in paragraph',
          k, 'using the amod-acl:relcl relationship')
print('='*100)

for k, v in neg_nmodas_map.items():
    print('The target', v, 'was found in paragraph',
          k, 'using the neg-nmodas relationship')
print('='*100)

for k, v in root_dobj_map.items():
    print('The target', v, 'was found in paragraph',
          k, 'using the root-dobj relationship')
print('='*100)
