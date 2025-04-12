#Use sorted() to sort a list of tuples by the second element.
def sort_tuples(my_list):
    sorted_list = sorted(my_list, key=lambda x: x[1])
    return sorted_list
