# Write a function that returns True if all elements are even.
def evennumbers (number_list):
    for number in number_list:
        if number % 2 != 0:
            return False
        else:
            continue
    return True

