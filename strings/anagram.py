from collections import Counter

# First solution
def is_anagram(string1, string2):
    """
    Checks if two strings are an anagram
    """

    # remove whitespaces
    string1_processed = whitespace_lower(string1)
    string2_processed = whitespace_lower(string2)

    counts1 = Counter(string1_processed.lower())
    counts2 = Counter(string2_processed.lower())
    return (counts1 == counts2)

def whitespace_lower(word_w_space):
    """
    Function that removes whitespace from a string
    """
    word_list = word_w_space.split(" ")
    return_string = ""
    for word in word_list:
        word_lower = word.lower()
        word_alpha = ''.join(x for x in word_lower if x.isalpha())
        return_string += word_alpha
    return return_string