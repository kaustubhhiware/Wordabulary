import os.path
import time
from prettytable import PrettyTable
import string

import histogram
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


def char_histogram(s):
    """

        Make a map from letters to number of times they appear in s.
        Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


def word_histogram(doc):
    """

        split words to get histogram for words

        doc is just one line of content
    """
    d = dict()
    punctuations = string.punctuation
    #print punctuations
    prev_pause = 0
    curr_pause = 0
    index = 0

    while index < len(doc):
        if doc[index] ==" " or doc[index] in punctuations:#split at spaces, comma, dot, etc

            if doc[index]=='\'' or doc[index]=='`':
                if doc[index+1]=='s':
                    continue#skip over if words like "nature's" come

            if index!=len(doc)-1 and doc[index+1]==" ":#new line sort
                prev_pause = index + 2
            else:
                #print 'punk : ',doc[index]
                curr_pause = index
                this_word = doc[prev_pause:curr_pause]
                this_word = this_word.lower()
                if this_word!='':
                    #print 'word:',this_word,':'
                    d[this_word] = d.get(this_word, 0) + 1
                prev_pause = curr_pause+1

        index += 1
    return d


def most_frequent(doc,typef='char',to_limit=False):
    """

        Sorts the typef in doc in reverse order of frequency.
    """
    if typef =='char':
        hist = histogram.histogram(doc)

    elif typef =='word':
        hist = word_histogram(doc)

    t = []
    for x, freq in hist.iteritems():
        t.append((freq, x))


    t.sort(reverse=True)

    result = []
    #list of tuples
    limit = 0# to limit only 20 most frequent words
    tots = total_freq(t)

    for freq, x in t:
        
        #if x!=' ':
        # space is not a char
        percentage = get_percent_in2points(freq,tots)
        result.append((x,freq,percentage))

        if typef=='word'and to_limit==False:
            limit += 1
            if limit==20:
                break

    return result,tots


def iterate(filer,typef='char'):
    """
		main function module
    """
    if not os.path.isfile(filer):
        print '\tNot a valid file !Returning now...'
        return 

    to_limit = False#Limit table display sie fr large docs

    print '\tFile found!Working ...'
    if typef=='char':
        doc = read_file(filer)
        out,tots = most_frequent(doc,'char')
        table = PrettyTable(['Char','Freq','%'])
    
    elif typef=='word':    
        #why this approach ? Well, it wasn't working with new lines.
        #courtesy http://stackoverflow.com/questions/19351164/multiple-line-file-into-one-string
        with open(filer) as f:
        
            data=''.join(line.rstrip() for line in f)
        
        print '\tNOTE : If your file is too big , the analysis may fail'
        to_limit = raw_input("\tEnter y to limit display top 20 entities : ")
        if to_limit=='y':
            to_limit = True

        out,tots = most_frequent(data,'word',to_limit)
        table = PrettyTable(['Word','Freq','%'])

    for x,freq,percent in out:
        table.add_row([x,freq,percent])

    print table
    time.sleep(1)
    print '\tTotal words in document : ',tots


if __name__ == '__main__':
    
    print '\t1 for finding most frequent words in a book(txt file)'
    print '\t2 for finding most frequent words in a book(txt file)'
    print '\n\t and 0 to exit this submenu'
    
    option = raw_input("\tYour choice :")
    print '\tTIP : start with / if address for file is not local'

    if option=='0' or option=='clear':
        exit

    elif option=='1':
        filer=raw_input("\tEnter your file for frequency distribution:\n\t")
        iterate(filer,'char')   
        
    elif option=='2':
        filer=raw_input("\tEnter your file for word distribution:\n\t")
        iterate(filer,'word')

    else :
        print '\tIncorrect choice :(\n'
