from bisect import bisect_left
#Perfect example of hiding in plain sight

def in_bisect(word_list, word):
    """

    	Binary search for word in sorted word_list
    """
    i = bisect_left(word_list, word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False


def word_list():
    """
    	Prepare word list to search in
    """
    word_list = []
    fin = open('words.txt')

    for line in fin:
        word = line.strip()
        word_list.append(word)
    
    return word_list

def is_there(word):
	"""

		search for given word with binary sort
		You'd think , you could just do 
		word in list , n00b
		Guess what,  it would take you ages !Go ahead , smarta$$
	"""
	listed = word_list()

	print '\n',word, 'in list : ', in_bisect(listed,word)
