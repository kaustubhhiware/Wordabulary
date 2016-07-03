import time
import booker_most_frequent

def initialise():
	"""

		submenu for dealing with books and docs
	"""
	print '\tLet\'s analyze some books and stuff'

	while True :
		print '\t#operations'
		print '\t1 for finding most frequent words in a book(txt file)'
		print '\t2 for finding most frequent words in a book(txt file)'
		print '\t3 for finding all typos in a book'
		print '\n\t and 0 to exit this submenu'
	
		option = raw_input("\tYour choice :")

		if option=='0' or option=='clear':
			break


		elif option=='1':
			filer=raw_input("\tEnter your file for freq dist(start with/if not local address):\n\t")
			booker_most_frequent.iterate_char(filer)	
		
		elif option=='2':
			filer=raw_input("\tEnter your file for word dist(start with/if not local address):\n\t")
			booker_correct.iterate_word(filer)

		elif option=='3':
			filer = raw_input("\tEnter your file for typos(start with/if not local address ): ")
			booker_correct.iterate(filer)	


		else :
			print '\tIncorrect choice :(\n'

		time.sleep(1)
		print '\n'



if __name__=='__main__':
	initialise()
