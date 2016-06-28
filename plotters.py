import matplotlib.pyplot as plt

def plot_letters(letters,frequency):
	"""
		Takes 2 lists as input and prints graph
		x axis : letters
		y axis : frequency
	"""
	plt.plot(letters,frequency,'r')
	plt.title('Alphabet wise arrangement')
	plt.xlabel('Alphabets')
	plt.ylabel('Frequency')
	plt.axis([0, 27, 0, 76168])#xmin , xmax , ymin , ymax
	#y max at e - 76168
	plt.show()
