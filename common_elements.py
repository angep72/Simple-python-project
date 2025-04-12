#Write a function that returns the common elements between two lists.
def my_function(list1, list2):
    result = []
    for item in list1:
        for items in list2:
            if item == items:
                result.append(items)
    return result
