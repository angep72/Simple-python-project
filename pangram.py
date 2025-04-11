#Check if a sentence contains all 26 letters .
def is_pangram(sentence):
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(sentence.lower()))
