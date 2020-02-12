import sys
import unicodedata
import math

# create file to write to
filename = "output.txt"
output = open(filename,"w",newline='\n')

# create function to remove numbers and punctuation
def remove_pun(my_str):
    # define punctuation
    extra = '''!()[]{};:'"\,<>./?@#$%^&*_~0123456789'''
    no_extra = ""
    for char in my_str:
       if (char not in extra):
           no_extra = no_extra + char

    return no_extra


# specify stop words
stop_words = ['a','the','an','and','or','but','about','above','after','along','amid','among',\
                           'as','at','by','for','from','in','into','like','minus','near','of','off','on',\
                           'onto','out','over','past','per','plus','since','till','to','under','until','up',\
                           'via','vs','with','that','can','cannot','could','may','might','must',\
                           'need','ought','shall','should','will','would','have','had','has','having','be',\
                           'is','am','are','was','were','being','been','get','gets','got','gotten',\
                           'getting','seem','seeming','seems','seemed',\
                           'enough', 'both', 'all', 'your' 'those', 'this', 'these', \
                           'their', 'the', 'that', 'some', 'our', 'no', 'neither', 'my',\
                           'its', 'his' 'her', 'every', 'either', 'each', 'any', 'another',\
                           'an', 'a', 'just', 'mere', 'such', 'merely' 'right', 'no', 'not',\
                           'only', 'sheer', 'even', 'especially', 'namely', 'as', 'more',\
                           'most', 'less' 'least', 'so', 'enough', 'too', 'pretty', 'quite',\
                           'rather', 'somewhat', 'sufficiently' 'same', 'different', 'such',\
                           'when', 'why', 'where', 'how', 'what', 'who', 'whom', 'which',\
                           'whether', 'why', 'whose', 'if', 'anybody', 'anyone', 'anyplace', \
                           'anything', 'anytime' 'anywhere', 'everybody', 'everyday',\
                           'everyone', 'everyplace', 'everything' 'everywhere', 'whatever',\
                           'whenever', 'whereever', 'whichever', 'whoever', 'whomever' 'he',\
                           'him', 'his', 'her', 'she', 'it', 'they', 'them', 'its', 'their','theirs',\
                           'you','your','yours','me','my','mine','I','we','us','much','and/or'
                           ]

# open file
qry = open("cran.qry","r")

# create dictionary to keep track of how many
# times a word appears in all the queries
word_num_in_docs = {}

# create a dictionary to hold all the queries and how
# many times each of their words appeared 
all_qrys = {}
qry_num = 225 + 1

# create a counter to keep track of current query
counter = 1
# iterate through queries
for x in range(qry_num):
    raw_line = qry.readline()
    line = raw_line.strip()
    line_items = line.split(' ')
    build_string = ""
    if (line_items[0] == ".W"):
        condition = True
        while (condition == True):
            raw_line = qry.readline()
            line = raw_line.strip()
            line_items = line.split(' ')
            if(line_items[0] == ".I" or line_items[0] == ""):
                condition = False
            else:
                string_to_add = remove_pun(line)
                build_string += (" "+string_to_add)

    if (build_string != ""):
        qry_items = build_string.split(' ')
        final_items = {}
        for pos in range(len(qry_items)):
            if (qry_items[pos] != "" and qry_items[pos] not in stop_words):
                word = qry_items[pos]
                # add word occurence among queries 
                if word in word_num_in_docs.keys() and word not in final_items.keys():
                    word_num_in_docs[word] += 1
                elif word not in word_num_in_docs.keys():
                    word_num_in_docs[word] = 1

                # add word to list of words for query 
                if word in final_items.keys():
                    final_items[word] += 1
                else:
                    final_items[word] = 1



        # add query
        all_qrys[counter] = final_items
        counter += 1


# calculate the TF-IDF for each query
qry_tf_idf = {}

for x in all_qrys.keys():
    new_dict = {} 
    for y in all_qrys[x].keys():
        word = y
        tf = all_qrys[x][y]
        global_freq = word_num_in_docs[word]
        idf = math.log((qry_num-1)/global_freq)
        val = tf*idf
        new_dict[word] = idf
    qry_tf_idf[x] = new_dict
        
        

# handle abstract
doc = open("cran.all.1400","r")

# create dictionary to keep track of how many
# times a word appears in all the abstracts
word_num_in_abstracts = {}
# create a dictionary to hold all the abstracts
# and their words
all_abstract = {}

# create an abstract count
# to keep track of the abstracts
abstract_count = 0
abstract_num = 1400

# iterate through the abstracts
while (abstract_count <= abstract_num):
    raw_line = doc.readline()
    line = raw_line.strip()
    line_items = line.split(' ')
    build_string = None
    if (line_items[0] == ".W"):
        build_string = ""
        condition = True
        # increment abstract count
        # if an abstract is found
        abstract_count += 1
        while (condition == True):
            raw_line = doc.readline()
            line = raw_line.strip()
            line_items = line.split(' ')
            if(line_items[0] == ".I" or line_items[0] == ""):
                condition = False
            else:
                string_to_add = remove_pun(line)
                build_string += (" "+string_to_add)

    if (build_string != "" and build_string != None):
        abstract_items = build_string.split(' ')
        final_items = {}
        for pos in range(len(abstract_items)):
            if (abstract_items[pos] != "" and abstract_items[pos] not in stop_words):
                word = abstract_items[pos]
                # add word occurence among abstracts 
                if word in word_num_in_abstracts.keys() and word not in final_items.keys():
                    word_num_in_abstracts[word] += 1
                elif word not in word_num_in_abstracts.keys():
                    word_num_in_abstracts[word] = 1

                # add word to list of words for abstract 
                if word in final_items.keys():
                    final_items[word] += 1
                else:
                    final_items[word] = 1
        all_abstract[abstract_count] = final_items
        if(abstract_count == 1400):
            break
    elif (build_string == ""):
        all_abstract[abstract_count] = {}
        


# handle abstract tf-idf
abstract_tf_idf = {}

# calculate abstract tf-idf
for x in all_abstract.keys():
    new_dict = {}
    for y in all_abstract[x].keys():
        word = y
        tf = all_abstract[x][y]
        global_freq = word_num_in_abstracts[word]
        idf = math.log((abstract_num)/global_freq)
        val = tf*idf
        new_dict[word] = idf
    abstract_tf_idf[x] = new_dict


# calculate cosine similarity 
qry_check = 1
# check score for each query
while (qry_check <= 225):
    abstract_check = 1
    words_to_check = qry_tf_idf[qry_check]
    score_abstract = {}
    # iterate through all abstracts 
    while (abstract_check <= abstract_num):
        abstract_vector = {}
        # build abstract vector
        for word in words_to_check.keys():
            if word in abstract_tf_idf[abstract_check].keys():
                abstract_vector[word] = abstract_tf_idf[abstract_check][word]
            else:
                abstract_vector[word] = 0
     

        # perform cosine similarity calculations
        # to get score 
        top_sum = 0
        bottom_sum1 = 0
        bottom_sum2 = 0
        for word in words_to_check.keys():
            top_sum += words_to_check[word]*abstract_vector[word]
            bottom_sum1 += math.pow(words_to_check[word],2)
            bottom_sum2 += math.pow(abstract_vector[word],2)
        final_bottom_sum = math.sqrt(bottom_sum1*bottom_sum2)
        # find the final score 
        final_sum = 0
        if(final_bottom_sum != 0):
            final_sum = top_sum/final_bottom_sum
        # set score equal to abstract num
        score_abstract[abstract_check] = final_sum
        # increment abstract 
        abstract_check += 1

    # sort abstract scores    
    sorted_abstract = sorted(score_abstract, key=score_abstract.get, reverse=True)
    # add info to text file
    for r in sorted_abstract:
        output.write(str(qry_check)+" "+str(r)+" "+str(score_abstract[r])+"\n")

    qry_check += 1


# close files
output.close()
doc.close()
qry.close()
    
        
        




        





            
            

