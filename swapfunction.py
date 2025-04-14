# Create a function that swaps keys and values.
def swap_function (obj):
    new_obj = {}
    for key in obj:
        new_obj[obj[key]] = key


