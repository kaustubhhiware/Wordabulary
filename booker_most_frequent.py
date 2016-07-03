import random
import os.path
import time
from prettytable import PrettyTable

####
####    NOTE : booker_most_frequent counts all occurences while
####            allstar_words checks for number of words , they are different !
####

# this function pasted here as this file is imported in allstar for most_frequent
def get_percent_in2points(freq,total):
    """
        get percent of total from freq as xx.xx%
    """
    percent = 100.0*freq/total
    percent = int(100*percent)/100.0
    return percent


def make_histogram(s):
    """Make a map from letters to number of times they appear in s.

    s: string

    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist



def total_freq(t):
    """

        Return total occurences of letters
    """
    count = 0
    for freq,x in t:
        count += freq

    return count


def most_frequent(doc):
    """

        Sorts the letters in doc in reverse order of frequency.
    """
    hist = make_histogram(doc)

    t = []
    for x, freq in hist.iteritems():
        t.append((freq, x))

    t.sort(reverse=True)

    result = []
    #list of tuples

    tots = total_freq(t)
    for freq, x in t:
        
        #if x!=' ':
                    # space is not a char
        percentage = get_percent_in2points(freq,tots)
        result.append((x,freq,percentage))

    return result,tots


def read_file(filename):
    return open(filename).read()


def iterate(filer):
    """
		main function module
    """
    
    if not os.path.isfile(filer):
    	print '\tNot a valid file !Returning now...'
    	return 

    print '\tFile found!Working ...'
    doc = read_file(filer)
    table = PrettyTable(['Char','Freq','%'])

    out,tots = most_frequent(doc)
    for x,freq,percent in out:
        table.add_row([x,freq,percent])
        #print x

    print table
    time.sleep(1)
    print '\tTotal words in document : ',tots




if __name__ == '__main__':
    filer = raw_input("\tEnter your file : ")
    iterate(filer)
