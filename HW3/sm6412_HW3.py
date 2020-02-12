import sys

# create file to write to
output = open("submission.pos","w+",newline='\n')


# methods
# gives a string representation of the matrix for testing
def return_matrix(matrix):
    print('\n'.join([''.join(['{:8}'.format(item) for item in row]) 
      for row in matrix]))
    return

# resets the viterbi matrix
def reset_viterbi():
    viterbi = []
    for row in range(states_num):
        new_row = []
        for col in range(word_range+2):
            new_row.append(0)
        viterbi.append(new_row)

    viterbi[0][0] = 1
    return viterbi

# writes information to the output file
def write_to_doc(final_states,current_words):
        for words in range(len(current_words)):
                if(current_words[words] == "END"):
                        output.write("\n")
                           
                else:
                        res = current_words[words]+"\t"+final_states[words]+"\n"
                        output.write(res)
        return


# gets the length of a file
def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
   
# open the pos files for training
pos_file1 = open("WSJ_24.pos","r",encoding="utf-8")
pos_file2 = open("WSJ_02-21.pos","r",encoding="utf-8")
file_length1 = file_lengthy("WSJ_24.pos")
file_length2 = file_lengthy("WSJ_02-21.pos")

# format the line
line = pos_file1.readline()
line = line.strip()
line_items = line.split('\t')


# create dictionaries
# word_pos maps how often a word occurs for a pos
word_pos = {line_items[1]:{line_items[0]:1}}

# dictionary that tracks pos frequency
pos_freq = {"START":1}
pos_freq[line_items[1]] = 1

# keeps track of prev part of speech to create prior prob dictionary
prev = "START"
next_pos = {prev:{line_items[1]:1}}
prev = line_items[1]

# create array to keep track of known words
words = [line_items[0]]


# read in info for first file
# file_length1
for line in range(file_length1):
    if prev == "START":
        pos_freq["START"] += 1
        
    # get elements of each line
    line = pos_file1.readline()
    line = line.strip()
    line_items = line.split('\t')
    
    # ensure there is a word and pos in line
    if(len(line_items)> 1):
        pos = line_items[1]
        word = str(line_items[0])

        # add new words to list of words
        if word not in words:
            words.append(word)

        # handle transition library
        if prev in next_pos.keys():
            if pos in next_pos[prev].keys():
                next_pos[prev][pos] += 1
            else:
                new_dict = {pos:1}
                next_pos[prev].update(new_dict)
        else:
            next_pos[prev] = {pos:1}
        prev = pos;

        # handle emmission library
        if pos in word_pos.keys():
            pos_freq[pos] += 1
            if word in word_pos[pos].keys():
                word_pos[pos][word] += 1
            else:
                new_dict = {word:1}
                word_pos[pos].update(new_dict) 
        else:
            word_pos[pos] = {word:1}
            pos_freq[pos] = 1
    else:
        pos = "END"
        if prev in next_pos.keys():
            if pos in next_pos[prev].keys():
                next_pos[prev][pos] += 1
            else:
                new_dict = {pos:1}
                next_pos[prev].update(new_dict)
        else:
            next_pos[prev] = {pos:1}

        prev = "START"

# read in info for second file
for line in range(file_length2):
    if prev == "START":
        pos_freq["START"] += 1
        
    # get elements of each line
    line = pos_file2.readline()
    line = line.strip()
    line_items = line.split('\t')
    
    # ensure there is a word and pos in line
    if(len(line_items)> 1):
        pos = line_items[1]
        word = str(line_items[0])

        # add new words to list of words
        if word not in words:
            words.append(word)

        # handle transition library
        if prev in next_pos.keys():
            if pos in next_pos[prev].keys():
                next_pos[prev][pos] += 1
            else:
                new_dict = {pos:1}
                next_pos[prev].update(new_dict)
        else:
            next_pos[prev] = {pos:1}
        prev = pos;

        # handle emmission library
        if pos in word_pos.keys():
            pos_freq[pos] += 1
            if word in word_pos[pos].keys():
                word_pos[pos][word] += 1
            else:
                new_dict = {word:1}
                word_pos[pos].update(new_dict) 
        else:
            word_pos[pos] = {word:1}
            pos_freq[pos] = 1
    else:
        pos = "END"
        if prev in next_pos.keys():
            if pos in next_pos[prev].keys():
                next_pos[prev][pos] += 1
            else:
                new_dict = {pos:1}
                next_pos[prev].update(new_dict)
        else:
            next_pos[prev] = {pos:1}

        prev = "START"



pos_freq["END"]  = 0
next_pos["END"] = 0

# close pos files
pos_file1.close()
pos_file2.close()


# gather one instance of every pos
pos_list = []
for pos in pos_freq:
    pos_list.append(pos)

# create a transition frequencies table
matrix_size = len(pos_list)
prior_prob = []
pos_str = (str(pos_list)).strip()

for row in range(matrix_size):
    new_row = []
    row_pos = pos_list[row]
    freq_of_pos = pos_freq[row_pos]
    for col in range(matrix_size):
        col_pos = pos_list[col]
        val = 0
        orig = 0
        if(row_pos == "END"):
            val = 0
        else:
            if col_pos in next_pos[row_pos].keys():
                val = (next_pos[row_pos][col_pos])/freq_of_pos
                orig = next_pos[row_pos][col_pos]
        new_row.append(val)

    # add new row to matrix
    prior_prob.append(new_row)


# get words from words file and put them in a list 
word_array = []
fname = sys.argv[1]
word_file = open(fname,"r",encoding="utf-8")
word_file_length = file_lengthy(fname)
line = (word_file.readline()).strip()
word_array.append(line)

# use word_file_length for length
# word_file_length
for x in range(word_file_length) :
    line = (word_file.readline()).strip()
    if(len(line) == 0):
        word_array.append("END")
    else:
        word_array.append(line)




# gather num of words and pos
word_range = len(word_array)
states_num = len(pos_list)


# create viterbi matrix
viterbi = reset_viterbi()

#return_matrix(viterbi)

# handle the maxes
max_num = 1
max_state = "START"
current_words= []
final_states = []
states_for_max = []
num_for_max = []

# run viterbi algo
for word in range(word_range-1):
    # get the current word
    current_word = word_array[word]
    current_words.append(current_word)
    # if the sentence ends, write info to ouput
    if(current_word == "END"):
        final_states.append("END")
        write_to_doc(final_states,current_words)

        # reset values
        current_words= []
        max_num = 1
        max_state = "START"
        final_states = []
        states_for_max = []
        num_for_max = []
        viterbi = reset_viterbi()
    else:
        for state in range(1,states_num):
            # get the current state
            current_state = pos_list[state]

            # get emmision prob
            # OOV case
            emi_prob = None
            # if word in words set prob initially to 0
            if current_word in words:
                emi_prob = 0
            # if word not in words, set emmission prob to 1/1000
            else:
                emi_prob = 0.001
                
            if current_state in word_pos.keys():
                if current_word in word_pos[current_state].keys():
                   emi_prob = (word_pos[current_state][current_word])/(pos_freq[current_state])

            # get transition prob 
            trans_prob = (prior_prob[pos_list.index(max_state)][pos_list.index(current_state)])

            # get final value
            final_val = max_num*trans_prob*emi_prob

            # put states and values into arrays to use later when finding the max state
            states_for_max.append(current_state)
            num_for_max.append(final_val)
            viterbi[state][word+1] = final_val


        # get new max state and number
        # search for max
        temp_max = num_for_max[0]
        temp_index = 0
        for x in range(1,len(num_for_max)):
            if(num_for_max[x] > temp_max):
                temp_max = num_for_max[x]
                temp_index = x

        # set new max num and state
        max_num = temp_max
        max_state = states_for_max[temp_index]

        # clear previous maxes and states
        states_for_max.clear()
        num_for_max.clear()
        final_states.append(max_state)


word_file.close()

output.close()





