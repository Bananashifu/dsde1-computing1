'''
structures.py

Simple functions performing operations on basic Python data structures.
'''

# Lists

# write a function that returns a list containing the first and the last element
# of "the_list".
def first_and_last(the_list):
    'Returns list consisting of first and last items'
    return list((the_list[0], the_list[-1]))


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list".
# If "end" is greater then "beginning" or any of the indices is out of the
# list, raise a "ValueError" exception.
def part_reverse(the_list, beginning, end):
    'Returns reversed slice of the_list'
    if beginning <= end <= len(the_list):
        return list(reversed(the_list[beginning:end]))


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4].
def repeat_at_index(the_list, index):
    'Returns a sorted list in which index appears thrice'
    return sorted(the_list + 2 * [index])


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    'Checks whether word is palindromic; case insensitive'
    return word.lower() == word[::-1].lower()


# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not.
def palindrome_sentence(sentence):
    'Checks whether a sentence is palindromic, ignoring spaces and letter case'
    sen = sentence.replace(' ', '')
    rev = sen[::-1]
    return sen.lower() == rev.lower()


# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence.
def concatenate_sentences(sentence1, sentence2):
    '''
    Concatenates two sentences ensuring they start with a capital letter; end with
    a full stop, question mark, or exclamation mark; and after stripping end whitespace
    '''
    sen1 = sentence1.strip()
    sen2 = sentence2.strip()

    condi_1A = sen1[0].isupper()
    condi_1B = bool(sen1[-1] == '.' or '?' or '!')

    condi_2A = sen2[0].isupper()
    condi_2B = bool(sen2[-1] == '.' or '?' or '!')

    if condi_1A and condi_1B and condi_2A and condi_2B:
        return sen1 + ' ' + sen2


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    'Checks whether a key exists in a dictionary'
    return key in dictionary.keys()

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    'Checks whether a value exists in a dictionary'
    return value in dictionary.values()

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    'Merges two dictionaries into a new dictionary'
    dictionary3 = {**dictionary1, **dictionary2}
    return dictionary3
    