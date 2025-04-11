# Build a function that capitalizes the first letter of each word in a string.

def capitalize_word(string):
    result = []
    new_string = string.split(" ")
    for num in new_string:
        x = num.capitalize()
        result.append(x)

    return " ".join(result)


