import time
from has_no_e import *

def ends_with(substring):
	"""
		check how many words ends with that substring
 	"""
	start_from = len(substring)
	print 'Words ending with ',substring,'\n'
	count = 0
	fin = open('words.txt')
	for line in fin:
		word = line.strip()#get rid of \r
	
		#print word
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
		

		##Approach 2:check only for words containing that substring
		#####		Debug later and check which is faster
		""" 
		if has_no_e(word,substring)=="False":
			#the substring is already present in the words
			
			print word
			word_start = len(word) - len(substring)
			if word.find(substring,word_start)==word_start:
			#start finding from last 3rd in case of bro
				print word
				count += 1
				time.sleep(0.2)
		"""

	print '\nTotal words:', count