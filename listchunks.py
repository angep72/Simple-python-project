# Split a list into chunks of a given size.
def chunk_list(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]
