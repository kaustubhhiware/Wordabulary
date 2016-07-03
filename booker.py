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

		print '\n\t and 0 to exit this submenu'
	
		option = raw_input("\tYour choice :")

		if option=='0' or option=='clear':
			break


		elif option=='1':
			filer = raw_input("\tEnter your file (start with / if not local address ): ")
			booker_most_frequent.iterate(filer)	
		

		else :
			print '\tIncorrect choice :(\n'

		time.sleep(1)
		print '\n'



if __name__=='__main__':
	initialise()
