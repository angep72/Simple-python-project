# Compare two strings and return the number of different characters.
def comparison(string, string1):
    new_object= {}
    result_array = []
    new_array = string.split()
    second_array = string1.split()
    combined_array = [*new_array, *second_array]
    joined_word ="".join(combined_array)
    for key in joined_word:
        if key in new_object:
            new_object[key] +=1
        else:
            new_object[key] = 1
    print(new_object)
    for key in new_object:
        if new_object[key] == 1:
            result_array.append(key)
    return result_array


