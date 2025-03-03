'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 
def first_and_last(the_list):
    A = the_list[0]
    B = the_list[-1]
    return [ A, B]


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):
    if beginning < end and end < len(the_list)-1:
        new_list_a = the_list[beginning:end]
        new_list_b = new_list_a.reverse()
    return(new_list_b)


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    new_list = the_list[0,index-1] + the_list[index] * 3 + the_list[index+1::]
    return(new_list)


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    word = word.lower()
    drow = word[::-1]
    result = drow == word
    return result

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    new_sentence = ''.join(e for e in sentence if e.isalnum())
    new_new_sentence = new_sentence.lower()
    reversed_sentence = new_new_sentence[::-1]
    result = reversed_sentence == new_new_sentence
    return result

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentence1, sentence2):
    s1 = sentence1.strip()
    s2 = sentence2.strip()
    if s1[-1] in '.!?':
        if s2[-1] in '.!?':
            if s1[0].isupper() and s2[0].isupper():
                result = s1 + ' ' + s2
                return result
            else:
                raise ValueError
        else:
            raise ValueError
    else:
        raise ValueError


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False


# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    if value in dictionary.values():
        return True
    else:
        return False
    return

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    A = {**dictionary1, **dictionary2}
    return A
