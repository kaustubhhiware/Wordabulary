from has_no_e import *
from words_with_e import *
import time
import string
from prettytable import PrettyTable

def allstar_words():
	"""

		Traverse all words to check how many words do not have a char

		traverse for all chars
	"""
	print ''
	table = PrettyTable(['Char','Freq','%'])

	start=ord('a')#convert char to int for iteration
	for i in range(26):
		char = chr(start+i)

		#print char 	#At this point , it just prints every alphabet
		#print 'words containing',char,':',words_with_e(char,False)

		freq = words_with_e(char,False)
		percent = 100.0*freq/113809
		percent = int(100*percent)/100.0
		table.add_row([char , freq , percent])	#Total number of words = 113809
		print 'Counting words with ',char,'...'
		time.sleep(0.5)

	print table
	#To Do : 
	#Further => save as freq[e] = 76168
	
	#a graph can be added
	#alphabet wise and freq.wise
