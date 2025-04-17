# Use sets to check if a sentence is a pangram.
import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(sentence.lower()))
