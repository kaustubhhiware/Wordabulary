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
	fin = open('reference/words.txt')
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


if __name__=='__main__':
	substring = raw_input("Enter substring to check how many words have it : ")
			
	is_print = raw_input("Enter 1 to print , else nothing:")
	print_bool = False
	if is_print=='1':
		print_bool=True
		#if len(char)==1:
		count = words_with_e(substring,print_bool)
			#disable printing words without char

	time.sleep(2)#externally called to save time for allstars
	print '\nwords containing',substring,':',count