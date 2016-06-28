
def has_no_e(word,substring):
	"""
		check if given word has that substring
		e is the most common char ~ 67 percent frequency
 	"""
	#for char in word:
	#	if char==letter:
	#		return False
	#return True
 	bool = substring in word
	return not bool		#allows flexibility for substring