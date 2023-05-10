from requests import get as reqget
from re import split
import os.path

#Aufagbe 18
def pride_and_prejudice ():
    '''The novel ’Pride and Prejudice’ by Jane Austen.
    :return: list of words (text and Project Gutenberg header/footer).'''

    file_exists = os.path.exists('pap.txt')                         # check if file exists

    if file_exists == True:                                         # if True
        with open('pap.txt', 'r', encoding='utf-8') as f:           # open it as read
            t = f.read()
    else:                                                           # else
        papurl = 'http://www.gutenberg.org/ebooks/1342.txt.utf-8'   # go to url
        t = reqget(papurl).text                                     # retrieve the text from the URL
        with open('pap.txt', 'w', encoding='utf-8') as f:           # open as write with encoding utf-8!
            f.write(t)                                              # write to file pap.txt which then is also crated
                                                                    # Wortliste wird für Aufgabe 19 gebraucht
    t = split(r'[^A-Za-z]+', t)                                     # split by non-letters and return
    return [w for w in t if len(w) > 0]                             # return the list of words


def showText():
    with open('pap.txt', 'r', encoding='utf-8') as f:  # open it as read
        t = f.read()
    print(t)

#showText()


print("-"*30)
#Aufgabe 19


import hashlib

def get_hash(value):
    return int(hashlib.md5(value.encode('utf-8')).hexdigest(), 16)      # returns the hash value

def get_trailing_zeros(n):
    s = str(bin(n))                         # n gets converted to binary representation
    return len(s) - len(s.rstrip('0'))      # returns the number of trailing zeros

# Number of bitmasks
num_bitmasks = 20                           # change this value to set the lentgh of the bitmask
bitmasks = [0] * num_bitmasks
#print(bitmasks)

# Function to process a single element
def process_element(bitmasks, element):
    hash_value = get_hash(element)          # get hash value for element
    #print(hash_value)
    bitmask_index = hash_value % len(bitmasks)      # get bitmask index by calculting the hash value modulo len(bitmask)
    #print(bitmasks[bitmask_index],get_trailing_zeros(hash_value))
    bitmasks[bitmask_index] = max(bitmasks[bitmask_index], get_trailing_zeros(hash_value))      # returns the larger value
    # between the current maximum number of trailing zeros stored in bitmasks[bitmask_index] and the number of trailing
    # zeros in the current hash value.
    #print(bitmasks)

# Function to estimate the number of unique elements
def estimate_unique(bitmasks):
    return 2** (sum(bitmasks) / len(bitmasks))
    # bitmasks now is a list that contains the maximum number of trailing zeros observed for each hash value or as we learned
    # bucket. Each index in the list represents a "bucket", and the value at each index is the maximum number of trailing zeros
    # observed for hash values that fall into that bucket.

# Test the implementation
stream = pride_and_prejudice()
    # call the function which returns the list of string words to the stream in this case
    # the stream can be changed to different list e.g [1,2,3,1,2,6]

for element in stream:      #executes the code by going through the stream
    process_element(bitmasks, element)      # calling the function with the set bitmask and the element from the stream

print(estimate_unique(bitmasks))

