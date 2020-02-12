# Samira Mantri
# 2/13/19

import re
import sys

file_name = sys.argv[1]
text_file = open(file_name,"r",encoding="utf-8")
text_str = ""
line = text_file.readline()

while line:
    text_str += line
    line = text_file.readline()

text_file.close()

# create a new file to hold the results
output = open("telephone_output.txt","w+")

# regex expression
regex1 = r"(((\+[0-9]{1,4}\W?)?(\(?([0-9]{3})\)?\W?))"
regex2 = "|(^))([0-9]{3})\W?([0-9]{4})(?!\B)"

regex = regex1+regex2

# matches
matches = list(re.finditer(regex,text_str,re.MULTILINE))

# print the matches 
for match in matches:
    match_output = (match.group(0)).replace ('\n', ' ')
    output.write(match_output+"\n")
    #print (match_output)

# close output file
output.close()

    



