# Count how many times each digit appears in a number string.
def number_string(number_digit):
    new_result = []
    new_object = {}
    for digit in number_digit:
        new_result.append(digit)
    for digit in new_result:
        if digit not in new_object:
            new_object[digit] = 1
        else:
            new_object[digit] += 1
    return new_object
