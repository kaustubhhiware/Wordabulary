# check this out - https://en.wikipedia.org/wiki/Moby_Project
import time

import length_sorter
import has_no_e 
import has_no_these 
import has_only_these  
import is_abecedarian 
import words_with_e 
import ends_with 
import allstar_words 
from prettytable import PrettyTable
import is_there 
import is_there_dict 
import reverse_pairs 
import interlocked 

#####
#####	install prettytable - pip install prettytable
#####


####
####	<3 : All functions are now imported for future clarity
####

if __name__=='__main__':
	
	print '\nWelcome to Wordabulary ! Choose your operation '

	while True:
		time.sleep(1)
		print '#operations '
		print '1 for printing words above some length'
		print '2 for checking if a group of letters are not present in a word'
		print '3 for checking if a group of letters are only present in a word'
		print '4 for checking if a group of letters are all exclusively present in a word'
		print '5 for checking if a word is abecedarian(arranged alphabetically)'
		print '6 for checking how many words contain given substring'
		print '7 for checking how many words end with given substring'
		print '8 for checking popularity of each char'
		print '9 for checking if given word makes sense'
		print '10 for printing all reverse pairs'
		print '11 for printing interlocked words'

		print 'and 0 to exit\n'
		option = raw_input("Enter choice : ")

		if option=='0':
			break

		elif option=='1':
			longword=raw_input("Print all longer words \nWhat min. length of words? ")
			longword = int(longword)
			length_sorter.length_sorter(longword)

		elif option=='2':
			not_letters = raw_input("Enter forbidden letter(s) ,separated by , : ").split(",")
			#not_let = map(char,not_letters.split(","))

			word=raw_input("Enter word to check for forbidden letter(s) : ")
			has_no_these.has_no_these(word,not_letters,True)#allow printing

		elif option=='3':
			only_letters = raw_input("Enter allowed letter(s), unseparated: ")

			word=raw_input("Enter word to check for allowed letter(s) : ")
			has_only_these.has_only_these(word,only_letters,True)#allow printing

		elif option=='4':
			fixed_letters = raw_input("Enter allowed letter(s), unseparated: ")

			word=raw_input("Enter word to check if all allowed letter(s) are present: ")
			has_only_these.has_only_these(fixed_letters,word,True)#allow printing

		elif option=='5':
			word = raw_input("Enter word to be checked for abecedarian : ")
			print is_abecedarian.is_abecedarian(word)		

		elif option=='6':
			substring = raw_input("Enter substring to check how many words have it : ")
			
			is_print = raw_input("Enter 1 to print , else nothing:")
			print_bool = False
			if is_print=='1':
				print_bool=True

			#if len(char)==1:
			count = words_with_e.words_with_e(substring,print_bool)
			#disable printing words without char

			time.sleep(2)#externally called to save time for allstars
			print '\nwords containing',substring,':',count

			#else:
			#	print 'char needs to be a single letter!'

		elif option=='7':
			#extend later to rhyming words - sky , bye
			substring=raw_input("Enter substring to check words which end with it : ")
			#printing mandatory
			ends_with.ends_with(substring)


		elif option=='8':
			print 'Crunching numbers ... displaying count of words containing each letter'
			allstar_words.allstar_words()


		elif option=='9':
			search_this = raw_input("Enter word to search for , in database : ")
			
			#	dict method faster upto 50% - for word boy
			# check speed , uncomment time prints in these files v

			#print 'Method 1 : list and append'
			#is_there.is_there(search_this)
			#print 'Method 2 : dict()'
			is_there_dict.is_there_dict(search_this)

		elif option=='10':
			print 'Displaying all reverse pairs:'
			char = raw_input("Begin with what letter? (all for complete) : ")
			reverse_pairs.reverse_pairs(char)


		elif option=='11':
			interlocked.interlocked()

#Total number of words = 113809
		else :
			print 'Incorrect choice :(\n'