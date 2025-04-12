#Remove duplicates from a list using set() and return a list.
def sort_tuples(tuples):
    result = set(tuples)
    return tuple(result)