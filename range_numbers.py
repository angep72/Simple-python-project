#Use max() and min() to find the range of values in a list.
def range_number (list_numbers):
    min_num = min(list_numbers)
    max_num = max(list_numbers)
    return min_num,max_num
print (range_number([1,2,4,35,6,8]))