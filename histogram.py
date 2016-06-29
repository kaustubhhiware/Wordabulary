import string

def histogram(string):
	"""

		provide a dict which returns char-wise distribution
	"""
	d = dict()
	for char in string:
		#if char not in d:
		#	d[char] = 1
		#else:
		#	d[char] += 1
		d[char] = d.get(char,0) + 1
				#	get key , default_value

	return d

def print_hist(h):
	for char in h:
		print char , h[char]

#TODO :
#check for a way to print_hist in order

