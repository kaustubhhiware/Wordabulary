from has_no_e import *
import time

def words_with_e(substring,is_print):
	"""

		Traverse all words to check how many words do not have this substring
		Changed  to return only number for now
		e is the most common letter
	"""
	#print ''
	if is_print:
		print 'Words with',substring
	count = 0
	fin = open('words.txt')
	for line in fin:
		word = line.strip()#get rid of \r
	
		if has_no_e(word,substring):#how do you even mess this up

			count = count + 1
		else:
			if is_print:
				print word
				time.sleep(0.1)
	#Total number of words = 113809
	count = 113809 - count# faster to check how many words don't have that letter
	
	return count