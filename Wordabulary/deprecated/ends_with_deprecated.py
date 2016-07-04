import time
from has_no_e import *

def ends_with(substring):
	"""
		check how many words ends with that substring
 	"""
	print 'Words ending with ',substring,'\n'

	
	start_from = len(substring)
	count = 0
	start_time = time.time()
	fin = open('reference/words.txt')
	for line in fin:
		word = line.strip()#get rid of \r

		##Approach 1 : first consider only words above certain length ,
		##				then search if it ends

		#consider bro as substring
		if len(word) >= start_from:
		#no point checking if bro is present in hi

			#print word
			word_start = len(word) - len(substring)
			if word.find(substring,word_start)==word_start:
			#start finding from last 3rd in case of bro
				print word
				count += 1
				time.sleep(0.2)

	elapsed_time = time.time() - start_time
	print '\nTotal words:', count,' in time :',elapsed_time


if __name__=='__main__':

	substring=raw_input("Enter substring to check words which end with it : ")
	
	ends_with(substring)