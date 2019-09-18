import re
import csv
import os

para = []
target = []
para_map = {}
s = {}
amod_nmod_map = {}
amod_nmod1_map = {}
amod_root_map = {}
amod_dobj_map = {}
advmod_nmod_map = {}
amod_nmodin_map = {}
amod_aclrel_map = {}
neg_nmodas_map = {}
root_dobj_map = {}
cop_nmodas_map = {}
advmod_conjb_map = {}
conjb_nmodas_map = {}
root_xcomp_map = {}
advcl_dobj_map = {}
path = 'C:\\Users\\Eddie\\Documents\\University\\ISYS358\\resamples\\final\\files\\'
filename = input('Enter Filename:')
lexxe = open(path + filename).read()


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


p = createParaMap(lexxe)


def count_targets(p):
    count = 0
    for k, v in p.items():
        for i in v:
            if re.search(r"t\d[-/\d]*", i):
                count += 1
    print(count)


count_targets(p)
