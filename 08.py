from bitarray import bitarray


from requests import get as reqget
from re import split
import os.path

#Aufagbe 18 # für den pride and prejudice text
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


#Aufgabe 20
class BloomFilter:

    def __init__(self, size, hash_functions):
        self.size = size
        self.hash_functions = hash_functions
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)
        self.count = 0      # für Aufgabe 21

    def add(self, string):
        for hash_func in self.hash_functions:
            result = hash_func(string) % self.size
            self.bit_array[result] = 1

    # methode für aufgabe 21 ein wenig geändert
    def add21(self, string):
        is_new = False
        for hash_func in self.hash_functions:
            result = hash_func(string) % self.size
            if self.bit_array[result] == 0:
                self.bit_array[result] = 1
                is_new = True
        if is_new:
            self.count += 1

    def lookup(self, string):
        for hash_func in self.hash_functions:
            result = hash_func(string) % self.size
            if self.bit_array[result] == 0:
                return "Wrong" # brauchen wir später für check
        return "Probably" # brauchen wir für zusatzaufgabe 1a

    # Trivial count für 21
    def trivial_count(self):
        return self.count

    # Improved count für 21
    def improved_count(self):
        b1 = self.bit_array.count(1)
        return -self.size / len(self.hash_functions) * np.log(1 - b1 / self.size)

    # Zusatzaufgabe 1a
    def add_check_duplicate(self, string):
        if self.lookup(string) == "Probably":
            print(f'Duplicate detected: {string}')
        else:
            self.add(string)

# alle hash funktionen
def jhash (s, m=31):            # Java hash function for strings
    if isinstance(s, ''.__class__):
        s = s.encode('utf-8')   # turn string into byte literal
    h = 0                       # compute a hash value for a string
    for c in s: h = h *m +c     # by a simple multiply and add method
    return h                    # return the computed hash value

def djb2hash (s, m=33):         # [Daniel Justus Bernstein]
    if isinstance(s, ''.__class__):
        s = s.encode('utf-8')   # turn string into byte literal
    h = 5381                    # compute a hash value for a string
    for c in s: h = h *m +c     # by a simple multiply and add method
    return h                    # return the computed hash value

def sdbmhash (s, m=65599):      # (like jhash, but with different factor)
    if isinstance(s, ''.__class__):
        s = s.encode('utf-8')   # turn string into byte literal
    h = 0                       # compute simple hash value for a string
    for c in s: h = h *m +c; h &= 0xffffffff
    return h                    # return the computed hash value

def jenkinshash (s):            # [Bob Jenkins 1997]
    if isinstance(s, ''.__class__):
        s = s.encode('utf-8')   # turn string into byte literal
    h = 0                       # start with zero
    for c in s:                 # traverse the characters of the string
        h += c                  # add next character to the hash value
        h += h << 10            # and do some magic operations
        h ^= h >> 6
        h &= 0xffffffff         # limit to 32 bits
    h += h << 3                 # do some more magic operations
    h ^= h >> 11
    h += h << 15
    h &= 0xffffffff             # limit to 32 bits
    return h                    # return the computed hash value

def fnvhash32 (s):              # Fowler-Noll-Vo hash function (32 bits)
    if isinstance(s, ''.__class__):
        s = s.encode('utf-8')   # turn string into byte literal
    h = 2166136261              # set the offset basis
    for c in s:                 # xor and multiply with prime number
        h = ((h ^ c) *16777619) & 0xffffffff
    return h                    # return the computed hash value

def fnvhash64 (s):              # Fowler-Noll-Vo hash function (64 bits)
    if isinstance(s, ''.__class__):
        s = s.encode('utf-8')   # turn string into byte literal
    h = 14695981039346656037    # set the offset basis
    for c in s:                 # xor and multiply with prime number
        h = ((h ^ c) *1099511628211) & 0xffffffffffffffff
    return h                    # return the computed hash value

#Liste aus unseren hash funktionen
hash_functions = [jhash, djb2hash, sdbmhash, jenkinshash, fnvhash32, fnvhash64]



# erstelle Filter mit den hash funktionen
def build_bloom_filter(words_file, size, hash_num):
    bloom_filter = BloomFilter(size, hash_num)
    with open(words_file, 'r') as file:
        for line in file:
            word = line.strip()
            bloom_filter.add(word)
    return bloom_filter


def spell_check(bloom_filter, text_file):
    misspelled_words = set()
    for word in text_file:
        if bloom_filter.lookup(word) == "Wrong":
            misspelled_words.add(word)
    return misspelled_words


# erstelle Filter mit allen hash funktionen und der bitmask
bloom_filter = build_bloom_filter("words.txt", 2**20, hash_functions)
#print(bloom_filter)

# initialisiere die misspelled_words
misspelled_words = spell_check(bloom_filter, pride_and_prejudice())
#für testen auskommentiert
for word in misspelled_words:
    #print(word)
    pass

# nicht sicher ob groß und klein schreibung zu richtig oder falsch führt
# benutzt für liste auf allen Wörtern
def build_word_list(words):
    word_list = set()
    with open(words, 'r') as file:
        for line in file:
            word = line.strip()
            word_list.add(word)
    return word_list

# überprüft ob das wort aus dem text in der liste der wörter ist
def exact_spell_check(word_list, prideAndPrejudice):
    misspelled_words = set()
    for word in prideAndPrejudice:
        if word not in word_list:
            misspelled_words.add(word)
    return misspelled_words
#inizialisiert für oben
word_list = build_word_list("words.txt")
#print(word_list)

# inizialisert das exakte ergebnis
exact_misspelled_words = exact_spell_check(word_list, pride_and_prejudice())
# können Wöter ausgeben, da untersChied gering ist jetzt auskommentiert
for word in exact_misspelled_words:
    #print(word)
    pass

print(f'Exact count: {len(exact_misspelled_words)}')
print(f'Our count: {len(misspelled_words)}')
print(exact_misspelled_words)
print(misspelled_words)

# Aufgabe 21
print("-"*30)
import numpy as np
import pandas as pd

def count_distinct_elements(strings, size, hash_num):
    bloom_filter = BloomFilter(size, hash_functions[:hash_num])
    for string in strings:
        bloom_filter.add21(string)
    return bloom_filter.trivial_count(), bloom_filter.improved_count()

# Test the function on Pride and Prejudice with different sizes and numbers of hash functions
sizes = [2**x for x in range(10, 17)]
hash_nums = [k for k in range(1, len(hash_functions) + 1)]
results = pd.DataFrame(index=hash_nums, columns=sizes)

for size in sizes:
    for hash_num in hash_nums:
        results[size][hash_num] = count_distinct_elements(pride_and_prejudice(), size, hash_num)

print(results)
# Das Ergebnis zeigt, dass der Bloom-Filter mit zunehmender Größe der Bitmaske (von 1024 bis 65536)
# eine immer genauere Schätzung der Anzahl eindeutiger Elemente im Text von "Pride and Prejudice" liefert.

# vergleich mit wahren Werten aus Aufgabe 19 haben wir nicht ganz implementiert da wir bei unserer Lösung
# nicht das exakte Ergebnis bekommen und keine Musterlösung stand jetzt online ist.

# Zusatzaufgabe test

# Neuer Bloom-Filter
bloom_filter = BloomFilter(2**20, hash_functions)

# Erstellen einer Liste von Strings, einige davon sind Duplikate
stringsListZusatz = ["Austria", "Spain", "France", "Austria", "Germany", "Sweden", "Germany"]

# check für duplikate
#for string in pride_and_prejudice():
#    bloom_filter.add_check_duplicate(string)

for string in stringsListZusatz:
    bloom_filter.add_check_duplicate(string)
