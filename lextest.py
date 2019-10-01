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
lexxe = open('C:\\Users\\Eddie\\Documents\\University\\ISYS358\\resamples\\final\\files\\anttest.ant').read()


paragraphs = re.sub(r'(\n\d\)*)', r'|\1', lexxe).split('|')

def p_map(paragraphs): #This creates a paragraph dictionary with the key being the paragraph # 
    p_map = {}         #and the values being the lines in the paragraph
    line_para_map = {}
    paragraph_lines = [p.split('\n') for p in paragraphs]   
    paragraph_lines = paragraph_lines[1:]
    for i, lines in enumerate(paragraph_lines):
        p_map[i] = lines[3:]
    return p_map



def createSourceMap(p_map): #This creates a source dictionary
    paragraph_count = 0     #with the key being the paragraph# and line#
    line_para_map = {}      #and the values being the source words
    for values in p_map.values():
        paragraph_count+=1
        for i,item in enumerate(values):
            if re.search(r"s\d[-/\d]*", item.rstrip()):
                index = "p:{},l:{}".format(paragraph_count, i)
                line_para_map[index] = item
    return line_para_map



def createParaLineMap(p_map): ##Uses the p_map to create a para_line map which 
    pline_map = {}            ##identifies which paragraph# and line# each paragraph is on
    p_count = 0  
    for values in p_map.values():
        p_count+=1
        for i,item in enumerate(values):
            idx = "p:{},l:{}".format(p_count, i)
            pline_map[idx] = item
    return pline_map



def count_targets(p):
    count = 0
    for v in p.values():
        for i in v:
            if re.search(r"t\d[-/\d]*", i):
                count += 1
    return count

p_map = p_map(paragraphs)
sourcemap = createSourceMap(p_map)
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
                        if second_word == [i]:
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


for k, v in sourcemap.items():
    if re.search('amod',v):
        first_word = re.findall(r'amod\(([^-]*)-', v)
        for k1,v1 in pline_map.items():
            if re.search("^nmod:in", v1):
                    second_word = re.findall(
                        '\, (.*?)\-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                amod_nmodin_map[k1] = second_word, v[-1]
map_list.append('amod_nmodin_map')

for k, v in sourcemap.items():
    if re.search('amod',v):
        first_word = re.findall(r'amod\(([^-]*)-',v)
        for k1,v1 in pline_map.items():
            if re.search('root',v1):
                second_word = re.findall(
                        '\, (.*?)\-', v1.lstrip(' '))
            if k[:4] == k1[:4]:
                for i in first_word:
                    if second_word == [i]:
                        amod_root_map[k1] = second_word, v[-1]
map_list.append('amod_root_map')
            
for k, v in sourcemap.items():
    if re.search('amod', v):
        first_word = re.findall(r'amod\(([^-]*)-', v)
        # print('this is the first word(s)', first_word, 'in paragraph', k)
        for k1, v1 in pline_map.items():
                if re.search("dobj", v1):
                    second_word = re.findall(
                        '\, (.*?)\-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                amod_dobj_map[k1] = second_word, v[-1]
map_list.append('amod_dobj_map')

for k, v in sourcemap.items():
    if re.search('amod', v):
        first_word = re.findall(r'amod\(([^-]*)-', v)
        for k1, v1 in pline_map.items():
                if re.search("acl:relcl", v1):
                    second_word = re.findall(
                        r'acl:relcl\(([^-]*)-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                amod_aclrel_map[k1] = second_word, v[-1]
map_list.append('amod_aclrel_map')

for k, v in sourcemap.items():
    if re.search('advmod', v):
        v = str(re.findall("(?<=advmod\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v)
        for k1, v1 in pline_map.items():
                if re.search("nmod:to", v1):
                    second_word = re.findall(r'nmod:to\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                advmod_nmod_map[k1] = second_word, v1[-1]
map_list.append('advmod_nmod_map')
for i in map_list:
    amod_nmod_map.update(eval(i)) #feeds and combines the list of rule dictionaries into a larger combined one


        
targets_marked = open('targetsmarked.txt', 'w+')
for idx,pline in pline_map.items():
    targets_marked.write(pline)
    if amod_nmod_map.get(idx) != None and ('t{}'.format(amod_nmod_map[idx][1]) not in pline):
        targets_marked.write('t{} \n'.format(amod_nmod_map[idx][1])) ##appends the t# based on s#
    else:
        targets_marked.write('\n') ## if it's just a normal line, new line and continue printing text

