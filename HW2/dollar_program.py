# Samira Mantri
# 2/13/19

import re
import sys

# open text file and read contents
file_name = sys.argv[1]
text_file = open(file_name,"r",encoding="utf-8")
text_str = ""
line = text_file.readline()

while line:
    text_str += line
    line = (text_file.readline()).lower()

text_file.close()


# create a new file to hold the results
output = open("dollar_output.txt","w+")

# check for when there is a dollar sign
regex0 = r"(\$?(\d{1,3}(,\d{3})*)(\.[0-9]{1,100})?\W?(million|billion)(\W?dollars))"
# check for when there is no dollar sign
regex1 = "|(\$(\d{1,3}(,\d{3})*)(\.[0-9]{1,100})?\W?(million|billion))"
# check cents
regex2 = "|(\$?([0-9]{1,100})?\.?[0-9]{1,100}\W?(cents|cent))"
# check for amounts with dollars and cents
regex3 = "|(\$?(\d{1,3}(,\d{3})*)(\.[0-9]{1,100})?\W?(dollars|dollar)(\W?and\W?([0-9]"
regex4 = "{1,100})?(\.?[0-9]{1,100})?\W?(cents|cent))?)"
# check for money with only dollar sign
regex5 = "|(\$(\d{1,3}(,\d{3})*)(\.?[0-9]{1,100})?)"
# check for parts of amounts
regex6 = "|((a\W?)?(quarter|half|third|fourth|fifth|sixth|seventh|eighth|ninth)\W?(of"
regex7 = "\W?)?a\s?(million|billion)(\W?(dollars)))"
# check for written out amounts
regex8 = "|(((one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|"
regex9 = "fourteen|fifteen|sixteen|seventeen|eighteen|ninteen|twenty|thirty|forty|fifty|"
regex10 = "sixty|seventy|eighty|ninty)\W?((one|two|three|four|five|six|seven|eight|"
regex11 = "nine)\W?)?(hundred|thousand|million|billion)?\W?)+(\W?(hundred|thousand|million|billion)\s?)?"
regex12 = "(dollars|dollar)(\W?and.*(cents|cent))?)"
# check for written amounts with cents
regex13 = "|(((twenty|thirty|forty|fifty|sixty|seventy|eighty|ninty)\W?)"
regex14 = "((one|two|three|four|five|six|seven|eight|nine)\W?)?cents)|"
regex15 = "((one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
regex16 = "thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|ninteen)\W?(cents|cent))"

# combine the regex string into one
regex_sum1 = regex0+regex1+regex2+regex3+regex4+regex5+regex6+regex7+regex8+regex9+regex10+regex11+regex12
regex = regex_sum1+regex13+regex14+regex15+regex16

# find the matches 
matches = list(re.finditer(regex,text_str,re.MULTILINE))

# print the matches 
for match in matches:
    match_output = (match.group(0)).replace ('\n', ' ')
    output.write(match_output+"\n")
    #print (match_output)

# close the output file
output.close()

    



