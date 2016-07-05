import time
from rotate import rotate_word
from prettytable import PrettyTable
from is_there_dict import create_dict
count = 0

def starts_with(substr,word):
    """

        return true if word starts with substr
    """
    l = len(substr)
    if len(word) < l:
        return False

    for i in range(l):
        if word[i]!=substr[i]:
            return False

    return True


def rotate_pairs(word, word_dict,table):
    """

    	Prints all words that can be generated by rotating word.
    """
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:

            #global table
            table.add_row([word,i,rotated])
            #print word, i, rotated
            
            global count
            count += 1
            time.sleep(0.01)


def iterate_rotors(substr):
    """

		Function to work of main in case imported as module
        prints only words starting with substr
    """
    table = PrettyTable(['Word','rotate id','rotated word'])

    word_dict = create_dict()
    for word in word_dict:
        if starts_with(substr,word):
            rotate_pairs(word, word_dict,table)

    print table
    time.sleep(1)
    global count
    print '\nTotal rotated pairs :',count 



if __name__ == '__main__':
    
    substr = raw_input("Enter substring from which words are to be rotated : ")
    iterate(substr)
