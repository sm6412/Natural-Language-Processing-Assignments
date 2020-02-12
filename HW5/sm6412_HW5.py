import sys

# gets the length of a file
def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1

# create file to write to
output = open("training.feature","w+",newline='\n')
output2 = open("test.feature","w+",newline='\n')

training_file = open("WSJ_02-21.pos-chunk","r",encoding="utf-8")

# counts lines
counter = 1

# counts sentence position
sen_pos = 1

# sentence list
sen_list = []

# retrieve file length
file_length = file_lengthy("WSJ_02-21.pos-chunk")

# create dictionary to hold words and tags
training_dict = {}

# grab features
while (True):
    # read new line
    line = training_file.readline()
    line = line.strip()
    line_items = line.split('\t')
    
    if(line_items[0]==""):
        sen_list = []
        training_dict[counter] = "blank"
        counter+=1
        
        # read new line
        line = training_file.readline()
        line = line.strip()
        line_items = line.split('\t')
        
    # grab sentence
    while (line_items[0]!=""):
        sen_list.append(line_items)
        # read new line
        line = training_file.readline()
        line = line.strip()
        line_items = line.split('\t')

    # get sentence info
    for y in range(len(sen_list)):
        list_element = sen_list[y]
        word = list_element[0]
        pos = list_element[1]
        bio = list_element[2]

        # create new dict for line
        line_dict = {}

        # put current word, pos, and bio in dict
        line_dict['word'] = word
        line_dict['POS'] = pos

        # see whether the word starts the sentence or not
        if(y==0):
                line_dict["sen_start"] = "true"
        else:
                line_dict["sen_start"] = "false"

        #see whether the word ends the sentence or not
        if(y==(len(sen_list)-1)):
                line_dict["sen_end"] = "true"
        else:
                line_dict["sen_end"] = "false"
                        
        # check to see whether the word is capitalized or not
        if(word[0].isupper()==True):
                line_dict["capitalized"] = "true"
        else:
                line_dict["capitalized"] = "false"
        
        # put previous word, pos, and bio in dict
        if((y-1)>=0):
            prev_list_element = sen_list[y-1]
            line_dict['prev_word'] = prev_list_element[0]
            line_dict['prev_POS'] = prev_list_element[1]
            line_dict['prev_BIO'] = prev_list_element[2]

        # put 2nd previous word, pos, and bio in dict
        if((y-2)>=0):
            prev_list_element = sen_list[y-2]
            line_dict['2nd_prev_word'] = prev_list_element[0]
            line_dict['2nd_prev_POS'] = prev_list_element[1]
            line_dict['2nd_prev_BIO'] = prev_list_element[2]

        # put 3rd previous word, pos, and bio in dict
        if((y-3)>=0):
            prev_list_element = sen_list[y-2]
            line_dict['3rd_prev_word'] = prev_list_element[0]
            line_dict['3rd_prev_POS'] = prev_list_element[1]
            line_dict['3rd_prev_BIO'] = prev_list_element[2]

        # put next word, pos, and bio in dict
        if((y+1)<=(len(sen_list)-1)):
            next_list_element = sen_list[y+1]
            line_dict['next_word'] = next_list_element[0]
            line_dict['next_POS'] = next_list_element[1]
            line_dict['next_BIO'] = next_list_element[2]

        # put 2nd next word, pos, and bio in dict
        if((y+2)<=(len(sen_list)-1)):
            next_list_element = sen_list[y+2]
            line_dict['2nd_next_word'] = next_list_element[0]
            line_dict['2nd_next_POS'] = next_list_element[1]
            line_dict['2nd_next_BIO'] = next_list_element[2]

        # put 3rd next word, pos, and bio in dict
        if((y+3)<=(len(sen_list)-1)):
            next_list_element = sen_list[y+2]
            line_dict['3rd_next_word'] = next_list_element[0]
            line_dict['3rd_next_POS'] = next_list_element[1]
            line_dict['3rd_next_BIO'] = next_list_element[2]

        line_dict['BIO'] = bio

        

        # add new dict to training dict
        training_dict[counter] = line_dict

        # increment counter
        counter+=1

 

    sen_list = []
    training_dict[counter] = "blank"

    # break if max lines reached
    if(counter>=file_length):
        break
    
    counter+=1



# write information to training document
for x in range(len(training_dict)):
    current = training_dict[x+1]
    if(current=="blank"):
        output.write("\n")
    else:
        res = ""
        for key in current.keys():
            if(key=="word"):
                res += current[key]
            elif(key=="BIO"):
                res += "\t"+current[key]
            else:
                res += "\t"+key+"="+current[key]

        res += "\n"
        output.write(res)

# close files 
output.close()           
training_file.close()

#-----------------------------------------------------------------------------
# handle test file

test_file = open("WSJ_23.pos","r",encoding="utf-8")

# counts lines
counter = 1

# counts sentence position
sen_pos = 1

# sentence list
sen_list = []

# retrieve file length
file_length = file_lengthy("WSJ_23.pos")

# create dictionary to hold words and tags
test_dict = {}

# grab features 
while (True):
    # read new line
    line = test_file.readline()
    line = line.strip()
    line_items = line.split('\t')
    
    if(line_items[0]==""):
        sen_list = []
        test_dict[counter] = "blank"
        counter+=1
        
        # read new line
        line = test_file.readline()
        line = line.strip()
        line_items = line.split('\t')
        
    # grab sentence
    while (line_items[0]!=""):
        sen_list.append(line_items)
        # read new line
        line = test_file.readline()
        line = line.strip()
        line_items = line.split('\t')

    # get sentence info
    for y in range(len(sen_list)):
        list_element = sen_list[y]
        word = list_element[0]
        pos = list_element[1]

        # create new dict for line
        line_dict = {}

        # put current word, pos, and bio in dict
        line_dict['word'] = word
        line_dict['POS'] = pos

        # see whether the word starts the sentence or not
        if(y==0):
                line_dict["sen_start"] = "true"
        else:
                line_dict["sen_start"] = "false"

        #see whether the word ends the sentence or not
        if(y==(len(sen_list)-1)):
                line_dict["sen_end"] = "true"
        else:
                line_dict["sen_end"] = "false"

        # check to see whether the word is capitalized or not
        if(word[0].isupper()==True):
                line_dict["capitalized"] = "true"
        else:
                line_dict["capitalized"] = "false"

        # put previous word, pos, and bio in dict
        if((y-1)>=0):
            prev_list_element = sen_list[y-1]
            line_dict['prev_word'] = prev_list_element[0]
            line_dict['prev_POS'] = prev_list_element[1]

        # put 2nd previous word, pos, and bio in dict
        if((y-2)>=0):
            prev_list_element = sen_list[y-2]
            line_dict['2nd_prev_word'] = prev_list_element[0]
            line_dict['2nd_prev_POS'] = prev_list_element[1]

        # put 3rd previous word, pos, and bio in dict
        if((y-3)>=0):
            prev_list_element = sen_list[y-2]
            line_dict['3rd_prev_word'] = prev_list_element[0]
            line_dict['3rd_prev_POS'] = prev_list_element[1]

        # put next word, pos, and bio in dict
        if((y+1)<=(len(sen_list)-1)):
            next_list_element = sen_list[y+1]
            line_dict['next_word'] = next_list_element[0]
            line_dict['next_POS'] = next_list_element[1]

        # put 2nd next word, pos, and bio in dict
        if((y+2)<=(len(sen_list)-1)):
            next_list_element = sen_list[y+2]
            line_dict['2nd_next_word'] = next_list_element[0]
            line_dict['2nd_next_POS'] = next_list_element[1]

        # put 3rd next word, pos, and bio in dict
        if((y+3)<=(len(sen_list)-1)):
            next_list_element = sen_list[y+2]
            line_dict['3rd_next_word'] = next_list_element[0]
            line_dict['3rd_next_POS'] = next_list_element[1]


        # add new dict to training dict
        test_dict[counter] = line_dict

        # increment counter
        counter+=1

 
    # clear sentence list
    sen_list = []
    # add blank space
    test_dict[counter] = "blank"

    # break if max lines reached
    if(counter>=file_length):
        break

    # increment counter
    counter+=1

# write information to test document
for x in range(len(test_dict)):
    current = test_dict[x+1]
    if(current=="blank"):
        output2.write("\n")
    else:
        res = ""
        for key in current.keys():
            if(key=="word"):
                res += current[key]
            elif(key=="BIO"):
                res += "\t"+current[key]
            else:
                res += "\t"+key+"="+current[key]

        res += "\n"
        output2.write(res)

# close files 
output2.close()
test_file.close()


