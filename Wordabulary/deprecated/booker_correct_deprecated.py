import time
from is_there_dict import create_dict
import os.path
import string

import is_there_dict 
import booker_most_frequent


#similar to booker_most_frequent.word_histogram , but here
# we are first separating word , and then checking if that word is in dictionary
# rudimentary now - need to return what line is wrong , along with correction suggestion
def check_data(data):
	"""

		check if eah word in data is present in dictionary.
	"""
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


def correct(filer):
	
	if not os.path.isfile(filer):
		print '\tNot a valid file !Returning now...'
		return 

	with open(filer) as f:
        
		data=''.join(line.rstrip() for line in f)

	count = check_data(data)
	print '\n\tSuggested corrections : ',count



if __name__ == '__main__':
	
	filer = raw_input("\tEnter your file for typos:\n\t ")
	correct(filer) 