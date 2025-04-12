#write function that flattern a list
import numpy as np
def flatternlist(list_words):
    array = np.array(list_words)
    flat_array = array.flatten()
    return flat_array
print(flatternlist([[1, 2], [3, 4], [5, 6]]))