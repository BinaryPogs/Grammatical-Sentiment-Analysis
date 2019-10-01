import re
import csv
import os

map_list = []
total_targets_found = 0
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
line_map = {}
path = 'C:\\Users\\Eddie\\Documents\\University\\ISYS358\\resamples\\final\\files\\'
#filename = input('Enter Filename:')
lexxe = open('C:\\Users\\Eddie\\Documents\\University\\ISYS358\\resamples\\final\\files\\000140.ant').read()


paragraphs = re.sub(r'(\n\d\)*)', r'|\1', lexxe).split('|')


# def createParaMap(path_or_file):
#     paragraph_lines = [p.split('\n') for p in paragraphs]
#     paragraph_lines = paragraph_lines[1:] 
#     for lines in paragraph_lines:  
#         para.append(lines)
#     for lines in para:
#         # gets rid of the first two lines as they are unnecessary
#         para_map[lines[1]] = lines[2:]
#     count = 0
#     for i in range(len(para_map)):
#         for k in para_map.keys():
#             if i == count:
#                 count += 1  # changes the key values to 0-len(para_map)
#                 para_map[i] = para_map.pop(k)
#     return para_map 


# def createSourceMap(list):
#     source = [[l.rstrip() for l in p.split('\n') if re.search(r"s\d[-/\d]*", l.rstrip())]
#               for p in paragraphs]  # creates a list that holds each inidividual list of the lines with s# in each distinct paragraph.
#     source = [x for x in source if x != []]  # Remove empty lists
#     for i, item in enumerate(source):
#         s[i] = str(item)  # map the paragraphs and their source lines
#     return s


def count_targets(p):
    count = 0
    for v in p.values():
        for i in v:
            if re.search(r"t\d[-/\d]*", i):
                count += 1
    return count

# p = createParaMap(lexxe)
# s = createSourceMap(p)
# target_count = count_targets(p)

# counter = 0
# for v in p.values():
#     for i, line in enumerate(v):
#         counter+=1
#         print(line, counter)

# for i in s.values():
#     print(i)

def p_map(paragraphs):
    p_map = {}
    line_para_map = {}
    paragraph_lines = [p.split('\n') for p in paragraphs]   
    paragraph_lines = paragraph_lines[1:]
    for i, lines in enumerate(paragraph_lines):
        p_map[i] = lines[3:]
    return p_map

p_map = p_map(paragraphs)

def createSourceMap(p_map):
    paragraph_count = 0 
    line_para_map = {}
    for values in p_map.values():
        paragraph_count+=1
        for i,item in enumerate(values):
            if re.search(r"s\d[-/\d]*", item.rstrip()):
                index = "p:{},l:{}".format(paragraph_count, i)
                line_para_map[index] = item
    return line_para_map

sourcemap = createSourceMap(p_map)
#print(sourcemap)
# print(line_para_map)

#print(p_map)
def createParaLineMap(p_map):
    pline_map = {}
    p_count = 0  
    for values in p_map.values():
        p_count+=1
        for i,item in enumerate(values):
            idx = "p:{},l:{}".format(p_count, i)
            pline_map[idx] = item
    return pline_map

pline_map = createParaLineMap(p_map)

for k,v in sourcemap.items():
    if re.search('amod', v):
        first_word = re.findall(r'amod\(([^-]*)-', v)
        #print(first_word, 'first')
        for k1,v1 in pline_map.items():
            if re.search("nmod:of", v1):
                second_word = re.findall(
                        r'nmod:of\(([^-]*)-', v1.lstrip(' '))
                if k[:4] == k1[:4]:
                    for i in first_word:
                        second_word = re.findall(
                                     '\, (.*?)\-', v1.lstrip(' '))
                        #print(second_word)
                        if second_word == [i]:
                            #print(second_word, 'second')
                            amod_nmod1_map[k1] = second_word, v[-1]
map_list.append('advmod_conjb_map')

for k,v in sourcemap.items():
    if re.search('amod',v):
        first_word = re.findall(r'amod\(([^-]*)-', v)
        for k1,v1 in pline_map.items():
            if re.search("nmod:of", v1):
                     second_word = re.findall(
                        r'nmod:of\(([^-]*)-', v1.lstrip(' '))
            if k[:4] == k1[:4]:
                for i in first_word:
                    if second_word == [i]:
                        second_word = re.findall(
                            '\, (.*?)\-', v1.lstrip(' '))
                        amod_nmod1_map[k1] = second_word, v[-1] #this creates a dict with para+line as keys
                                                                # and target word, target number as values
map_list.append('amod_nmod1_map')

for k, v in sourcemap.items():
    if re.search('advmod',v):
        first_word = re.findall(r'advmod\(([^-]*)-', v)
        for k1,v1 in pline_map.items():
            if re.search('conj:but',v1):
                second_word = re.findall(
                        '\, (.*?)\-', v1.lstrip(' '))
                if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                advmod_conjb_map[k1] = second_word, v[-1] #this creates a dict with para+line as keys
                                                                          # and target word, target number as values
map_list.append('amod_nmod_map')


for i in map_list:
    amod_nmod_map.update(eval(i)) #feeds and combines the list of rule dictionaries into a larger combined one

#amod_nmod_map.update(amod_nmod1_map)
#print(advmod_conjb_map)
targets_marked = open('targetsmarked.txt', 'w+')
for idx,pline in pline_map.items():
    targets_marked.write(pline)
    if amod_nmod_map.get(idx) != None:
        targets_marked.write('t{} \n'.format(amod_nmod_map[idx][1])) ##appends the t# based on s#
    else:
        targets_marked.write('\n')
        
        
 
            
        

# for k,v in pline_map.items():
#     print(k,v)
    


# for k,v in pline_map.items():
#     print(k,v)

# for values in p_map.values():
#     #p_count+=1
#     for i,item in enumerate(values):
#         print(item)

# print(sourcemap)
# print(pline_map)