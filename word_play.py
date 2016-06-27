# check this out - https://en.wikipedia.org/wiki/Moby_Project

def length_sorter(longword):
	"""
		print all words only beyond some length
	"""
	count = 0
	fin = open('words.txt')
	for line in fin:
		word = line.strip()#get rid of \r
	
		if len(word) >=longword:
			print word
			count = count + 1
	print '\nTotal words printed : ',count


def has_no_e(word,letter):
	"""
		check if given word has that letter
		e is the most common 
	"""
	for char in word:
		if char==letter:
			return False
	return True


def has_no_these(word,not_letters):
	"""

		check if certain letters are not present in the word
	"""
	count_breach = 0
	for each_letter in not_letters:
		if has_no_e(word,each_letter):
			#print each_letter,' is not present'
			print 'working...'

		else: 
			print 'The barrier has been breached by ',each_letter
			count_breach = count_breach+1

	if count_breach > 0:
		print '\nWe have been compromised\n'
	else:
		print '\nThe coast is clear , mate\n'


if __name__=='__main__':
	
	print '\nWelcome to word_play ! Choose your operation '

	while True:
		
		print '#operations '
		print '1 for printing words above some length'
		print '2 for checking if a group of letters are not present in a word'
		print 'and 0 to exit\n'
		option = raw_input("Enter choice : ")

		if option=='0':
			break

		elif option=='1':
			longword=raw_input("Sort words on basis of length \n What min. length of printed words ? ")
			longword = int(longword)
			length_sorter(longword)

		elif option=='2':
			not_letters = raw_input("Enter forbidden letter(s) ,separated by , : ").split(",")
			#not_let = map(char,not_letters.split(","))

			word=raw_input("Enter word to check for forbidden letter(s) : ")
			has_no_these(word,not_letters)

		elif option=='3':
			print ''
		


		else :
			print 'Incorrect choice :(\n'