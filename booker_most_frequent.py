import random
import os.path

def most_frequent(s):
    """Sorts the letters in s in reverse order of frequency.

    s: string

    Returns: list of letters
    """
    hist = make_histogram(s)

    t = []
    for x, freq in hist.iteritems():
        t.append((freq, x))

    t.sort(reverse=True)

    res = []
    for freq, x in t:
        res.append(x)

    return res
    

def make_histogram(s):
    """Make a map from letters to number of times they appear in s.

    s: string

    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


def read_file(filename):
    """Returns the contents of a file as a string."""
    return open(filename).read()


def iterate(filer):
    """
		main function module
    """
    
    if not os.path.isfile(filer):
    	print '\tNot a valid file !'
    	return 
    print 'File found!Working ...'
    s = read_file(filer)
    t = most_frequent(s)
    for x in t:
        print x

if __name__ == '__main__':
    filer = raw_input("\tEnter your file : ")
    iterate(filer)
