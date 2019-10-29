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
compound_appos_map = {}
conj_nsubj_map = {}
xcomp_dobj_map = {}
xcomp_xsubj_map = {}
ccomp_iobj_map = {}
conj_dobj_map = {}
ccomp_nsubj = {}
ccomp_xcomp = {}
nmodb_nmodp = {}
advcl_dobj = {}
acl_dobj = {}
acl_nsubj = {}
acl_nmodw = {}
advcl_nsubj = {}
xcomp_nsubj = {}
amod_nmodf = {}
nsubj_nmod = {}
root_nsubj = {}
advmod_amod = {}
amod_nmodf = {}
advmod_root = {}
acl_nsubjp = {}
nmod_nsubjpass = {}
conja_advcl = {}
acl_dobj={}
neg_nsubj ={}
appos_nsubj = {}
xcomp_nsubj = {}
xcomp_nsubj = {}
acl_nsubj = {}
line_map = {}
path = 'C:\\Users\\Eddie\\Documents\\University\\ISYS358\\resamples\\final\\files\\'
filename = input('Enter Filename:')
lexxe = open(path + filename).read()


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

def print_progress_bar(iteration, total, prefix="", suffix="", length=30, fill="=", head=">", track="."):
    filled_length = int(length * iteration // total)
    if filled_length == 0:
        bar = track * length
    elif filled_length == 1:
        bar = head + track * (length - 1)
    elif filled_length == length:
        bar = fill * filled_length
    else:
        bar = fill * (filled_length-1) + ">" + "." * (length-filled_length)
    print("\r" + prefix + "[" + bar + "] " + str(iteration) + "/" + str(total), suffix, end = "\r")
    if iteration == total: 
        print()

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
target_count = count_targets(p_map)

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
                            amod_nmod1_map[k1] = second_word, v.rstrip()[-1]

map_list.append('amod_nmod_map')

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
                        amod_nmod1_map[k1] = second_word, v.rstrip()[-1] #this creates a dict with para+line as keys
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
                                advmod_conjb_map[k1] = second_word, v.rstrip()[-1] #this creates a dict with para+line as keys
                                                                          # and target word, target number as values
map_list.append('advmod_conjb_map')


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
                                amod_nmodin_map[k1] = second_word, v.rstrip()[-1]

map_list.append('amod_nmodin_map')

for k, v in sourcemap.items():
    if re.search('amod',v):
        first_word = re.findall(r'amod\(([^-]*)-', v)
        for k1,v1 in pline_map.items():
            if re.search("root", v1):
                    second_word = re.findall(
                        '\, (.*?)\-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                amod_root_map[k1] = second_word, v.rstrip()[-1]

map_list.append('amod_root_map')
            
for k, v in sourcemap.items():
    if re.search('amod',v):
        first_word = re.findall(r'amod\(([^-]*)-', v)
        for k1,v1 in pline_map.items():
            if re.search("dobj", v1):
                    second_word = re.findall(
                        '\, (.*?)\-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                amod_dobj_map[k1] = second_word, v.rstrip()[-1]
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
                                amod_aclrel_map[k1] = second_word, v.rstrip()[-1]
map_list.append('amod_aclrel_map')

for k, v in sourcemap.items():
    if re.search('advmod', v):
        v2 = str(re.findall("(?<=advmod\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("nmod:to", v1):
                    second_word = re.findall(r'nmod:to\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                advmod_nmod_map[k1] = second_word, v.rstrip()[-1]
map_list.append('advmod_nmod_map')

for k, v in sourcemap.items():
    if re.search("neg", v):
        first_word = re.findall(r'neg\(([^-]*)-', v)
        for k1, v1 in pline_map.items():
                if re.search('nmod:as',v1):
                    second_word = re.findall(
                        r'nmod:as\(([^-]*)-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-', v1)
                                neg_nmodas_map[k1] = second_word, v.rstrip()[-1]

map_list.append('neg_nmodas_map')

for k, v in sourcemap.items():
    if re.search("root", v):
        v2 = str(re.findall("(?<=root\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("dobj", v1):
                    second_word = re.findall(r'dobj\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4]== k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-', v1)
                                root_dobj_map[k1] = second_word, v.rstrip()[-1]
map_list.append('root_dobj_map')

for k, v in sourcemap.items():
    if re.search("cop", v):
        first_word = re.findall(r'cop\(([^-]*)-', v)
        for k1, v1 in pline_map.items():
                if re.search('nmod:as', v1):
                    second_word = re.findall(
                        r'nmod:as\(([^-]*)-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-', v1)
                                cop_nmodas_map[k1] = second_word, v.rstrip()[-1]
map_list.append('cop_nmodas_map')

for k, v in sourcemap.items():
    if re.search("conj:but", v):
        v2 = str(re.findall("(?<=conj:but\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2) 
        for k1, v1 in pline_map.items():
                if re.search('nmod:with', v1):
                    second_word = re.findall(r'nmod:with\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-', v1)
                                conjb_nmodas_map[k1] = second_word, v.rstrip()[-1]

map_list.append('conjb_nmodas_map')

for k, v in sourcemap.items():
    if re.search("root", v):
        v2 = str(re.findall("(?<=root\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2) 
        for k1, v1 in pline_map.items():
                if re.search('xcomp', v1):
                    second_word = re.findall(r'xcomp\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-', v1)
                                root_xcomp_map[k1] = second_word, v.rstrip()[-1]

map_list.append('root_xcomp_map')

for k, v in sourcemap.items():
    if re.search("advcl", v):
        v2 = str(re.findall("(?<=advcl\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("dobj", v1):
                    second_word = re.findall(
                        r'dobj\(([^-]*)-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                advcl_dobj_map[k1] = second_word, v.rstrip()[-1]

map_list.append('advcl_dobj_map')

for k, v in sourcemap.items():
    if re.search('compound',v):
        first_word = re.findall(r'compound\(([^-]*)-', v)
        for k1,v1 in pline_map.items():
            if re.search("appos", v1):
                    second_word = re.findall(
                        '\, (.*?)\-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                compound_appos_map[k1] = second_word, v.rstrip()[-1]
map_list.append('compound_appos_map')

for k, v in sourcemap.items():
    if re.search("conj:and", v):
        v2 = str(re.findall("(?<=conj:and\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1,v1 in pline_map.items():
            if re.search("nsubj", v1):
                    second_word = re.findall(
                        r'nsubj\(([^-]*)-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                conj_nsubj_map[k1] = second_word, v.rstrip()[-1]
map_list.append('conj_nsubj_map')

for k, v in sourcemap.items():
    if re.search('xcomp', v):
        v2 = str(re.findall("(?<=xcomp\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("dobj", v1):
                    second_word = re.findall(r'dobj\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                xcomp_dobj_map[k1] = second_word, v.rstrip()[-1]
map_list.append('xcomp_dobj_map')

for k, v in sourcemap.items():
    if re.search('xcomp', v):
        v2 = str(re.findall("(?<=xcomp\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("nsubj:xsubj", v1):
                    second_word = re.findall(r'nsubj:xsubj\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                xcomp_xsubj_map[k1] = second_word, v.rstrip()[-1]
map_list.append('xcomp_xsubj_map')

for k, v in sourcemap.items():
    if re.search('ccomp', v):
        v2 = str(re.findall("(?<=ccomp\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("iobj", v1):
                    second_word = re.findall(r'iobj\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                xcomp_xsubj_map[k1] = second_word, v.rstrip()[-1]
map_list.append('ccomp_iobj_map')

for k, v in sourcemap.items():
    if re.search('conj:but', v):
        v2 = str(re.findall("(?<=conj:but\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("dobj", v1):
                    second_word = re.findall(r'dobj\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                conj_dobj_map[k1] = second_word, v.rstrip()[-1]
map_list.append('conj_dobj_map')

for k, v in sourcemap.items():
    if re.search('ccomp', v):
        v2 = str(re.findall("(?<=ccomp\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("nsubj", v1):
                    second_word = re.findall(r'nsubj\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                ccomp_nsubj[k1] = second_word, v.rstrip()[-1]
map_list.append('ccomp_nsubj')

for k, v in sourcemap.items():
    if re.search('ccomp', v):
        v2 = str(re.findall("(?<=ccomp\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("xcomp", v1):
                    second_word = re.findall(r'xcomp\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                ccomp_xcomp[k1] = second_word, v.rstrip()[-1]
map_list.append('ccomp_xcomp')

for k, v in sourcemap.items():
    if re.search('nmod:but', v):
        v2 = str(re.findall("(?<=nmod:but\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("nmod:poss", v1):
                    second_word = re.findall(r'nmod:poss\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                nmodb_nmodp[k1] = second_word, v.rstrip()[-1]
map_list.append('nmodb_nmodp')

for k, v in sourcemap.items():
    if re.search("advcl", v):
        first_word = re.findall(r'advcl\(([^-]*)-', v)
        for k1, v1 in pline_map.items():
                if re.search('dobj',v1):
                    second_word = re.findall(
                        r'dobj\(([^-]*)-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-', v1)
                                advcl_dobj[k1] = second_word, v.rstrip()[-1]

map_list.append('advcl_dobj')


for k, v in sourcemap.items():
    if re.search('acl:relcl', v):
        v2 = str(re.findall("(?<=acl:relcl\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("dobj", v1):
                    second_word = re.findall(r'dobj\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                acl_dobj[k1] = second_word, v.rstrip()[-1]
map_list.append('acl_dobj')


for k, v in sourcemap.items():
    if re.search('acl:relcl', v):
        v2 = str(re.findall("(?<=acl:relcl\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("nmod:with", v1):
                    second_word = re.findall(r'nmod:with\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                acl_nmodw[k1] = second_word, v.rstrip()[-1]
map_list.append('acl_nmodw')


for k, v in sourcemap.items():
    if re.search('advcl', v):
        v2 = str(re.findall("(?<=advcl\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("nsubj", v1):
                    second_word = re.findall(r'nsubj\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                advcl_nsubj[k1] = second_word, v.rstrip()[-1]
map_list.append('advcl_nsubj')

for k, v in sourcemap.items():
    if re.search('xcomp', v):
        v2 = str(re.findall("(?<=xcomp\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("nsubj:xsubj", v1):
                    second_word = re.findall(r'nsubj:xsubj\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                xcomp_nsubj[k1] = second_word, v.rstrip()[-1]
map_list.append('xcomp_nsubj')

for k, v in sourcemap.items():
    if re.search("amod", v):
        first_word = re.findall(r'amod\(([^-]*)-', v)
        for k1, v1 in pline_map.items():
                if re.search('nmod:from',v1):
                    second_word = re.findall(
                        r'nmod:from\(([^-]*)-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-', v1)
                                amod_nmodf[k1] = second_word, v.rstrip()[-1]

map_list.append('amod_nmodf')


for k, v in sourcemap.items():
    if re.search('nsubj', v):
        v2 = str(re.findall("(?<=nsubj\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("nmod:of", v1):
                    second_word = re.findall(r'nmod:of\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                nsubj_nmod[k1] = second_word, v.rstrip()[-1]
map_list.append('nsubj_nmod')

for k, v in sourcemap.items():
    if re.search('root', v):
        v2 = str(re.findall("(?<=root\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("nsubj", v1):
                    second_word = re.findall(r'nsubj\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                root_nsubj[k1] = second_word, v.rstrip()[-1]
map_list.append('root_nsubj')

for k, v in sourcemap.items():
    if re.search('advmod',v):
        first_word = re.findall(r'advmod\(([^-]*)-', v)
        for k1,v1 in pline_map.items():
            if re.search("amod", v1):
                    second_word = re.findall(
                        '\, (.*?)\-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                advmod_amod[k1] = second_word, v.rstrip()[-1]
map_list.append('advmod_amod')

for k, v in sourcemap.items():
    if re.search('amod',v):
        first_word = re.findall(r'amod\(([^-]*)-', v)
        for k1,v1 in pline_map.items():
            if re.search("nmod:for", v1):
                    second_word = re.findall(
                        '\, (.*?)\-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                amod_nmodf[k1] = second_word, v.rstrip()[-1]
map_list.append('amod_nmodf')

for k, v in sourcemap.items():
    if re.search('advmod',v):
        first_word = re.findall(r'advmod\(([^-]*)-', v)
        for k1,v1 in pline_map.items():
            if re.search("root", v1):
                    second_word = re.findall(
                        '\, (.*?)\-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                advmod_root[k1] = second_word, v.rstrip()[-1]
map_list.append('advmod_root')

for k, v in sourcemap.items():
    if re.search('acl:relcl', v):
        v2 = str(re.findall("(?<=acl:relcl\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("nsubjpass", v1):
                    second_word = re.findall(r'nsubjpass\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                acl_nsubjp[k1] = second_word, v.rstrip()[-1]
map_list.append('acl_nsubjp')

for k, v in sourcemap.items():
    if re.search("nmod:in", v):
        first_word = re.findall(r'nmod:in\(([^-]*)-', v)
        for k1, v1 in pline_map.items():
                if re.search('nsubjpass',v1):
                    second_word = re.findall(
                        r'nsubjpass\(([^-]*)-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-', v1)
                                nmod_nsubjpass[k1] = second_word, v.rstrip()[-1]

map_list.append('nmod_nsubjpass')

for k, v in sourcemap.items():
    if re.search('conj:and', v):
        v2 = str(re.findall("(?<=conj:and\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("advcl", v1):
                    second_word = re.findall(r'advcl\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                conja_advcl[k1] = second_word, v.rstrip()[-1]
map_list.append('conja_advcl')

for k, v in sourcemap.items():
    if re.search('acl', v):
        v2 = str(re.findall("(?<=acl\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("dobj", v1):
                    second_word = re.findall(r'dobj\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                acl_dobj[k1] = second_word, v.rstrip()[-1]
map_list.append('acl_dobj')

for k, v in sourcemap.items():
    if re.search("neg", v):
        first_word = re.findall(r'neg\(([^-]*)-', v)
        for k1, v1 in pline_map.items():
                if re.search('nsubj',v1):
                    second_word = re.findall(
                        r'nsubj\(([^-]*)-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-', v1)
                                neg_nsubj[k1] = second_word, v.rstrip()[-1]

map_list.append('neg_nsubj')

for k, v in sourcemap.items():
    if re.search('appos',v):
        first_word = re.findall(r'appos\(([^-]*)-', v)
        for k1,v1 in pline_map.items():
            if re.search("nsubj", v1):
                    second_word = re.findall(
                        '\, (.*?)\-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                appos_nsubj[k1] = second_word, v.rstrip()[-1]
map_list.append('appos_nsubj')

for k, v in sourcemap.items():
    if re.search("xcomp", v):
        first_word = re.findall(r'xcomp\(([^-]*)-', v)
        for k1, v1 in pline_map.items():
                if re.search('nsubj',v1):
                    second_word = re.findall(
                        r'nsubj\(([^-]*)-', v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-', v1)
                                xcomp_nsubj[k1] = second_word, v.rstrip()[-1]

map_list.append('xcomp_nsubj')

for k, v in sourcemap.items():
    if re.search('acl:relcl', v):
        v2 = str(re.findall("(?<=acl:relcl\().+?(?=\))", v))
        first_word = re.findall('\, (.*?)\-', v2)
        for k1, v1 in pline_map.items():
                if re.search("nsubj", v1):
                    second_word = re.findall(r'nsubj\(([^-]*)-',
                                             v1.lstrip(' '))
                    if k[:4] == k1[:4]:
                        for i in first_word:
                            if second_word == [i]:
                                second_word = re.findall('\, (.*?)\-',v1)
                                acl_nsubj[k1] = second_word, v.rstrip()[-1]
map_list.append('acl_nsubj')

for i in map_list:
    #print(eval(i))
    amod_nmod_map.update(eval(i)) #feeds and combines the list of rule dictionaries into a larger combined one

found_targets_counter = 0

targets = open('targets.txt', 'w+')
i=0
print('Creating Target File...')
for idx,pline in pline_map.items():
    i+=1
    print_progress_bar(i+1, len(pline_map)+1)
    targets.write(pline)
    if amod_nmod_map.get(idx):
        targets.write('t{} \n'.format(amod_nmod_map[idx][1])) ##appends the t# based on s#
        found_targets_counter+=1
    else:
        targets.write('\n') ## if it's just a normal line, new line and continue printing text
print('targets.txt created')
print("Found {} targets".format(found_targets_counter))

