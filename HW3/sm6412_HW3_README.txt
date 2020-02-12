net id: sm6412
name: Samira Mantri
date: 2/25/19

How to run: 
When submitting my zip file, I will be sure to include the two training pos files:
1st file: WSJ_02-21.pos
2nd file: WSJ_24.pos

My program calls them specifically, so they do not need to be entered as command line
arguments. They simply need to be in the same location as the sm6412_HW3.py file. When running my code
with a word file(like WSJ_23.words) you will enter the name of the word file as a 
command line argument. On my windows, the command line arguments for my python3 file
look like the following:

python sm6412_HW3.py WSJ_23.words

The output file will always be entitled: submission.pos

How I handled OOVs:
I used 1/1000 for the emission probability for all OOV words.
For the transition probability, I kept track of the previous part of speech with the highest probability,
then used the pos with the highest probability of following that pos for all OOV words. 
