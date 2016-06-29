from has_no_e import *
from words_with_e import *
import time
import string
from prettytable import PrettyTable

import matplotlib.pyplot as plt
from plotters import *

def allstar_words():
	"""

		Traverse all words to check how many words do not have a char

		traverse for all chars
	"""
	print ''
	table = PrettyTable(['Char','Freq','%'])
	frequency=[]
	letters=[]

	start=ord('a')#convert char to int for iteration
	for i in range(26):
		char = chr(start+i)

		#print char 	#At this point , it just prints every alphabet
		#print 'words containing',char,':',words_with_e(char,False)
		letters.append(i+1)
		frequency.append(words_with_e(char,False))

		percent = 100.0*frequency[i]/113809
		percent = int(100*percent)/100.0
		table.add_row([char , frequency[i] , percent])	#Total number of words = 113809
		print 'Counting words with ',char,'...'
		time.sleep(0.08)

	time.sleep(1)
	print '\nTotal number of words = 113809'
	print table

	show_freq = raw_input("Enter y to display alphabet wise plot : ")
	if show_freq=='y':
		plot_letters(letters,frequency)


	#To Do : 
	
	#a graph can be added
	# freq.wise
