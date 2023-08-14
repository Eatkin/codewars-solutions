# https://www.codewars.com/kata/5a2166f355519e161a000019
# 2023-06-16T14:31:54.201+0000
import string
def construct_keyed_alphabet(key):
    # Make sure key only contains unique elements
    cache = []
    new_key = []
    for char in key:
        if char not in cache:
            cache.append(char)
            new_key.append(char)
    return new_key + [c for c in string.ascii_lowercase if c not in new_key]

def encode(text, key):
    keyed_alphabet = construct_keyed_alphabet(key)
    cypher = ""
    i = 0
    for letter in text:
        try:
            pos = keyed_alphabet.index(letter.lower())
            cypher += keyed_alphabet[(pos + i + 1) % 26].upper() if letter.isupper() else keyed_alphabet[(pos + i + 1) % 26]
            i += 1
        except:
            cypher += letter
            i = 0
    return cypher
    
def decode(text, key):
    keyed_alphabet = construct_keyed_alphabet(key)
    # Break into words
    cypher = ""
    i = 0
    for letter in text:
        try:
            pos = keyed_alphabet.index(letter.lower())
            cypher += keyed_alphabet[(pos - (i + 1)) % 26].upper() if letter.isupper() else keyed_alphabet[(pos - (i + 1)) % 26]
            i += 1
        except:
            cypher += letter
            i = 0
    return cypher