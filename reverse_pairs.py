from is_there import *
import time


def is_reverse_there(word_list, word):
    """

        Checks whether a reversed word appears in word_list.
    """
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)
        

def reverse_pairs(char):
    """
    
        print all reverse pair words
    """   
    listed = word_list()
    count = 0 

    for word in listed:

        if char!='all':
            if word[0]!=char:
                continue
                #continue if word doesn't begin with letter

        if is_reverse_there(listed, word):
            count += 1
            print word, word[::-1]
            time.sleep(0.01)
            if char!='all':
                time.sleep(0.04)#so le jara , so le jara

    print '\nTotal words : ',count,'\n'