
def has_no_e(word,letter):
	"""
		check if given word has that letter
		e is the most common 
	"""
	for char in word:
		if char==letter:
			return False
	return True