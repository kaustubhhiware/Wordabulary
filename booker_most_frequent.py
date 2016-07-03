#import random
import os.path
import time
from prettytable import PrettyTable
import string
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


def total_freq(t):
    """

        Return total occurences of letters
    """
    count = 0
    for freq,x in t:
        count += freq

    return count


def read_file(filename):
    return open(filename).read()


def make_histogram(s):
    """

        Make a map from letters to number of times they appear in s.
        Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


def most_frequent_char(doc):
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


def iterate_char(filer):
    """
		main function module
    """
    
    if not os.path.isfile(filer):
        print '\tNot a valid file !Returning now...'
        return 

    print '\tFile found!Working ...'
    doc = read_file(filer)
    table = PrettyTable(['Char','Freq','%'])

    out,tots = most_frequent_char(doc)
    for x,freq,percent in out:
        table.add_row([x,freq,percent])
        #print x

    print table
    time.sleep(1)
    print '\tTotal words in document : ',tots


def word_histogram(doc):
    """

        split words to get histogram for words
    """
    d = dict()

    punctuations = string.punctuation
    #print punctuations
    
    prev_pause = 0
    curr_pause = 0
    index = 0

    while index < len(doc):

        if doc[index] ==" " or doc[index] in punctuations:#split at spaces, comma, dot, etc

            if index!=len(doc)-1 and doc[index+1]==" ":#new line sort
                prev_pause = index + 2
            else:
                #print 'punk : ',doc[index]
                curr_pause = index
                this_word = doc[prev_pause:curr_pause]
              
                if this_word!='' and this_word!=' \n':

                    print 'word:',this_word,':'

                prev_pause = curr_pause+1

        index += 1

def most_frequent_word(doc):

    word_histogram(doc)


def iterate_word(filer):
   
    if not os.path.isfile(filer):
        print '\tNot a valid file !Returning now...'
        return 

    print '\tFile found !Working ...'
    doc = read_file(filer)

    out = most_frequent_word(doc)



if __name__ == '__main__':
    
    print '\t1 for finding most frequent words in a book(txt file)'
    print '\t2 for finding most frequent words in a book(txt file)'
    
    print '\n\t and 0 to exit this submenu'
    
    option = raw_input("\tYour choice :")

    if option=='0' or option=='clear':
        exit


    elif option=='1':
        filer=raw_input("\tEnter your file for freq dist(start with/if not local address):\n\t")
        iterate_char(filer)   
        
    elif option=='2':
        filer=raw_input("\tEnter your file for word dist(start with/if not local address):\n\t")
        iterate_word(filer)
