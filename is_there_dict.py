import time

def create_dict():
	"""

		Add each string as key in a dict
	"""
	word_dict = dict()
	fin = open('words.txt')

	for line in fin:
		word = line.strip()
		word_dict[word] = word

	return word_dict

def is_there_dict(word):
 	"""

 		U still here ?Why are you so obsessed with this . Go , away !
 		Good . Use your in method , because #tables were made for you
 	"""
	start_time = time.time()
	source = create_dict()
	print '\n',word,'in dict : ',word in source

	elapsed_time = time.time() - start_time
	#print 'elapsed_time :',elapsed_time,'seconds'
	# upto 50 % better - check where this backtracks to in wordabulary