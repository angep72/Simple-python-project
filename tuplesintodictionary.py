# write a function that turns a list of tuples into a dictionary
# [(1, 'apple'), (2, 'orange'), (3, 'cherry')]
def convert_tuples(list_of_tuples):
    new_dictionary = {}
    for tuple in list_of_tuples:
        new_dictionary[tuple[0]] = tuple[1]
    return new_dictionary

# #alternative way and simple one
# def tuples_to_dict(tuples_list):
#     return dict(tuples_list)
