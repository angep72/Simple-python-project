# Write the function that uses lambda and map to change an array of strings to integers

def change_string_to_integer(list_number):
    result = list(map(int, list_number))
    return result;
print(change_string_to_integer(["1","2","3","4","5","6","7","8","9"]))