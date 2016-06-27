from has_no_e import *
from words_with_e import *
import time
import string

def allstar_words():
	"""

		Traverse all words to check how many words do not have a char

		traverse for all chars
	"""
	print ''
	
	start=ord('a')#convert char to int for iteration
	for i in range(26):
		char = chr(start+i)

		#print char
		#At this point , it just prints every alphabet
		print 'words containing',char,':',words_with_e(char,False)
		time.sleep(0.5)

		#To Do : 
		#Further => save as freq[e] = 76168
		
		#a graph can be added
		#alphabet wise and freq.wise

		#could use prettyTable to display results

