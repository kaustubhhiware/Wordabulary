from pronounce import pronounce_dict
from is_there_dict import create_dict


def homophones(a, b, phonetic):
    """
        Checks if words a and b two can be pronounced the same way.

        phonetic: map from words to pronunciation codes
    """
    if a not in phonetic or b not in phonetic:
        return False

    return phonetic[a] == phonetic[b]


def check_rhyme(singel,word,word_dict,phonetic):
    """

        check if word rhymes with singel 

        word: string
        #word_dict: dictionary with words as keys
        #phonetic: map from words to pronunciation codes
    """

    p_a = phonetic[singel]
    p_b = phonetic[word]

    a = p_a[::-1]
    b = p_b[::-1]

    if a[0]==b[0]:
        return True
    else:
        return False


def rhyming(singel):
    """
        print rhyming words using the cmu dictionary
    """
    phonetic = pronounce_dict()
    word_dict = create_dict()
    
    for word in word_dict:
        if check_rhyme(singel,word, word_dict, phonetic):
            print word


if __name__ == '__main__':
    phonetic = pronounce_dict()
    word_dict = create_dict()

    for word in word_dict:
        if check_word(singel,word, word_dict, phonetic):
            print word
