# Build a function to count occurrences of each letter in a string.

def occurrence(string):
    new_obj = {}

    for char in string:
        if char in new_obj:
            new_obj[char] += 1
        else:
            new_obj[char] = 1
    return new_obj


