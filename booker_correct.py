import time
import os.path
import string

import is_there_dict 
import booker_most_frequent


#similar to booker_most_frequent.word_histogram , but here
# we are first separating word , and then checking if that word is in dictionary
# rudimentary now - need to return what line is wrong , along with correction suggestion
####3
####3	deprecated
####3
"""
def check_data(data):
	""

		check if each word in data is present in dictionary.
	""
	reference_dict = is_there_dict.create_dict()

	#punctuations = string.punctuation
	punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
	prev_pause = 0
	curr_pause = 0
	index = 0
	sugg_corrections = 0

	while index < len(data):
		if data[index] ==" " or data[index] in punctuations:#split at spaces, comma, dot, etc
		
			his = True

			if data[index]=='\'' or data[index]=='`':
				if data[index+1]=='s':
					his = False#skip over if words like "nature's" come
					pass
					
			#if not his:
			if index!=len(data)-1 and data[index+1]==" ":#new line sort
				prev_pause = index + 2
			else:
				curr_pause = index
				this_word = data[prev_pause:curr_pause]
				this_word = this_word.lower()
				if this_word!='':
					if this_word not in reference_dict:
						print this_word
						sugg_corrections += 1
				
				prev_pause = curr_pause+1
		index += 1
	return sugg_corrections
"""


def check_data(transcript,reference_dict):
	"""

		return a dictionary of words in transcript not in reference_dict
		Effectively , these are percieved as misspelled words.
	"""
	incorrect_dict = dict()
	count = 0
	for key ,freq,percent in transcript:

		if key not in reference_dict:
			#print key,' not in dict'
			incorrect_dict[key] = 'suggest_correction_here'
			count += freq	# a word may be misspelled multiple times

	return incorrect_dict,count


def correct(filer):
	
	if not os.path.isfile(filer):
		print '\tNot a valid file !Returning now...'
		return 

	out,tot_words_doc = booker_most_frequent.most_frequent(filer,'word')
	reference_dict = is_there_dict.create_dict()

	incorrect_dict,count = check_data(out,reference_dict)
	print '\n'	
	for key in incorrect_dict:
		print '\t',key

	time.sleep(2)
	print '\n\tTotal misspelled occurences : ',count



if __name__ == '__main__':
	
	filer = raw_input("\tEnter your file for typos:\n\t ")
	correct(filer)