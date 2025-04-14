# Group words that are anagrams using a dictionary.

from collections import defaultdict

def group_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))  # Sort letters to form the key
        anagram_dict[key].append(word)
    return dict(anagram_dict)
