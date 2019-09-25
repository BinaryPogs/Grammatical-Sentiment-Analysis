## Introduction

(Stanford Parser)[1] is a natural language parser program that is used to output typed dependency parses. 
The purpose of this project is to create a program that can read text-file input from Stanford parser and return an output that defines what the target words of each paragraph are. This is a project given to me by a search engine startup called (Lexxe)[2], which uses sentiment analysis in their search engines. The goal is to utilise Stanford parser to create a system that can attribute sentiment meaning to keywords via grammatical analysis. 

## How it works

The program will read a text-file (suffixes in .ant or .psd) and separate each paragraph(or search query) separately so that targets correspond to their respective paragraph. The requirements of the program are not fully defined as of today (18/09/2019) but currently the program outputs text indicating the target words and which paragraph they were found in based on multiple different rules created by linguists that have examined the text file outputs created by the Stanford parser. The current program creates a .csv file with the target words and how many targets found divided by the number of targets in the file (accuracy.



[1]: https://nlp.stanford.edu/software/lex-parser.shtml

[2]: https://en.wikipedia.org/wiki/Lexxe