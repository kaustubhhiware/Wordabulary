import time
from has_no_e import *

def ends_with(substring):
	"""
		check how many words ends with that substring
 	"""
	print 'Words ending with ',substring,'\n'

	#Approach 1
 	"""
	start_from = len(substring)
	count = 0
	start_time = time.time()
	fin = open('words.txt')
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

	print ' Approach 2'
	"""
	#Approach 2 found to be marginally faster
	# 0.2417 and 0.24107 - approach 2 overall better
	count = 0
	start_time = time.time()
	fin = open('words.txt')
	for line in fin:
		##Approach 2:check only for words containing that substring
		#####		Debug later and check which is faster
		word = line.strip()#get rid of \r

		if has_no_e(word,substring)==False:
			#the substring is already present in the words

			word_start = len(word) - len(substring)
			if word.find(substring,word_start)==word_start:
			#start finding from last 3rd in case of bro
				print word
				count += 1
				time.sleep(0.2)

	elapsed_time = time.time() - start_time
	print '\nTotal words :', count#,' in time :',elapsed_time
