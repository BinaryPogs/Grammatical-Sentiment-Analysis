import re


s = 'neg(ables-23, never-21) s2-1/3'
i = 'amod(Markets-8, magical-5) s1'
word = re.search('(s\d+)-?([0-9]+)?\/?([0-9]+)?$', i)
print(word)

#new = re.search(r"s\d[-/\d]*", l.rstrip())
# print(new)

r = 'root(ROOT-0, wearing-6)'


v = str(re.findall("(?<=root\().+?(?=\))", r))
first_word = re.findall('\, (.*?)\-', v)

print(first_word)
