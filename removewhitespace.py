# Write a function that removes all whitespace from a string.

def remove_whitespace(string):
    new_string = string.split(" ")
    joined_string = "".join(new_string)
    return joined_string

