#Write a function that removes all punctuation from a string.
import re
def punctuation(string):
    txt = re.sub(r'[^\w\s]','',string)
    return txt
